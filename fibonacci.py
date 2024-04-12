def fibonacci(n):
    if n <= 0:
        return "输入错误，请输入一个正整数"
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 示例用法
number = input("请输入一个正整数：")
result = fibonacci(int(number))
print(result)
