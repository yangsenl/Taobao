import  requests
import json
# 'http://1.198.6.194:8080/send?q=优衣库&start=1&end=2'
url='http://127.0.0.1:5000/send?'
data={
    'q':'连衣裙',
    'start':'1',
    'end':2,
}
data=requests.post(url,data=data).text
data=json.loads(data)
print(data['data'])
# http://127.0.0.1:5000/send?q=连衣裙&start=1&end=2
import urllib.parse
import re
url='https://s.taobao.com/search?'
urls=[]
for i in range(1,10):
    params={
    'q': '连衣裙',
    'bcoffset': '{}'.format(9-i*3),
    'ntoffset': '{}'.format(9-i*3),
    'p4ppushleft': '1,48',
    's': '{}'.format((i-1)*44),
    }

    url=url+urllib.parse.urlencode(params)
    urls.append(url)
# print(urls)
# datas=get_html(url)
# print(datas)
# import asyncio
# tasks = [asyncio.ensure_future(get_html(url)) ]
# loop = asyncio.get_event_loop()
# datas= loop.run_until_complete(asyncio.gather(*tasks))
# print(datas)