import requests, os, subprocess
base_dir = os.path.dirname(os.path.abspath(__file__))
path_cur = os.path.join(base_dir, '1.js')
print(path_cur)
cookies = {
    'Hm_lvt_f80b2b389f44bbfb3bfe1704817d44e0': '1782788768',
    'HMACCOUNT': 'DB68F4C4F92A8401',
    'sessionid': 'ejymx8r9cv8d7q3yv4u8667otnqqa0g3',
    'Hm_lpvt_f80b2b389f44bbfb3bfe1704817d44e0': '1782798145',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://match.yuanrenxue.cn/match/1',
    'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}
# 让 Node 自己读 1.js，绕过 execjs 的 GBK 编码问题
page = 1
js_path = path_cur.replace('\\', '/')
runner = f"""
const fs = require('fs');
eval(fs.readFileSync('{js_path}', 'utf8'));
console.log(get_m({page}));
"""
res = subprocess.run(['node', '-e', runner], capture_output=True, text=True, encoding='utf-8')
if res.returncode != 0:
    raise RuntimeError(f'Node 执行出错: {res.stderr}')
m = res.stdout.strip()
print('生成的 m:', m)

params = {
    'page': page,
    'pageSize': '10',
    'kw': '',
    'm': m,
}

response = requests.get('https://match.yuanrenxue.cn/api/question/1', params=params, cookies=cookies, headers=headers)
print(response.text)
