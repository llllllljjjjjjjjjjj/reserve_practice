import requests
from lxml import etree
import csv
import os
import time
from typing import Union, List, Dict
import random
# ===================== 基础配置 =====================
SAVE_FOLDER = "fang_rent_data"
URL_TEMPLATE = "https://zu.fang.com/house-a01/i3{}.htm"
FIRST_PAGE_URL = "https://zu.fang.com/house-a01/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# ===================== os 拼接绝对路径 =====================
current_script_dir = os.path.dirname(os.path.abspath(__file__))
save_abs_dir = os.path.join(current_script_dir, SAVE_FOLDER)
os.makedirs(save_abs_dir, exist_ok=True)


# ===================== 核心接口1：页数接口 =====================
def crawl_page(page_num: int) -> List[Dict]:
    """
    爬取指定页码的所有房源数据
    :param page_num: 页码，从1开始
    :return: 该页所有房源的字典列表，爬取失败返回空列表
    """
    if page_num == 1:
        target_url = FIRST_PAGE_URL
    else:
        target_url = URL_TEMPLATE.format(page_num)

    try:
        response = requests.get(target_url, headers=HEADERS, timeout=10)
        response.encoding = response.apparent_encoding
        html_text = response.text
    except Exception as e:
        print(f"❌ 第 {page_num} 页请求失败：{str(e)}")
        return []

    html = etree.HTML(html_text)
    house_nodes = html.xpath("//dl[contains(@class, 'list') and contains(@class, 'hiddenMap')]")

    result = []
    for idx, item in enumerate(house_nodes, start=1):
        title = item.xpath("./dd/p[@class='title']/a/text()")
        title = title[0].strip() if title else ""

        detail_url = item.xpath("./dd/p[@class='title']/a/@href")
        detail_url = "https:" + detail_url[0] if detail_url else ""

        base_info = item.xpath("normalize-space(./dd/p[contains(@class, 'font15')])")

        area_list = item.xpath("./dd/p[contains(@class, 'gray6') and contains(@class, 'mt12')]/a/span/text()")
        district = area_list[0] if len(area_list) >= 1 else ""
        block = area_list[1] if len(area_list) >= 2 else ""
        community = area_list[2] if len(area_list) >= 3 else ""

        subway = item.xpath("./dd//span[contains(@class, 'note')]/text()")
        subway = subway[0].strip() if subway else ""

        price = item.xpath("./dd//span[@class='price']/text()")
        price = price[0] if price else ""

        img_url = item.xpath("./dt//img/@data-original")
        img_url = "https:" + img_url[0] if img_url else ""

        house_dict = {
            "页内序号": idx,
            "房源标题": title,
            "详情链接": detail_url,
            "基础信息": base_info,
            "行政区": district,
            "所在板块": block,
            "小区名称": community,
            "地铁信息": subway,
            "月租金": f"{price}元/月",
            "封面图链接": img_url
        }
        result.append(house_dict)

    print(f"✅ 第 {page_num} 页爬取完成，共获取 {len(result)} 条房源")
    return result


# ===================== 核心接口2：单条数据接口 =====================
def get_single_house(page_num: int, index: int) -> Union[Dict, None]:
    """
    获取指定页、指定序号的单条房源数据
    :param page_num: 页码
    :param index: 页内第几条，从1开始
    :return: 房源字典，不存在则返回None
    """
    page_data = crawl_page(page_num)
    if not page_data or index < 1 or index > len(page_data):
        print(f"❌ 第 {page_num} 页第 {index} 条数据不存在")
        return None
    return page_data[index - 1]


# ===================== CSV保存函数 =====================
def save_page_to_csv(page_data: List[Dict], page_num: int) -> str:
    """
    将单页数据保存为CSV文件，文件名为 {页数}.csv
    :param page_data: 房源数据列表
    :param page_num: 页码，作为文件名
    :return: 保存的CSV文件绝对路径
    """
    if not page_data:
        print(f"⚠️  第 {page_num} 页无数据，跳过保存")
        return ""

    csv_filename = f"{page_num}.csv"
    csv_abs_path = os.path.join(save_abs_dir, csv_filename)

    with open(csv_abs_path, "w", newline="", encoding="utf-8-sig") as f:
        field_names = list(page_data[0].keys())
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(page_data)

    print(f"💾 第 {page_num} 页已保存到：{csv_abs_path}")
    return csv_abs_path


# ===================== 使用示例 =====================
if __name__ == "__main__":
    # 爬取第1页并保存为 1.csv
    for i in range(1, 38):
        page_data = crawl_page(i)
        save_page_to_csv(page_data, i)
        time.sleep(3 + (random.random()-0.5) * 2 )