#编写程序实现：输入一个正整数，将其写成其所有因数的积。

def factor_product(num):
    factors = [] # 存储因数
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor) # 将因数添加到列表中
            num = num / divisor
        divisor += 1
    return factors

num = int(input("please input number:"))
result = factor_product(num)
print(f"{num} ={' × '.join(map(str, result))}")
