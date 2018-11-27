import   requests
import  re
import urllib.parse
import aiohttp
import json
async  def  get_cookies(url):
    async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=20) as response:
                    text= await response.text()
    return text

#异步执行
async def get_html(url):
    try:
        html = await get_cookies('http://127.0.0.1:5000/taobao/random')
        cookies = json.loads(html)
    except:
        cookies = ''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'cookie': 'thw=cn; isg=BE5OFXA3mWBmlC1Fl-1AmV2WnCS83lEHkmUhbHiXutEM2-414F9i2fSZF8cSWArh; t=2f3e9153ea7a2a647a56e75f01d78641; cookie2=13a062c5802762794a0a8090188e42e4; _tb_token_=ee45733bebee1; cna=rrxRFN8nUBICAQHGBsLdcToK; _cc_=WqG3DMC9EA%3D%3D; tg=0; mt=ci=0_0; enc=sOpwz0gIVzAzR9ZmRO3XxKHaAhXb5YgwMuHdkTS39KlqWa9zUxykilMbYSz9B7q5lNAEMCB0Godx8U2iAPvCmQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; JSESSIONID=9DB8DCE70DDFAF8F3EA0353D725C73E6; swfstore=23378; v=0', }
    async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers,timeout=20) as response:
                    text= await response.text()
                    uids = re.findall('"uid":"(\d+)",', text)
                    persons = re.findall('"nick":"(.*?)",', text)
                    shop_names = re.findall('"rawTitle":"(.*?)",', text)
                    mainAuctions = re.findall('"mainAuction":"(.*?)",', text)
                    totalsolds = re.findall('"totalsold":(\d+),', text)
                    procnts = re.findall('"procnt":(\d+),', text)
                    provcitys = re.findall('"provcity":"(.*?)",', text)

                    datas = []
                    for uid, person, shop_name, mainAuction, totalsold, procnt, provcity in zip(uids, persons,
                                                                                                shop_names,
                                                                                                mainAuctions,
                                                                                                totalsolds, procnts,
                                                                                                provcitys):
                        data = {}
                        data['uid'] = uid
                        data['person'] = person
                        data['shop_name'] = shop_name
                        data['mainAuction'] = mainAuction.split('0000')[0]
                        data['totalsold'] = totalsold
                        data['procnt'] = totalsold
                        data['provcity'] = provcity
                        datas.append(data)
                    return datas


# 商品
async def get_shop(url):
    try:
        html = await get_cookies('http://127.0.0.1:5000/taobao/random')
        cookies = json.loads(html)
    except:
        cookies = ''

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'cookie': 'thw=cn; isg=BP7-DRbkKXTd7n1V550w6Q1mTBTsLoF34vWRXKgHYME8S5wlEM5lyd8Hx5eH6LrR; t=2f3e9153ea7a2a647a56e75f01d78641; cna=rrxRFN8nUBICAQHGBsLdcToK; _cc_=WqG3DMC9EA%3D%3D; tg=0; mt=ci=0_0; enc=sOpwz0gIVzAzR9ZmRO3XxKHaAhXb5YgwMuHdkTS39KlqWa9zUxykilMbYSz9B7q5lNAEMCB0Godx8U2iAPvCmQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; cookie2=10c8458316632eba50a4dfd3b3236b36; v=0; _tb_token_=5e8763338abe4; JSESSIONID=BE8F39ABC275487B2EA0465859C2F307; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com', }
#
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            text = await response.text()


            persons = re.findall('"nick":"(.*?)",', text)
            'https://amos.alicdn.com/getcid.aw?&v=3&groupid=0&s=1&charset=utf-8&uid=jkjs%E6%97%97%E8%88%B0%E5%BA%97&site=cntaobao'

            view_sales = re.findall('"view_sales":"(.*?)",', text)
            shop_names = re.findall('"raw_title":"(.*?)",', text)
            icons = re.findall('"item_loc":"(.*?)",', text)
            uids = re.findall('"nid":"(\d+)",', text)
            view_prices = re.findall('"view_price":"(.*?)",', text)
            # view_sales=re.findall('"view_sales":"(.*?)",', text)

            datas = []
            for uid, person, shop_name, view_sale, icon, view_price in zip(uids, persons, shop_names,
                                                                           view_sales, icons,
                                                                           view_prices):
                data = {}
                shop_url='https://detail.tmall.com/item.htm?id={}'.format(uid)
                data['shop_url']=shop_url
                data['uid'] = uid
                data['person'] = person
                data['shop_name'] = shop_name
                data['icon'] = icon
                data['view_price'] = view_price
                data['view_sale']=view_sale
                datas.append(data)
            return datas


#普通函数
def  get():
    url='https://shopsearch.taobao.com/search?'
    q='优衣库'
    page=1
    params={
    'app':'shopsearch',
        'q':q,
        'search_type':'shop',
    's':int(page)*10
    }
    url=url+urllib.parse.urlencode(params)
    print(url)
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
             'cookie': 'cna=9ElQFDE84HACAQHGBsLRCWLc; isg=BE1NmC2oKudKeI7JbmMDVXWCXGlrO8Iyg_mm4o_Si-RThm04V3mDzdZX9FpFRpm0',}
    text=requests.get(url,headers=headers).text
    uids = re.findall('"uid":"(\d+)",', text)
    persons = re.findall('"nick":"(.*?)",', text)
    shop_names = re.findall('"rawTitle":"(.*?)",', text)
    mainAuctions = re.findall('"mainAuction":"(.*?)",', text)
    totalsolds = re.findall('"totalsold":(\d+),', text)
    procnts = re.findall('"procnt":(\d+),', text)
    provcitys = re.findall('"provcity":"(.*?)",', text)
    print(uids)

    datas=[]
    for uid, person, shop_name, mainAuction, totalsold, procnt, provcity in zip(uids, persons, shop_names, mainAuctions,
                                                                                totalsolds, procnts, provcitys):
        data = {}
        data['uid'] = uid
        data['person'] = person
        data['shop_name'] = shop_name
        data['mainAuction'] = mainAuction.split('0000')[0]
        data['totalsold'] = totalsold
        data['procnt'] = totalsold
        data['provcity'] = provcity
        datas.append(data)
    print(datas)
    # return datas

if __name__ == '__main__':
    pass