import sqlite3
import requests
from lxml import etree 

conn = sqlite3.connect('安居客.db')  # 2. 连接数据库（没有会自动创建）
cursor = conn.cursor()              # 拿到操作光标

# 建表（没有会自动创建，有了会跳过）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS 租房 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        介绍 TEXT,
        是否安选 TEXT,
        情况1 TEXT,
        位置 TEXT,
        情况2 TEXT
    )
''')
conn.commit()

cookies = {
    'aQQ_ajkguid': 'B858C22F-AB49-41F5-ADA5-1E989A5A9D0E',
    'sessid': '3D7C7700-C165-4E47-9F3F-378E27C3F669',
    'ajk-appVersion': '',
    'ctid': '674',
    'id58': 'CkwAUmozbo0nDsHuBHr2Ag==',
    'xxzlclientid': '2b26d280-14f8-4dbf-9623-1781755535083',
    'xxzlxxid': 'pfmxoglX2XFB1Z20BngUSI3LiIDqFAIn6DMGYKw5F+ZQoVhp38e2Qht5MlxWd2z8Gok4',
    'obtain_by': '2',
    'twe': '2',
    'fzq_h': 'abb8230c5705a17733a910e5d4eb72a5_1782558269522_8a45c1169a3a495b998b0c860cf53584_1867104836',
    'lps': 'https%3A%2F%2Fjinx.zu.anjuke.com%2F%3Ffrom%3DHomePage_TopBar%7Chttps%3A%2F%2Fjinxian.anjuke.com%2F',
    'cmctid': '677',
    'wmda_uuid': '3afe6cfcd7531ab22a21617e7566912e',
    'wmda_new_uuid': '1',
    'wmda_session_id_6289197098934': '1782558283913-844b45e4-3bc7-04f1',
    'wmda_visited_projects': '%3B6289197098934',
    'xxzlbbid': 'pfmbRMs7zLvw5uW+OqJPgdnR86WIYYVUxhMaS9LTNnJzFQbUMqO6+/VIoW014DSLmqiRD8LathTphpDT11jn7ezoQ/jkwjgz/dmpDi/9vR6sdZbPNbP9dYTu/Tgumccm8HT2EGNU2XgxNzgyNTU4Njk5OTUxNDUz_1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Microsoft Edge";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
    # 'cookie': 'aQQ_ajkguid=B858C22F-AB49-41F5-ADA5-1E989A5A9D0E; sessid=3D7C7700-C165-4E47-9F3F-378E27C3F669; ajk-appVersion=; ctid=674; id58=CkwAUmozbo0nDsHuBHr2Ag==; xxzlclientid=2b26d280-14f8-4dbf-9623-1781755535083; xxzlxxid=pfmxoglX2XFB1Z20BngUSI3LiIDqFAIn6DMGYKw5F+ZQoVhp38e2Qht5MlxWd2z8Gok4; obtain_by=2; twe=2; fzq_h=abb8230c5705a17733a910e5d4eb72a5_1782558269522_8a45c1169a3a495b998b0c860cf53584_1867104836; lps=https%3A%2F%2Fjinx.zu.anjuke.com%2F%3Ffrom%3DHomePage_TopBar%7Chttps%3A%2F%2Fjinxian.anjuke.com%2F; cmctid=677; wmda_uuid=3afe6cfcd7531ab22a21617e7566912e; wmda_new_uuid=1; wmda_session_id_6289197098934=1782558283913-844b45e4-3bc7-04f1; wmda_visited_projects=%3B6289197098934; xxzlbbid=pfmbRMs7zLvw5uW+OqJPgdnR86WIYYVUxhMaS9LTNnJzFQbUMqO6+/VIoW014DSLmqiRD8LathTphpDT11jn7ezoQ/jkwjgz/dmpDi/9vR6sdZbPNbP9dYTu/Tgumccm8HT2EGNU2XgxNzgyNTU4Njk5OTUxNDUz_1',
}

params = {
    'from': 'HomePage_TopBar',
}

response = requests.get('https://jinx.zu.anjuke.com/', params=params, cookies=cookies, headers=headers)
#print(response.text)
#介绍、格局、大小、楼层、位置、周围道路、细节
html = etree.HTML(response.text)
house_list = html.xpath('//div[@class="zu-itemmod clearfix"]/div[@class="zu-info"]')
print(len(house_list))
for i in house_list:
    summary1 = i.xpath('./h3/a/b/text()')[0]
    #print(summary1)
    try:
        summary2 = i.xpath('./h3/em/text()')[0]
    except:
        summary2 = "没安选"
    format = ''.join(i.xpath('./p[@class="details-item tag"]//text()')).replace(" ", '').replace('\n', '')
    address = ''.join(i.xpath('./address[@class="details-item tag"]//text()')).replace(' ', '').replace('\n', '').replace('\xa0', '')
    aaaa = ''.join(i.xpath('./p[@class="details-item bot-tag"]//text()')).replace('\n', '').replace(' ', '')
    lll = {
        '介绍':summary1, 
        '是否安选':summary2, 
        '情况1':format,
        '位置': address,
        '情况2':aaaa
    }
    print(lll)
     # ========== 新增：插入数据库 ==========
    cursor.execute('''
        INSERT INTO 租房 (介绍, 是否安选, 情况1, 位置, 情况2)
        VALUES (?, ?, ?, ?, ?)
    ''', (summary1, summary2, format, address, aaaa))
    
    lll = {
        '介绍': summary1, 
        '是否安选': summary2, 
        '情况1': format,
        '位置': address,
        '情况2': aaaa
    }
    print(lll)

# ========== 新增：全部爬完后一次性保存 ==========
conn.commit()
conn.close()
print("数据已保存到 安居客.db")
    