#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#requets是一个爬虫的第三方库，需要单独安装
import requests
import csv

# 以'w'模式打开文件，如果文件不存在将会创建一个新文件

f = open('评论2.csv',mode='a',encoding='utf-8-sig',newline='')
csv_write = csv.writer(f)
csv_write.writerow(['id', 'text_raw', 'source'])  # 写入表头

call_count = 0  # 函数调用次数计数器


# 请求头 用文字的方式输出网页数据----->定义请求头
headers = {
    # 用户身份信息
    'cookie' : 'XSRF-TOKEN=MJqiTewfsP47Nsf8FJXW_6Fg; SUB=_2A25LVsZqDeRhGeFJ7VcV-SbOyz-IHXVoKkeirDV8PUNbmtANLVCgkW9Nf3auDBLlwU666f0_J6TFCD2Sm71anC9l; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5JD-215qyX3i9kdChjFpmA5NHD95QNS0qfSh.Reo50Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0McSKB41hz7e7tt; ALF=02_1719288634; WBPSESS=VC13eXCDS6sgLONS22hQp4KyVsA1EF_0awdnEjPaVPu0vOtVn-NLI_YfHYl55zd-mNZ-HBZ0CvEdnXNP6yKADizZ3g1gVP1ap9eXwIcdxtsgW2bh9Oi4HERBlspc_DSTqCNeVJ0a6BnOuG03_P6RBA==',
    # 防盗链
    'referer' : 'https://weibo.com/2656274875/OfLyjD5c2',
    # 浏览器基本信息
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

def get_next( next = 'count=10'):
    global call_count  # 使用global关键字声明call_count是全局变量
    call_count += 1  # 每次函数调用增加计数器
    if call_count==16: #选定最大爬取页面
        return
    
    #url是一访问网站的地址
    url = f'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=5037577159314758&is_show_bulletin=2&is_mix=0&{next}&uid=2656274875&fetch_level=0&locale=zh-CN'
     

    response = requests.get(url=url,headers=headers)

    json_data = response.json()
    
    if json_data['data']:
        data_list = json_data['data']
    else:
        print("请求失败")
        return
    
    max_id = json_data['max_id']
    
    for data in data_list:
        text_raw = data['text_raw']
        id = data['id']
        if 'source' in data:
            source=data['source']
        else:
            source=0   
        #print(id,text_raw,source)
        csv_write.writerow([id,text_raw,source])
    max_str = 'max_id='+str(max_id)
    get_next(max_str)
 
 
get_next()
f.close()
print("函数 get_next 被调用了", call_count, "次")
###############################################################################
#画图
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
# import matplotlib


# 读取CSV文件
df = pd.read_csv('评论2.csv', encoding='utf-8')

# 分析text_raw列中频率高的2字词语

content = ' '.join(df['text_raw'])  # 将text_raw列的文本合并为一个字符串
# 使用正则表达式匹配2个连续的中文字符或英文字符
words = re.findall(r'[\u4e00-\u9fa5]{2}|[a-zA-Z]{2}', content)
top_words = dict(Counter(words).most_common(10))  # 使用Counter统计单词频率，取出现频率最高的前10个单词

# 绘制频率高的2字词语柱状图
plt.bar(top_words.keys(), top_words.values())  # 绘制柱状图，x轴为单词，y轴为频率
plt.xlabel('2 Letter Words')  # 设置x轴标签
plt.ylabel('Frequency')  # 设置y轴标签
plt.xticks(range(len(top_words.keys())), top_words.keys(), fontproperties='Heiti TC')  # 使用中文标签，并指定字体为宋体
plt.title('Top 2 Letter Words')  # 设置图表标题
plt.show()  # 显示图表

# 绘制source列中不同地区的分类图
source_counts = df['source'].value_counts()  # 统计source列中不同值的数量
i=-1
source_name=[]
source_number=[]
for index in source_counts.index:
    
    if index != "0":
        source_name.append(str(index[2:]))
        source_number.append(int(source_counts.values[i]))
        i=1+i #记录索引
    else:
        i=1+i #记录索引
        
sorted_source=sorted(list(zip(source_number,source_name)),reverse=True)
sorted_number,sorted_name=zip(*sorted_source)
sorted_number=list(sorted_number)
sorted_name=list(sorted_name)
normalized_number = [x / max(sorted_number) for x in sorted_number]

plt.figure(dpi=500)  # 设置图的分辨率
plt.bar(sorted_name, normalized_number)  # 绘制柱状图，x轴为地区，y轴为数量
plt.xlabel('Source')  # 设置x轴标签
plt.ylabel('frequency')  # 设置y轴标签
plt.title('Source Distribution')  # 设置图表标题
plt.xticks(range(len(source_name)), sorted_name, fontproperties='Heiti TC',rotation=45,fontsize=6.5)  # 旋转x轴标签，使其更易阅读
plt.show()  # 显示图表



