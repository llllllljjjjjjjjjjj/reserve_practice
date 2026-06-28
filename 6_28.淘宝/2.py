import requests
import hashlib

def get_md5(text: str) -> str:
    # 1. 创建md5对象
    md5_obj = hashlib.md5()
    # 2. 字符串必须编码为bytes（utf-8）再更新
    md5_obj.update(text.encode("utf-8"))
    # 3. 获取32位小写十六进制md5结果
    md5_hex = md5_obj.hexdigest()
    return md5_hex
def aaa():
    cookies = {
        'thw': 'cn',
        't': 'b25abb0107d26ae1355f8eef83104d80',
        'aui': '2218208617778',
        'cna': 'HtQIIa3kbDQCAXOWQtw1UUYR',
        'cookie2': '1f18fee858bf51f0344adc91dc29bc58',
        '_tb_token_': '7eb34e38307e1',
        'xlly_s': '1',
        'mtop_partitioned_detect': '1',
        '_m_h5_tk': 'b804b40cc093993580a02a8e13702a54_1782663038054',
        '_m_h5_tk_enc': '2e79edc2a4c03bf15271a88d91cde590',
        '3PcFlag': '1782654488002',
        'wk_cookie2': '1672216e80a0c8d0610b79ee5836c630',
        'wk_unb': 'UUpgTsupqYQ6cIsHpA%3D%3D',
        'sgcookie': 'E100Ue%2BNSEPmoY2IkhTidraBjsbjw7xLMQ%2Bwek%2Buzc0I%2FojZilDdBEI%2Fhk3asGlCgOxFoAO1fog5WoEQKIJU878Z7KZ652rxeCPTUfESYlTjASr%2FPlhH%2BGEOrYeVMg9gchBZ',
        'unb': '2218208617778',
        'csg': 'ee1a869a',
        'lgc': 'tb530666708967',
        'cancelledSubSites': 'empty',
        'cookie17': 'UUpgTsupqYQ6cIsHpA%3D%3D',
        'dnk': 'tb530666708967',
        'skt': 'feb78f2802c7e6f5',
        'tracknick': 'tb530666708967',
        '_l_g_': 'Ug%3D%3D',
        'sg': '782',
        '_nk_': 'tb530666708967',
        'cookie1': 'VynKMYML67jWxeDOL%2FwcMcPuD2tzEuTm%2B0BexFnEIdE%3D',
        'uc1': 'cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&pas=0&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie14=UoYWPyKFhCXQrg%3D%3D',
        'sn': '',
        'uc3': 'nk2=F5RAQUl3%2BS3alYH5CHA%3D&id2=UUpgTsupqYQ6cIsHpA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dD1NV%2FcP%2FdcsOfrO4%3D',
        'existShop': 'MTc4MjY1NDUwOA%3D%3D',
        'uc4': 'nk4=0%40FY4L7Qb0Y0TwyVu%2BrmPvMafLcE3URRDUog%3D%3D&id4=0%40U2gqwYJcJkvExOjYqMoSvr2J5KVY71vx',
        '_cc_': 'WqG3DMC9EA%3D%3D',
        '_hvn_lgc_': '0',
        'havana_lgc2_0': 'eyJoaWQiOjIyMTgyMDg2MTc3NzgsInNnIjoiNTY5MDE3MWI3YjFkOWVkNGU2ZTVjZWMyZmViMjRmYzAiLCJzaXRlIjowLCJ0b2tlbiI6IjFEM3BldkJlYzVLTm5ZMjVPWEdIc3ZRIn0',
        'tfstk': 'hmREhE9hp5ixAA1pV18dV0k_U6LdPHV7N_sIIhSMkkZBrg1y43-PATmdOQ-wohECx81hrT-pX99Ct_sPqntNx2KWdQ5yf3uscjao2PXPMwVhqu6GsZEl69wtGeLLSyroldv56f-Au8Vkq9jGsZIG-WjlEVWGlafutTV3IljOr_jkqgXGIwQFq72hx50NyGjlZ_xkSV7PjgflZ3YGPlNyCQdWYsVnby5jPwWF47sO0ig5R9SD-BPQOAberxc5iSk5mKIChhxi1W5ySa-Cfnc0_1X2HU_yYXPhOHJ0D7PWcWmiNCjyDL6zy0uD1d-XYHaoRxoFv1RDP5hEHCT1OE-0eqAm-FvkfB4-u2kDVH8esomqwpY61htiTzR-HHfvy3bN7w9FvABGqLf0e8BpBNSjJ2e8e9bO7igZ78eRp1QNc23d.',
        '_samesite_flag_': 'true',
        'ultraCookieBase': '1k6S5%2BcxkgQpZVJ5N08GM2MXJWGTU13jDoIgVX0c0A6r2K21VhQI%2F5BZf3T8c%2Be6qtm4K1UBzkKOqAnbefND4cab9aXjOnyTe9XtcR1uuQMPB8U7riKpErBxfbzSV8YHhTFClEE1L3RHKz1WPd8mIS0Xf5jXESqB3Riy9cwSbb3Jq35%2FXuYotzxr8jbBWjiLeXGP0Lie98KysLUbY1drT%2FlRU5y9OQRTA%2FGlxTIHhghc64X6p0ZLNeXn4%2F1JK7ifYoI2ApMinA20RYg2G2ARHbIXF4U1s1YS8t%2BDofTgkcg4Y%2BYvbOKrSUjL%2F%2FaFQmadu%2B8Neo5IrzLbHlKs%3D',
        'havana_lgc_exp': '1813760296654',
        'sdkSilent': '1782685096653',
        'havana_sdkSilent': '1782685096653',
        'isg': 'BGBg895AHuKh6aEXcEjpD_QdMW4yaUQzPzurl9p5C3s71RP_gHvVw3yjbX3V5fwL',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://uland.taobao.com/sem/tbsearch',
        'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
        # 'cookie': 'thw=cn; t=b25abb0107d26ae1355f8eef83104d80; aui=2218208617778; cna=HtQIIa3kbDQCAXOWQtw1UUYR; cookie2=1f18fee858bf51f0344adc91dc29bc58; _tb_token_=7eb34e38307e1; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=b804b40cc093993580a02a8e13702a54_1782663038054; _m_h5_tk_enc=2e79edc2a4c03bf15271a88d91cde590; 3PcFlag=1782654488002; wk_cookie2=1672216e80a0c8d0610b79ee5836c630; wk_unb=UUpgTsupqYQ6cIsHpA%3D%3D; sgcookie=E100Ue%2BNSEPmoY2IkhTidraBjsbjw7xLMQ%2Bwek%2Buzc0I%2FojZilDdBEI%2Fhk3asGlCgOxFoAO1fog5WoEQKIJU878Z7KZ652rxeCPTUfESYlTjASr%2FPlhH%2BGEOrYeVMg9gchBZ; unb=2218208617778; csg=ee1a869a; lgc=tb530666708967; cancelledSubSites=empty; cookie17=UUpgTsupqYQ6cIsHpA%3D%3D; dnk=tb530666708967; skt=feb78f2802c7e6f5; tracknick=tb530666708967; _l_g_=Ug%3D%3D; sg=782; _nk_=tb530666708967; cookie1=VynKMYML67jWxeDOL%2FwcMcPuD2tzEuTm%2B0BexFnEIdE%3D; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&pas=0&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie14=UoYWPyKFhCXQrg%3D%3D; sn=; uc3=nk2=F5RAQUl3%2BS3alYH5CHA%3D&id2=UUpgTsupqYQ6cIsHpA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dD1NV%2FcP%2FdcsOfrO4%3D; existShop=MTc4MjY1NDUwOA%3D%3D; uc4=nk4=0%40FY4L7Qb0Y0TwyVu%2BrmPvMafLcE3URRDUog%3D%3D&id4=0%40U2gqwYJcJkvExOjYqMoSvr2J5KVY71vx; _cc_=WqG3DMC9EA%3D%3D; _hvn_lgc_=0; havana_lgc2_0=eyJoaWQiOjIyMTgyMDg2MTc3NzgsInNnIjoiNTY5MDE3MWI3YjFkOWVkNGU2ZTVjZWMyZmViMjRmYzAiLCJzaXRlIjowLCJ0b2tlbiI6IjFEM3BldkJlYzVLTm5ZMjVPWEdIc3ZRIn0; tfstk=hmREhE9hp5ixAA1pV18dV0k_U6LdPHV7N_sIIhSMkkZBrg1y43-PATmdOQ-wohECx81hrT-pX99Ct_sPqntNx2KWdQ5yf3uscjao2PXPMwVhqu6GsZEl69wtGeLLSyroldv56f-Au8Vkq9jGsZIG-WjlEVWGlafutTV3IljOr_jkqgXGIwQFq72hx50NyGjlZ_xkSV7PjgflZ3YGPlNyCQdWYsVnby5jPwWF47sO0ig5R9SD-BPQOAberxc5iSk5mKIChhxi1W5ySa-Cfnc0_1X2HU_yYXPhOHJ0D7PWcWmiNCjyDL6zy0uD1d-XYHaoRxoFv1RDP5hEHCT1OE-0eqAm-FvkfB4-u2kDVH8esomqwpY61htiTzR-HHfvy3bN7w9FvABGqLf0e8BpBNSjJ2e8e9bO7igZ78eRp1QNc23d.; _samesite_flag_=true; ultraCookieBase=1k6S5%2BcxkgQpZVJ5N08GM2MXJWGTU13jDoIgVX0c0A6r2K21VhQI%2F5BZf3T8c%2Be6qtm4K1UBzkKOqAnbefND4cab9aXjOnyTe9XtcR1uuQMPB8U7riKpErBxfbzSV8YHhTFClEE1L3RHKz1WPd8mIS0Xf5jXESqB3Riy9cwSbb3Jq35%2FXuYotzxr8jbBWjiLeXGP0Lie98KysLUbY1drT%2FlRU5y9OQRTA%2FGlxTIHhghc64X6p0ZLNeXn4%2F1JK7ifYoI2ApMinA20RYg2G2ARHbIXF4U1s1YS8t%2BDofTgkcg4Y%2BYvbOKrSUjL%2F%2FaFQmadu%2B8Neo5IrzLbHlKs%3D; havana_lgc_exp=1813760296654; sdkSilent=1782685096653; havana_sdkSilent=1782685096653; isg=BNbWbzT-oOCyL5e1iobHTc6rJ4zYdxqxtc19tUA9zblUA3KdqgXTwW21m5_vqxLJ',
    }

    params = {
        'jsv': '2.7.2',
        'appKey': '12574478',
        't':str(int(time.time() * 1000)),
        'sign': '82bc8c33ea8afb2a7c2348c1f4b72ee1',
        'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
        'v': '2.0',
        'type': 'jsonp',
        'dataType': 'jsonp',
        'callback': 'mtopjsonp1',
        'data': '{"appId":"43356","params":"{\\"device\\":\\"HMA-AL00\\",\\"isBeta\\":\\"false\\",\\"grayHair\\":\\"false\\",\\"from\\":\\"nt_history\\",\\"brand\\":\\"HUAWEI\\",\\"info\\":\\"wifi\\",\\"index\\":\\"4\\",\\"rainbow\\":\\"\\",\\"schemaType\\":\\"auction\\",\\"elderHome\\":\\"false\\",\\"isEnterSrpSearch\\":\\"true\\",\\"newSearch\\":\\"false\\",\\"network\\":\\"wifi\\",\\"subtype\\":\\"\\",\\"hasPreposeFilter\\":\\"false\\",\\"prepositionVersion\\":\\"v2\\",\\"client_os\\":\\"Android\\",\\"gpsEnabled\\":\\"false\\",\\"searchDoorFrom\\":\\"srp\\",\\"debug_rerankNewOpenCard\\":\\"false\\",\\"homePageVersion\\":\\"v7\\",\\"searchElderHomeOpen\\":\\"false\\",\\"search_action\\":\\"initiative\\",\\"sugg\\":\\"_4_1\\",\\"sversion\\":\\"13.6\\",\\"style\\":\\"list\\",\\"ttid\\":\\"600000@taobao_pc_10.7.0\\",\\"needTabs\\":\\"true\\",\\"areaCode\\":\\"CN\\",\\"vm\\":\\"nw\\",\\"countryNum\\":\\"156\\",\\"m\\":\\"pc_sem\\",\\"page\\":1,\\"n\\":48,\\"q\\":\\"%E5%A5%B3%E8%A3%85\\",\\"qSource\\":\\"manual\\",\\"pageSource\\":\\"tbpc.pc_sem_alimama/a.201867-main.d6_first.418d2a89QqQAj1\\",\\"tab\\":\\"all\\",\\"pageSize\\":48,\\"totalPage\\":100,\\"totalResults\\":4800,\\"sourceS\\":\\"0\\",\\"sort\\":\\"_coefp\\",\\"bcoffset\\":\\"\\",\\"ntoffset\\":\\"\\",\\"filterTag\\":\\"\\",\\"service\\":\\"\\",\\"prop\\":\\"\\",\\"loc\\":\\"\\",\\"start_price\\":null,\\"end_price\\":null,\\"startPrice\\":null,\\"endPrice\\":null,\\"itemIds\\":null,\\"p4pIds\\":null,\\"categoryp\\":\\"\\",\\"myCNA\\":\\"HtQIIa3kbDQCAXOWQtw1UUYR\\",\\"clk1\\":\\"6b781fd1e82fdaa22a92ed45104d9534\\",\\"refpid\\":\\"mm_2898300158_3078300397_115665800437\\"}"}',
    }
    plain = cookies['_m_h5_tk'][:-14] + '&' + params['t'] + '&' + params['appKey'] + '&' + params['data']
    params['sign'] = get_md5(plain)
    print(params['sign'])
    response = requests.get(
        'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.text)
cookies = {
    'thw': 'cn',
    't': 'b25abb0107d26ae1355f8eef83104d80',
    'aui': '2218208617778',
    'cna': 'HtQIIa3kbDQCAXOWQtw1UUYR',
    'cookie2': '1f18fee858bf51f0344adc91dc29bc58',
    '_tb_token_': '7eb34e38307e1',
    'xlly_s': '1',
    '3PcFlag': '1782654488002',
    'wk_cookie2': '1672216e80a0c8d0610b79ee5836c630',
    'wk_unb': 'UUpgTsupqYQ6cIsHpA%3D%3D',
    'sgcookie': 'E100Ue%2BNSEPmoY2IkhTidraBjsbjw7xLMQ%2Bwek%2Buzc0I%2FojZilDdBEI%2Fhk3asGlCgOxFoAO1fog5WoEQKIJU878Z7KZ652rxeCPTUfESYlTjASr%2FPlhH%2BGEOrYeVMg9gchBZ',
    'unb': '2218208617778',
    'csg': 'ee1a869a',
    'lgc': 'tb530666708967',
    'cancelledSubSites': 'empty',
    'cookie17': 'UUpgTsupqYQ6cIsHpA%3D%3D',
    'dnk': 'tb530666708967',
    'skt': 'feb78f2802c7e6f5',
    'tracknick': 'tb530666708967',
    '_l_g_': 'Ug%3D%3D',
    'sg': '782',
    '_nk_': 'tb530666708967',
    'cookie1': 'VynKMYML67jWxeDOL%2FwcMcPuD2tzEuTm%2B0BexFnEIdE%3D',
    'uc1': 'cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&pas=0&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie14=UoYWPyKFhCXQrg%3D%3D',
    'sn': '',
    'uc3': 'nk2=F5RAQUl3%2BS3alYH5CHA%3D&id2=UUpgTsupqYQ6cIsHpA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dD1NV%2FcP%2FdcsOfrO4%3D',
    'existShop': 'MTc4MjY1NDUwOA%3D%3D',
    'uc4': 'nk4=0%40FY4L7Qb0Y0TwyVu%2BrmPvMafLcE3URRDUog%3D%3D&id4=0%40U2gqwYJcJkvExOjYqMoSvr2J5KVY71vx',
    '_cc_': 'WqG3DMC9EA%3D%3D',
    '_hvn_lgc_': '0',
    'havana_lgc2_0': 'eyJoaWQiOjIyMTgyMDg2MTc3NzgsInNnIjoiNTY5MDE3MWI3YjFkOWVkNGU2ZTVjZWMyZmViMjRmYzAiLCJzaXRlIjowLCJ0b2tlbiI6IjFEM3BldkJlYzVLTm5ZMjVPWEdIc3ZRIn0',
    '_samesite_flag_': 'true',
    'ultraCookieBase': '1k6S5%2BcxkgQpZVJ5N08GM2MXJWGTU13jDoIgVX0c0A6r2K21VhQI%2F5BZf3T8c%2Be6qtm4K1UBzkKOqAnbefND4cab9aXjOnyTe9XtcR1uuQMPB8U7riKpErBxfbzSV8YHhTFClEE1L3RHKz1WPd8mIS0Xf5jXESqB3Riy9cwSbb3Jq35%2FXuYotzxr8jbBWjiLeXGP0Lie98KysLUbY1drT%2FlRU5y9OQRTA%2FGlxTIHhghc64X6p0ZLNeXn4%2F1JK7ifYoI2ApMinA20RYg2G2ARHbIXF4U1s1YS8t%2BDofTgkcg4Y%2BYvbOKrSUjL%2F%2FaFQmadu%2B8Neo5IrzLbHlKs%3D',
    'havana_lgc_exp': '1813760296654',
    'sdkSilent': '1782685096653',
    'havana_sdkSilent': '1782685096653',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': 'a98ccac321ae1bd3c16da2b892f0cbfb_1782669984538',
    '_m_h5_tk_enc': '2ac6c3e22ea3d3f62908074ac018ed7a',
    'tfstk': 'hhdxNaq4DuFo113o2FCe4O1GM4mnkCb15F8a5i1foVC92H6_sx5cB1K5qIjDoss_63jzsVSmu1B6fngoxX2nqOghTlwfflf5VNzmdg9ZtE84PrEs-L9GaQtCJRN6ftsWPNs5lG6_G4B5-N1_GONbFusP51s6fiNSNZ7bloNfh_gR7gs111t6P4QGVG111hT5y6Xjue4-azHKj6yqTgF_9y7x0McFVIA2wZLRAEwQ1mUr_tSO4BioeUSJhnbyXXnR_3J6fNK7VcX25LKRknjUIC07CRkfzk9sZg2ICJsCyM0uERyNEa7Rx438QRWfzaInrb2aQTbP.',
    'isg': 'BFlZfV8RV4maGAjsEZdw1CXqaEUz5k2Y7qxCjHsO1QD_gnkUwzZdaMcUgEb0OuXQ',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://uland.taobao.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://uland.taobao.com/',
    'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    # 'cookie': 'thw=cn; t=b25abb0107d26ae1355f8eef83104d80; aui=2218208617778; cna=HtQIIa3kbDQCAXOWQtw1UUYR; cookie2=1f18fee858bf51f0344adc91dc29bc58; _tb_token_=7eb34e38307e1; xlly_s=1; 3PcFlag=1782654488002; wk_cookie2=1672216e80a0c8d0610b79ee5836c630; wk_unb=UUpgTsupqYQ6cIsHpA%3D%3D; sgcookie=E100Ue%2BNSEPmoY2IkhTidraBjsbjw7xLMQ%2Bwek%2Buzc0I%2FojZilDdBEI%2Fhk3asGlCgOxFoAO1fog5WoEQKIJU878Z7KZ652rxeCPTUfESYlTjASr%2FPlhH%2BGEOrYeVMg9gchBZ; unb=2218208617778; csg=ee1a869a; lgc=tb530666708967; cancelledSubSites=empty; cookie17=UUpgTsupqYQ6cIsHpA%3D%3D; dnk=tb530666708967; skt=feb78f2802c7e6f5; tracknick=tb530666708967; _l_g_=Ug%3D%3D; sg=782; _nk_=tb530666708967; cookie1=VynKMYML67jWxeDOL%2FwcMcPuD2tzEuTm%2B0BexFnEIdE%3D; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&pas=0&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie14=UoYWPyKFhCXQrg%3D%3D; sn=; uc3=nk2=F5RAQUl3%2BS3alYH5CHA%3D&id2=UUpgTsupqYQ6cIsHpA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dD1NV%2FcP%2FdcsOfrO4%3D; existShop=MTc4MjY1NDUwOA%3D%3D; uc4=nk4=0%40FY4L7Qb0Y0TwyVu%2BrmPvMafLcE3URRDUog%3D%3D&id4=0%40U2gqwYJcJkvExOjYqMoSvr2J5KVY71vx; _cc_=WqG3DMC9EA%3D%3D; _hvn_lgc_=0; havana_lgc2_0=eyJoaWQiOjIyMTgyMDg2MTc3NzgsInNnIjoiNTY5MDE3MWI3YjFkOWVkNGU2ZTVjZWMyZmViMjRmYzAiLCJzaXRlIjowLCJ0b2tlbiI6IjFEM3BldkJlYzVLTm5ZMjVPWEdIc3ZRIn0; _samesite_flag_=true; ultraCookieBase=1k6S5%2BcxkgQpZVJ5N08GM2MXJWGTU13jDoIgVX0c0A6r2K21VhQI%2F5BZf3T8c%2Be6qtm4K1UBzkKOqAnbefND4cab9aXjOnyTe9XtcR1uuQMPB8U7riKpErBxfbzSV8YHhTFClEE1L3RHKz1WPd8mIS0Xf5jXESqB3Riy9cwSbb3Jq35%2FXuYotzxr8jbBWjiLeXGP0Lie98KysLUbY1drT%2FlRU5y9OQRTA%2FGlxTIHhghc64X6p0ZLNeXn4%2F1JK7ifYoI2ApMinA20RYg2G2ARHbIXF4U1s1YS8t%2BDofTgkcg4Y%2BYvbOKrSUjL%2F%2FaFQmadu%2B8Neo5IrzLbHlKs%3D; havana_lgc_exp=1813760296654; sdkSilent=1782685096653; havana_sdkSilent=1782685096653; mtop_partitioned_detect=1; _m_h5_tk=a98ccac321ae1bd3c16da2b892f0cbfb_1782669984538; _m_h5_tk_enc=2ac6c3e22ea3d3f62908074ac018ed7a; tfstk=hhdxNaq4DuFo113o2FCe4O1GM4mnkCb15F8a5i1foVC92H6_sx5cB1K5qIjDoss_63jzsVSmu1B6fngoxX2nqOghTlwfflf5VNzmdg9ZtE84PrEs-L9GaQtCJRN6ftsWPNs5lG6_G4B5-N1_GONbFusP51s6fiNSNZ7bloNfh_gR7gs111t6P4QGVG111hT5y6Xjue4-azHKj6yqTgF_9y7x0McFVIA2wZLRAEwQ1mUr_tSO4BioeUSJhnbyXXnR_3J6fNK7VcX25LKRknjUIC07CRkfzk9sZg2ICJsCyM0uERyNEa7Rx438QRWfzaInrb2aQTbP.; isg=BFlZfV8RV4maGAjsEZdw1CXqaEUz5k2Y7qxCjHsO1QD_gnkUwzZdaMcUgEb0OuXQ',
}

params = {
    'jsv': '2.7.2',
    'appKey': '12574478',
    't': '1782660498584',
    'sign': 'd4b23c5ffa7377d9a5266d51ae5d62db',
    'jsonpIncPrefix': 'tbnavnew',
    'api': 'mtop.alibaba.fc.api.maoxland.containerfacade.singleview',
    'v': '1.0',
    'type': 'originaljson',
    'dataType': 'json',
    'timeout': '5000',
    'data': '{"projectName":"PcTaobao","responseCode":"PcTranslateConfig","params":{"operationType":"read","cna":"HtQIIa3kbDQCAXOWQtw1UUYR"}}',
}
plain = cookies['_m_h5_tk'][:-14] + '&' + params['t'] + '&' + params['appKey'] + '&' + params['data']
params['sign'] = get_md5(plain)
print(params['sign'])
response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.alibaba.fc.api.maoxland.containerfacade.singleview/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)