import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'lt': '2A1E3DE641B507BB0C76BFC572BCE4FDEA786C49F0E280BE8B3202A20AA31F7214EC21A3838F64CB85F3DC6E7A659C3C8BB9B7C40234144301F2FB4280C82F19C2627807AC7B12CE8FB3119A0F6CD6D48CEB0156',
    'origin': 'https://open.e.189.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://open.e.189.cn/api/logbox/separate/web/index.html?appId=E_189&lt=2A1E3DE641B507BB0C76BFC572BCE4FDEA786C49F0E280BE8B3202A20AA31F7214EC21A3838F64CB85F3DC6E7A659C3C8BB9B7C40234144301F2FB4280C82F19C2627807AC7B12CE8FB3119A0F6CD6D48CEB0156&reqId=52c482a1944249159e581a1b16d382eb&encryptUrl=8E8BD2989F169B69B202137391188971E3586DC1DB772E7ADD36D3FE26AFAFE994FF164B69847B1AC91324B456B50231B4F919370661B7CA32EA47A6B87F2A42DCAFF7B92BF783F304B7A074BCD4405E3DD6BADDD3FD661A9708F54D88E2A041FE2BB84498E350BE8129B5E11F336928B9EE4554AC53EE5F0425770E7D628BEFC379C2C3AA55278CAE3FDCDAE3DE2422026CB1FFC2211332CE497C0E27C8A85F0FEEB303',
    'reqid': '52c482a1944249159e581a1b16d382eb',
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
    'userName': '{NRP}793d4b4e61ff972e7216654fcee88605ea9ce52a6998a01c2a19524bfe045e3f6a4d2a1fa67a44024a9f1f4c20e2c7cadd12f08ca12cf833db3f83d24f0b8d14593cabd1a0406d1390bda6dbc77a3ff6a3b973a95b1ab065026019bcd8eb160e7e160231741ce50ace5d341d4bcf84734ee1b978c3021573e1f892e10a564cfe',
    'epd': '{NRP}5493c67504de07c2b06a79c0dee693c631cf1497fad54a470086b89c479770440c2579b59533ce9f455a4d3528181ea177d4cca1e6823ee9b36c5bce27d5be6bbb28d5522286a0b74930e9c160ab72a8020f3261032425e765ad298b1c603c28989c01c73e48b5f219161a1c744526ca2356b9ac5134a04bbf1447a09e43ff90',
    'captchaType': '1',
    'validateCode': '70217a52cba737f87fda923191203c6f2fd0b780e807106f305a5ae0980069c3b7a0d65dfa2f891e9e5df8431e0dc62d7876b52b5a201afddab972f0ac01e30a',
    'smsValidateCode': '70217a52cba737f87fda923191203c6f2fd0b780e807106f305a5ae0980069c3b7a0d65dfa2f891e9e5df8431e0dc62d7876b52b5a201afddab972f0ac01e30a',
    'captchaToken': '40ee93be8b5648a48ba7e7ba72395aed',
    'returnUrl': 'https%3A%2F%2Fe.dlife.cn%2Fuser%2FloginMiddle.do%3FreturnUrlMid%3DaHR0cHM6Ly9lLmRsaWZlLmNuL3BvcnRhbC93ZWIvaW5kZXguaHRtbCZCRDJDRDU0REYzMkZFRkQ0NEZDQkE0QzhDNEJERTI0QTQ3RUEzOEI5',
    'mailSuffix': '',
    'dynamicCheck': 'FALSE',
    'clientType': '1',
    'cb_SaveName': '0',
    'isOauth2': 'true',
    'state': '',
    'paramId': '3195336B8D31ED40D5D8CCF23AEBD9425297686D3653376AC0CE97F607EE1754E348CB9748E6E590416C4251B725E095A8F0A3C24C3FD61C3EEE0C44490C4E78FEA6BD18',
}

response = requests.post('https://open.e.189.cn/api/logbox/oauth2/loginSubmit.do', headers=headers, data=data)



