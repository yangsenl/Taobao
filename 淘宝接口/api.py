from flask import Flask, request,jsonify
import urllib.parse
from ultis import *
import asyncio
app = Flask(__name__)
import  json
@app.route("/send", methods=['POST', 'GET'])
def send():
    if request.method == "POST":
        query = request.form.get('q')
        start=request.form.get('start')
        end=request.form.get('end')
        url = 'https://shopsearch.taobao.com/search?'
        params = {
            'app': 'shopsearch',
            'q': query,
            'search_type': 'shop',
            's': ''
        }
        urls = []
        for i in range(int(start), int(end)):
            url = url + urllib.parse.urlencode(params) + str( 10* i)
            urls.append(url)
        tasks = [asyncio.ensure_future(get_html(url)) for url in urls]
        loop = asyncio.get_event_loop()
        datas= loop.run_until_complete(asyncio.gather(*tasks))
        dicts={'status':1,
               'data':datas}
        return json.dumps(dicts)
    elif request.method == "GET":
        query = request.args.get('q')
        page=request.args.get('page')
        # start=request.args.get('start')
        # end=request.args.get('end')
        base_url = 'https://shopsearch.taobao.com/search?'
        types=request.args.get('type')
        if type==None:
            types=''
        params = {
            'app': 'shopsearch',
            'q': query,
            'search_type': 'shop',
            's': '',
            'ratesum':types,
        }
        urls = []
        for i in range(int(page), int(page)+1):
            url = base_url + urllib.parse.urlencode(params) + str( 10* i)
            urls.append(url)
        tasks = [asyncio.ensure_future(get_html(url)) for url in urls]
        loop = asyncio.get_event_loop()
        datas= loop.run_until_complete(asyncio.gather(*tasks))
        dicts={'status':1,
               'datas':datas}
        return jsonify(dicts)

@app.route("/shop", methods=['POST', 'GET'])
def shop():
    if request.method == "POST":
        query = request.form.get('q')
        # start=request.form.get('start')
        # end=request.form.get('end')
        # low_price = request.args.get('low_price')
        # high_price = request.args.get('high_price')
        url = 'https://s.taobao.com/search?'
        page= request.form.get('page')
        if page==None:
            page=1
        urls = []
        for i in range(int(page), int(page)+1):
            params = {
                'q': '{}'.format(query),
                # 'filter': 'reserve_price[{}, {}]'.format(low_price, high_price),
                'bcoffset': '{}'.format(9 - i * 3),
                'ntoffset': '{}'.format(9 - i * 3),
                'p4ppushleft': '1,48',
                's': '{}'.format((i - 1) * 44),
            }

            url = url + urllib.parse.urlencode(params)
            urls.append(url)
        print(urls)
        tasks = [asyncio.ensure_future(get_shop(url)) for url in urls]
        loop = asyncio.get_event_loop()
        datas= loop.run_until_complete(asyncio.gather(*tasks))
        dicts={'status':1,
               'data':datas}
        return json.dumps(dicts)
    elif request.method == "GET":
        query = request.args.get('q')
        start=request.args.get('start')
        end=request.args.get('end')
        low_price = request.args.get('low_price')
        high_price = request.args.get('high_price')
        url = 'https://s.taobao.com/search?'
        page = request.args.get('page')

        if page == None:
            page = 1
        urls = []
        print(page)
        for i in range(int(page), int(page) + 1):
            params = {
                'q': '{}'.format(query),
                # 'filter': 'reserve_price[{}, {}]'.format(low_price, high_price),
                'bcoffset': '{}'.format(9 - i * 3),
                'ntoffset': '{}'.format(9 - i * 3),
                'p4ppushleft': '1,48',
                's': '{}'.format((i - 1) * 44),
            }

            url = url + urllib.parse.urlencode(params)
            urls.append(url)
        print(urls)
        tasks = [asyncio.ensure_future(get_shop(url)) for url in urls]
        loop = asyncio.get_event_loop()
        datas= loop.run_until_complete(asyncio.gather(*tasks))
        dicts={'status':1,
               'datas':datas}
        return jsonify(dicts)
if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8080)
    app.run(port=8080)


