import requests
from lxml import etree
cookies = {
    'global_cookie': 'ycmr4w6afb8ax8pclgxme2szq22mq55re66',
    'sfut': 'FE9EB76D778376EEBFCCE1ABB59F9E499A3FA0E7FF9956E4E3030FFC68BAD6BDEA60ACC83BC06443D288979A37727619B3BECE11A8FD027DBFDD054642007970A31145413E9C0FA118CF2A7D2577F377DB647F994DE2B3ADE34ED6E6E9E63B20B3C61FA170670748',
    'otherid': '552721886f046bcf03dc5212b62e4167',
    '__utma': '147393320.2049000955.1780919960.1782017865.1782445663.21',
    '__utmz': '147393320.1782445663.21.5.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmt_t0': '1',
    '__utmt_t1': '1',
    '__utmt_t2': '1',
    'token': '9b075412a0b8466eb14877eef8a33c14',
    '__utmc': '147393320',
    '__utmb': '147393320.9.10.1782445663',
    'city': 'bj',
    'csrfToken': 'LKdCd_Xi_ArjO6AImgAL7owU',
    'g_sourcepage': 'zf_fy%5Elb_pc',
    'new_loginid': '133368365',
    'login_username': 'fang35762065688',
    'unique_cookie': 'U_6i955nvvrkw5rrrco67qlkcem2fmque84f6*7',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://zu.fang.com/hezu/',
    'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    # 'cookie': 'global_cookie=ycmr4w6afb8ax8pclgxme2szq22mq55re66; sfut=FE9EB76D778376EEBFCCE1ABB59F9E499A3FA0E7FF9956E4E3030FFC68BAD6BDEA60ACC83BC06443D288979A37727619B3BECE11A8FD027DBFDD054642007970A31145413E9C0FA118CF2A7D2577F377DB647F994DE2B3ADE34ED6E6E9E63B20B3C61FA170670748; otherid=552721886f046bcf03dc5212b62e4167; __utma=147393320.2049000955.1780919960.1782017865.1782445663.21; __utmz=147393320.1782445663.21.5.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; token=9b075412a0b8466eb14877eef8a33c14; __utmc=147393320; __utmb=147393320.9.10.1782445663; city=bj; csrfToken=LKdCd_Xi_ArjO6AImgAL7owU; g_sourcepage=zf_fy%5Elb_pc; new_loginid=133368365; login_username=fang35762065688; unique_cookie=U_6i955nvvrkw5rrrco67qlkcem2fmque84f6*7',
}

def get_save(i):
    response = requests.get(f'https://zu.fang.com/hezu/i3{i}/', cookies=cookies, headers=headers)

    html = etree.HTML(response.text)
    house_list = html.xpath('//div[@class="houseList"]/dl')
    for item in house_list:
        print('\n\n')
        # --- 提取房源标题 ---
        # xpath()永远返回列表，匹配不到就是空列表，加判断避免索引报错
        title = item.xpath("./dd/p[@class='title']/a/text()")
        title = title[0].strip() if title else ''
        
        # --- 提取详情页链接 ---
        detail_url = item.xpath("./dd/p[@class='title']/a/@href")
        detail_url = detail_url[0] if detail_url else ''
        
        # --- 提取基础信息（合租类型+面积+朝向） ---
        # normalize-space()是XPath内置函数，自动去除多余空格和换行，直接返回字符串
        base_info = item.xpath("normalize-space(./dd/p[contains(@class, 'font15')])")
        
        # --- 提取行政区、板块、小区名称 ---
        district = item.xpath("./dd/p[contains(@class, 'gray6') and contains(@class, 'mt12')]/a[1]/span/text()")
        district = district[0] if district else ''
        
        block = item.xpath("./dd/p[contains(@class, 'gray6') and contains(@class, 'mt12')]/a[2]/span/text()")
        block = block[0] if block else ''
        
        community = item.xpath("./dd/p[contains(@class, 'gray6') and contains(@class, 'mt12')]/a[3]/span/text()")
        community = community[0] if community else ''
        
        # --- 提取地铁交通信息 ---
        subway = item.xpath("./dd//span[contains(@class, 'note')]/text()")
        subway = subway[0].strip() if subway else ''
        
        # --- 提取月租金 ---
        price = item.xpath("./dd//span[@class='price']/text()")
        price = price[0] if price else ''
        
        # --- 提取封面图真实地址（懒加载存在data-original里） ---
        img_url = item.xpath("./dt//img/@data-original")
        img_url = img_url[0] if img_url else ''

        # 把单条数据整理成字典，加入结果列表
        house_info = {
            '房源标题': title,
            '详情链接': detail_url,
            '基础信息': base_info,
            '行政区': district,
            '所在板块': block,
            '小区名称': community,
            '地铁信息': subway,
            '月租金': f'{price}元/月',
            '封面图': img_url
        }
        print(house_info)