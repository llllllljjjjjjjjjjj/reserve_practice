import requests, os, subprocess, json
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
tolal = 0
for i in range(1, 6):    
    page = i
    if(i == 5):
        headers['user-agent'] = 'yuanrenxue'
    with open(path_cur, 'r', encoding='utf-8') as f:
        js_code = f.read()

    # 直面 GBK 问题：显式指定子进程编码为 utf-8
    node_script = f"""
    {js_code}
    console.log(get_m({page}))
    """
    p = subprocess.Popen(
        ['node'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )
    stdout, stderr = p.communicate(input=node_script)
    if p.returncode != 0:
        raise RuntimeError(stderr)

    m = stdout.strip()
    print('生成的 m:', m)

    params = {
        'page': page,
        'pageSize': '10',
        'kw': '',
        'm': m,
    }

    response = requests.get('https://match.yuanrenxue.cn/api/question/1', params=params, cookies=cookies, headers=headers)
    arr1 = json.loads(response.text)['data']
    #print(arr1)    
    for j in arr1:
        tolal += j
print(tolal)