import sys
sys.path.append('/Users/wangqi/anaconda3/lib/python3.11/site-packages')

import jieba
import re
from collections import Counter

# 读取文本数据
def get_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 分词并进行词频统计
def get_top_keywords(text, top_n):
    # 使用jieba分词
    words = jieba.lcut(text)
    # 使用正则表达式去除特殊符号和停用词
    words = [word for word in words if re.match(r'^[\u4e00-\u9fa5]+$', word)]
    # 进行词频统计
    word_count = Counter(words)
    # 找出出现频率最高的前top_n个关键词
    top_keywords = word_count.most_common(top_n)
    return top_keywords

filename = '/Users/wangqi/Desktop/2024年政府工作报告.txt'  # 替换为实际文件路径
text = get_text(filename)
top_keywords = get_top_keywords(text, 10)
print(top_keywords)
