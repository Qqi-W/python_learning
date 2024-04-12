# 编马函数multi0，参数个数不限，返回所有参数的乘积。 
def multi0(*args):
    numbers = [int(x) for x in args] #将参数转换为整数列表
    result = 1
    for num in numbers: 
        result *= num
    return result

parameters=input("enter the parameters:")
parameters=parameters.split() #将输入的字符串以空格分割为列表
result=multi0(*parameters) #将列表作为参数传入multi0函数
print(result)    #输出结果