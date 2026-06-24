import re
import requests
import pandas as pd
import mplfinance as mpf
import matplotlib as mpl

# 解决中文显示问题
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

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

# 提取 JSON 数组
match = re.search(r'\((\[.*\])\)', response.text, re.DOTALL)
if not match:
    raise ValueError('无法从 response.text 中提取数据')

raw_list = eval(match.group(1))

# 构建 DataFrame
df = pd.DataFrame(raw_list)
df = df.rename(columns={
    'd': 'Date',
    'o': 'Open',
    'h': 'High',
    'l': 'Low',
    'c': 'Close',
    'v': 'Volume',
})
df['Date'] = pd.to_datetime(df['Date'])
df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Volume']].astype(float)
df.set_index('Date', inplace=True)

print(f'共获取 {len(df)} 条K线数据，日期范围：{df.index[0].date()} ~ {df.index[-1].date()}')

# 只取最近 120 条用于展示，避免数据过多拥挤
plot_df = df.tail(120)

fig, axes = mpf.plot(
    plot_df,
    type='candle',
    style='charles',
    title='TA0 期货日K线',
    ylabel='价格',
    ylabel_lower='成交量',
    volume=True,
    mav=(5, 10, 20),
    figratio=(16, 9),
    figscale=1.2,
    returnfig=True,
)

# 强制将所有文字字体改为中文字体
for text in fig.findobj(mpl.text.Text):
    text.set_fontfamily('Microsoft YaHei')

fig.savefig('kline.png', dpi=150, bbox_inches='tight')
print('K线图已保存为 kline.png')
