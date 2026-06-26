import requests
import sys
import json
# 强制stdout为utf8
sys.stdout.reconfigure(encoding='utf-8')
cookies = {
    '__snaker__id': 'ZGc591q9UA15eN71',
    'PC_TOKEN': 'aa595332f7',
    'SVB': '_2AkMdYF_If8NxqwFRnPgSxGLlZY9_zQ3EieKrPK4TJRMxHRl-yT9yqmE6tRB6NuBxJxLV-Yoir98HUUPNvr2f7aKY-2Yi',
    'SUB': '_2AkMdYF_If8NxqwFRnPgSxGLlZY9_zQ3EieKrPK4TJRMxHRl-yT9yqlZctRB6NuBxJxOC-qO9n1-aNbkKsT2bzlFZ24XY',
    'SUBP': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhEHCKPIauTWpjfA9QnbGhY',
    'SRT': 'D.QqHBTrs%21d4SaNdRtOeYoWrSNUbBe43YGOFoTdOba5bmqMdbbN3HANqM4NbHi5mYNUCsuPDbuVdoTR3MNAZSKW4HtNeYLApsoOqblJNsYOcHhN3i4JcHwUmSTJZMRdA77%2AB.vAflW-P9Rc0lR-ykKDvnJqiQVbiRVPBtS%21r3J8sQVqbgVdWiMZ4siOzu4DbmKPWfM4YDNsBHRQP4P3BgS%21mu4du8M-YS',
    'SRF': '1782370559',
    'X-CSRF-TOKEN': 'CK-Yco4ZCoEmc_gZJX1wDXOsEWzoEWxIxacaxoFzC_gwxaEZCH0=',
    'gdxidpyhxdE': 'GVWj2baEQ6s3x7pYjEp%5Ct2b4Ae4VS1Jhs9vmAnmMBX6GJjYK%5CKkP3JbZWqixgy44UoKZuxH6iC%2BbO5vXJGAQBePKxHIPdZm%2FAmd2GV2LJhp9nzqsgvhoV0YRaUEaphMvOtwaE1PKt5QmQC68b6DuH2mvN0x0LWTQHZBRweXP55MZVdaK%3A1782371476151',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://passport.weibo.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://passport.weibo.com/sso/signin?entry=miniblog&source=miniblog&disp=popup&url=https%3A%2F%2Fweibo.com%2Fnewlogin%3Ftabtype%3Dweibo%26gid%3D102803%26openLoginLayer%3D0%26url%3D&from=weibopro',
    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'x-csrf-token': 'CK-Yco4ZCoEmc_gZJX1wDXOsEWzoEWxIxacaxoFzC_gwxaEZCH0=',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': '__snaker__id=ZGc591q9UA15eN71; PC_TOKEN=aa595332f7; SVB=_2AkMdYF_If8NxqwFRnPgSxGLlZY9_zQ3EieKrPK4TJRMxHRl-yT9yqmE6tRB6NuBxJxLV-Yoir98HUUPNvr2f7aKY-2Yi; SUB=_2AkMdYF_If8NxqwFRnPgSxGLlZY9_zQ3EieKrPK4TJRMxHRl-yT9yqlZctRB6NuBxJxOC-qO9n1-aNbkKsT2bzlFZ24XY; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhEHCKPIauTWpjfA9QnbGhY; SRT=D.QqHBTrs%21d4SaNdRtOeYoWrSNUbBe43YGOFoTdOba5bmqMdbbN3HANqM4NbHi5mYNUCsuPDbuVdoTR3MNAZSKW4HtNeYLApsoOqblJNsYOcHhN3i4JcHwUmSTJZMRdA77%2AB.vAflW-P9Rc0lR-ykKDvnJqiQVbiRVPBtS%21r3J8sQVqbgVdWiMZ4siOzu4DbmKPWfM4YDNsBHRQP4P3BgS%21mu4du8M-YS; SRF=1782370559; X-CSRF-TOKEN=CK-Yco4ZCoEmc_gZJX1wDXOsEWzoEWxIxacaxoFzC_gwxaEZCH0=; gdxidpyhxdE=GVWj2baEQ6s3x7pYjEp%5Ct2b4Ae4VS1Jhs9vmAnmMBX6GJjYK%5CKkP3JbZWqixgy44UoKZuxH6iC%2BbO5vXJGAQBePKxHIPdZm%2FAmd2GV2LJhp9nzqsgvhoV0YRaUEaphMvOtwaE1PKt5QmQC68b6DuH2mvN0x0LWTQHZBRweXP55MZVdaK%3A1782371476151',
}

data = {
    'entry': 'miniblog',
    'source': 'miniblog',
    'type': '1',
    'url': 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=',
    'ver': '20250520',
    #
    'username': '5844787262590d7f58447c',
    #
    'pass': '408f9e624068361e86dcb9bb65eb5f34b7777882a9ee102eda1e4aaa89e00d69c8703e6bd78931be7b806f9c0b5a1110dfb461951bde653b19f51b0abc7b081dfba0cd76af9eee73c65298746da60c55916d3f1a0e6f664c795fa48142c79ee94e2a68e3107add515d64a5031bec8c440e5d884001c8fe1559f835d43ad8c2bb',
    'cid': '3Y2JqPNEQABXe4iRSsca2TapPxXQ5aky_C3Jpc2tfdmVyaWZ5',
    'pwencode': 'rsa',
    'rsakv': '1330428213',
    'disp': 'popup',
    #
    'rid': '02ASDA6Iq05x_U_QyHllGCdkyu6uyP',
    'el': '1',
}

response = requests.post('https://passport.weibo.com/sso/v2/login', cookies=cookies, headers=headers, data=data)
print(response.text)