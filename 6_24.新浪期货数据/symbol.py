import requests

cookies = {
    'UOR': ',finance.sina.com.cn,',
    'SFA_version10.3.0': '2026-06-24%2017%3A12',
    'SINAGLOBAL': '117.41.135.108_1782292643.542122',
    'Apache': '117.41.135.108_1782292643.542124',
    'hqEtagMode': '0',
    'ULV': '1782292800303:2:2:2:117.41.135.108_1782292643.542124:1782292644295',
    'SGUID': '1782292800790_15253218',
    'SR_SEL': '1_511',
    'U_TRS1': '0000006c.770be28a.6a3ba1f5.b67ce657',
    'U_TRS2': '0000006c.7711e28a.6a3ba1f5.b1758541',
    'Hm_lvt_90c40f528e0b2106bc03da5aadec190f': '1782293026',
    'HMACCOUNT': 'DB68F4C4F92A8401',
    'Hm_lpvt_90c40f528e0b2106bc03da5aadec190f': '1782293033',
    'rotatecount': '6',
    'FIN_ALL_VISITED': 'TA0%2CV2609%2CV0',
    'NEWESTVISITED_FUTURE': '%7B%22code%22%3A%22TA0%22%2C%22hqcode%22%3A%22nf_TA0%22%2C%22type%22%3A1%7D%7C%7B%22code%22%3A%22V2609%22%2C%22hqcode%22%3A%22nf_V2609%22%2C%22type%22%3A1%7D%7C%7B%22code%22%3A%22V0%22%2C%22hqcode%22%3A%22nf_V0%22%2C%22type%22%3A1%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://finance.sina.com.cn/futures/quotes/TA0.shtml',
    'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    # 'cookie': 'UOR=,finance.sina.com.cn,; SFA_version10.3.0=2026-06-24%2017%3A12; SINAGLOBAL=117.41.135.108_1782292643.542122; Apache=117.41.135.108_1782292643.542124; hqEtagMode=0; ULV=1782292800303:2:2:2:117.41.135.108_1782292643.542124:1782292644295; SGUID=1782292800790_15253218; SR_SEL=1_511; U_TRS1=0000006c.770be28a.6a3ba1f5.b67ce657; U_TRS2=0000006c.7711e28a.6a3ba1f5.b1758541; Hm_lvt_90c40f528e0b2106bc03da5aadec190f=1782293026; HMACCOUNT=DB68F4C4F92A8401; Hm_lpvt_90c40f528e0b2106bc03da5aadec190f=1782293033; rotatecount=6; FIN_ALL_VISITED=TA0%2CV2609%2CV0; NEWESTVISITED_FUTURE=%7B%22code%22%3A%22TA0%22%2C%22hqcode%22%3A%22nf_TA0%22%2C%22type%22%3A1%7D%7C%7B%22code%22%3A%22V2609%22%2C%22hqcode%22%3A%22nf_V2609%22%2C%22type%22%3A1%7D%7C%7B%22code%22%3A%22V0%22%2C%22hqcode%22%3A%22nf_V0%22%2C%22type%22%3A1%7D',
}

params = {
    'symbol': 'TA0',
    '_': '2026_6_24',
}

response = requests.get(
    'https://stock2.finance.sina.com.cn/futures/api/jsonp.php/var%20_TA02026_6_24=/InnerFuturesNewService.getDailyKLine',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)
