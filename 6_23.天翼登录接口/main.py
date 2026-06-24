"""
1.pb:
2.cp:
3.reqId
4.referer
5.:path

"""
import requests, time, execjs, os, random, string, re, base64, ddddocr,json

base_dir = os.path.dirname(os.path.abspath(__file__))
js_path = os.path.join(base_dir, '1.js')

with open(js_path, 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
user = {
    'zhanghao': '15083702253', 
    'pwd':'123456'
}
def get_img():    
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://open.e.189.cn/api/logbox/separate/web/index.html?appId=E_189&lt=01EC4DD16E9ECC61CB5D009B2F65F88B6A7DA261E021AF28C96A2A68AC17B1454CB249EF3753FBE78005DA085983DC71EDEC0828B1C5F99063BDCE255101ED6B79EA6E42AA987D22D2AE19B18D53B96C2EDC91F8&reqId=0a5007004f9e488691e2060e79962e1d&encryptUrl=8E8BD2989F169B69B202137391188971E3586DC1DB772E7ADD36D3FE26AFAFE994FF164B69847B1AC91324B456B50231B4F919370661B7CA32EA47A6B87F2A42DCAFF7B92BF783F304B7A074BCD4405E3DD6BADDD3FD661A9708F54D88E2A041FE2BB84498E350BE8129B5E11F336928B9EE4554AC53EE5F0425770E7D628BEFC379C2C3AA55278CAE3FDCDAE3DE2422026CB1FFC2211332CE497C0E27C8A85F0FEEB303',
        'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-storage-access': 'active',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    }

    time_now = int(time.time() * 1000)
    randomStr = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

    data = {
        "appId": "E_189",
        "captchaType": 1,
        "referer": headers['referer'],
        "time": time_now,
        "finger": 3881141159,
        "width": "310"
    }

    public_key = ctx.eval('PUBLIC_KEY')
    cp = ctx.call('get_cp', randomStr, public_key)
    pb = ctx.call('get_pb', data, randomStr)
    reqId = ctx.call('get_reqId')

    params = {
        'callback': 'callback_' + str(time_now),
        'pb': pb,
        'cp': cp,
        'appId': 'E_189',
        'version': '1.0.1',
        'reqId': reqId,
    }

    response = requests.get('https://open.e.189.cn/gw/captcha/get.do', params=params, headers=headers)
    reg_bg = r'"bg":"([^"]+)"'
    reg_token = r'"token":"([^"]+)"'
    reg_front = r'"front":"([^"]+)"'
    
    # re.S 让.匹配换行，适配多行响应文本
    bg_match = re.search(reg_bg, response.text, re.S)
    token_match = re.search(reg_token, response.text, re.S)
    front_match = re.search(reg_front, response.text, re.S)

    result = {
        "bg": bg_match.group(1) if bg_match else None,
        "front": front_match.group(1) if front_match else None,
        "token": token_match.group(1) if token_match else None
    }
    return result 
iiii = get_img()
token = iiii['token']
retire_img = iiii['bg']
part_img = iiii['front']
def save_img(url, name):
    match = re.match(r'data:image/\w+;base64,(.+)', url)
    if match:
        img_data = base64.b64decode(match.group(1))
        save_path = os.path.join(base_dir, name)
        with open(save_path, 'wb') as f:
            f.write(img_data)
        print(f"图片已经保存在 {save_path}")
    else:
        print("无法解析图片数据")
save_img(retire_img, 'retire.jpg')
save_img(part_img, 'part.png')
def get_x_y():
    slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

    with open(os.path.join(base_dir, 'retire.jpg'), 'rb') as f:
        background = f.read()

    with open(os.path.join(base_dir, 'part.png'), 'rb') as f:
        target = f.read()

    result = slide.slide_match(target, background, simple_target=True)
    print('ddddocr raw result:', result)

    # 兼容多种返回值格式
    if isinstance(result, list) and len(result) > 0:
        # 旧版列表格式: [{'target': [x, y, w, h]}]
        item = result[0]
        if isinstance(item, dict) and 'target' in item:
            x = int(item['target'][0])
            y = int(item['target'][1])
        else:
            x = int(item[0])
            y = int(item[1])
    elif isinstance(result, dict):
        # 新版字典格式: {'target': [x, y, w, h]}
        x = int(result['target'][0])
        y = int(result['target'][1])
    else:
        raise ValueError(f'Unexpected ddddocr result format: {result}')

    print(f'ddddocr parsed x={x}, y={y}')
    return x, y

x, y = get_x_y()
print(x, y)
t111 = [
    {
        "x": x,
        "y": 0
    }
]
hhhhh = ctx.call('generateSlideTrack', x)
data = {
    'token': iiii['token'],
    'captchaType': 1,
    'points': t111,
    'rates': hhhhh['track'],
    'dragTime': hhhhh['totalTime'],
    'time': int(time.time() * 1000),
    'finger': 3881141159
        
}
print(data)

def get_check():
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://open.e.189.cn/api/logbox/separate/web/index.html?appId=E_189&lt=01EC4DD16E9ECC61CB5D009B2F65F88B6A7DA261E021AF28C96A2A68AC17B1454CB249EF3753FBE78005DA085983DC71EDEC0828B1C5F99063BDCE255101ED6B79EA6E42AA987D22D2AE19B18D53B96C2EDC91F8&reqId=0a5007004f9e488691e2060e79962e1d&encryptUrl=8E8BD2989F169B69B202137391188971E3586DC1DB772E7ADD36D3FE26AFAFE994FF164B69847B1AC91324B456B50231B4F919370661B7CA32EA47A6B87F2A42DCAFF7B92BF783F304B7A074BCD4405E3DD6BADDD3FD661A9708F54D88E2A041FE2BB84498E350BE8129B5E11F336928B9EE4554AC53EE5F0425770E7D628BEFC379C2C3AA55278CAE3FDCDAE3DE2422026CB1FFC2211332CE497C0E27C8A85F0FEEB303',
        'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-storage-access': 'active',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    }
    
    pb_and_cb = ctx.call("get_pb2_cp2", data)
    params = {
        'pb': pb_and_cb['pb'],
        'cp': pb_and_cb['cp'],
        'appId': 'E_189',
        'version': '1.0.1',
        'reqId': ctx.call("get_reqId"),
        'callback': 'callback',
    }
    response = requests.get('https://open.e.189.cn/gw/captcha/check.do', params=params, headers=headers)
    #print(params['pb'])
    json1 = response.text.split('callback(')[-1].split(')')[0]
    print(json1)
    dict = json.loads(json1)
    return dict['data'], pb_and_cb['i']
plain , i= get_check()
print(plain, i)
cipher = ctx.call('aes_decrypt', plain, i, i)
print(cipher)
cipher = json.loads(cipher)








headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'lt': '06B76336C3146472D4DC5AF082CCF8DBA514D598C6BB3086CDAFC3FBD227AFCA0ED17A83D99C682A0CAD1BCB23CE6FA9837D1DC493707B5F1C25AA7C79578549F7D9E3F579BCB27FFDF7ED8BCE97272A3654712A',    'origin': 'https://open.e.189.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://open.e.189.cn/api/logbox/separate/web/index.html?appId=E_189&lt=06B76336C3146472D4DC5AF082CCF8DBA514D598C6BB3086CDAFC3FBD227AFCA0ED17A83D99C682A0CAD1BCB23CE6FA9837D1DC493707B5F1C25AA7C79578549F7D9E3F579BCB27FFDF7ED8BCE97272A3654712A&reqId=1f31a2b9c0b14018bb744dbc8e4d3842&encryptUrl=8E8BD2989F169B69B202137391188971E3586DC1DB772E7ADD36D3FE26AFAFE994FF164B69847B1AC91324B456B50231B4F919370661B7CA32EA47A6B87F2A42DCAFF7B92BF783F304B7A074BCD4405E3DD6BADDD3FD661A9708F54D88E2A041FE2BB84498E350BE8129B5E11F336928B9EE4554AC53EE5F0425770E7D628BEFC379C2C3AA55278CAE3FDCDAE3DE2422026CB1FFC2211332CE497C0E27C8A85F0FEEB303',    'reqid': '0fcfdcbcd46a493a85c0460a714ddfe4',
    'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    'user-finger': '3881141159',
}


data = {
    'version': 'v2.0',
    'apToken': '',
    'appKey': 'E_189',
    'pageKey': 'normal',
    'accountType': '02',
    'userName': '{NRP}'+ ctx.call('encrypt', user['zhanghao']),
    'epd': '{NRP}' + ctx.call('encrypt', user['pwd']),
    'captchaType': '1',
    'validateCode': cipher['validate'],
    'smsValidateCode': cipher['validate'],
    'captchaToken': cipher['token'],
    'returnUrl': 'https%3A%2F%2Fe.dlife.cn%2Fuser%2FloginMiddle.do%3FreturnUrlMid%3DaHR0cHM6Ly9lLmRsaWZlLmNuL3BvcnRhbC93ZWIvaW5kZXguaHRtbCZCRDJDRDU0REYzMkZFRkQ0NEZDQkE0QzhDNEJERTI0QTQ3RUEzOEI5',    'mailSuffix': '',
    'dynamicCheck': 'FALSE',
    'clientType': '1',
    'cb_SaveName': '0',
    'isOauth2': 'true',
    'state': '',
    'paramId': '58E1DF862B40CD836A64D5CD968A66B5CD1EE8BADFC232173FC4A5AACD774648E999C2DD2AB93A813AD257907AD9F107E24ACA19FAE50B1707B956A1AF6285373E177238',}
print(data)
response = requests.post('https://open.e.189.cn/api/logbox/oauth2/loginSubmit.do', headers=headers, data=data)
print(response.text)