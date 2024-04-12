def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if num == 0:
        return "zero"
    elif num < 10:
        return units[num]
    elif num < 20:
        return teens[num - 11]
    elif num < 100:
        return tens[num // 10] + (" " + units[num % 10] if num % 10 != 0 else "")
    elif num < 1000:
        return units[num // 100] + " hundred" + (" and " + number_to_words(num % 100) if num % 100 != 0 else "")

# 获取用户输入的数字
input_number = int(input("请输入一个1~999的整数："))

# 将数字转换为英文表示
result = number_to_words(input_number)
print(result)
