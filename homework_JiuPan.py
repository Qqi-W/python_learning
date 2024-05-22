import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# 发送 HTTP 请求获取网页内容
url = 'https://example.com/photovoltaic-development-data'
response = requests.get(url)

# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取数据并存入适当的数据结构 (例如 DataFrame)
data = []
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        data.append({
            'year': cells[0].text,
            'installed_capacity': cells[1].text
            # Add more data fields as needed
        })

df = pd.DataFrame(data)

# 对数据进行分析
# 例如，计算每年光伏装机容量的平均值
average_capacity = df['installed_capacity'].mean()

# 数据可视化
# 例如，绘制光伏装机容量随时间的变化
plt.plot(df['year'], df['installed_capacity'])
plt.xlabel('Year')
plt.ylabel('Installed Capacity')
plt.title('Photovoltaic Development')
plt.show()
