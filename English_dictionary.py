import os #是Python标准库中的一个模块，提供了与操作系统交互的函数。它允许Python程序与操作系统进行各种交互，包括文件和目录操作、进程管理等。
def load_dictionary(file_path):
    dictionary = {} #创建空字典
    if os.path.exists(file_path): #检查文件是否存在
        with open(file_path, 'r', encoding='utf-8') as file: #打开文件，以读方式打开，并指定编码为utf-8
            for line in file: #遍历文件每一行
                word, translation = line.strip().split(' ') #以空格分割行，得到单词和翻译。 去除字符串 line 开头和结尾的空白字符，包括空格、制表符、换行符等。将分割后的字符串列表按顺序赋值
                dictionary[word] = translation
    return dictionary
def save_dictionary(file_path, dictionary):
    with open(file_path, 'w', encoding='utf-8') as file: #打开文件，以写方式打开，并指定编码为utf-8
        for word, translation in dictionary.items(): #遍历字典中的每一对键值对
            file.write(f"{word} {translation}\n")
def add_word(dictionary):
    word = input("请输入要添加的英文单词: ")
    if word in dictionary:
        print("该单词已添加到词典中")
    else:
        translation = input("请输入该单词的中文释义: ")
        dictionary[word] = translation
        print("单词添加成功")

def search_word(dictionary):
    word = input("请输入要查询的英文单词: ")
    translation = dictionary.get(word, "字典中未找到该单词")
    print(translation)

# 程序主体
file_path = '/Users/wangqi/Desktop/dictionary.txt'
dictionary = load_dictionary(file_path)

while True:
    print("1. 添加单词")
    print("2. 查询单词")
    print("3. 退出")
    choice = input("请选择操作: ")
    if choice == "1":
        add_word(dictionary)
    elif choice == "2":
        search_word(dictionary)
    elif choice == "3":
        save_dictionary(file_path, dictionary)
        print("词典已保存，程序退出")
        break
    else:
        print("输入有误")


