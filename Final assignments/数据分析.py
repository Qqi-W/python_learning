#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:28:44 2024

@author: wangqi
"""

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