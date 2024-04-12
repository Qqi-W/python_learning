'''
编写程序，判断用户输入的8位信用卡号是否合法，信用卡号是否合法的判断规则如下：
(1)对给定的8位信用卡号码，如43589795，从最右边数字开始，隔一位取一个数相加，如5+7+8+3=23.
(2)将信用卡号中未出现在第一步中的每个数字乘2，然后将相乘的结果的每位数字相加。
例如，上述例子中从右至左为18、18、10、8，将所有数字相加为1+8+1+8+1+0+8=27.
(3)将上述两步得到的值相加，如果结果的个位为0，则输入的信用卡号是有效的。
要求;用户输入的8位卡号必须一次性输入。
'''
def validate_credit_card(card_number):
    # 验证信用卡号的有效性
    if len(card_number) != 8 or not card_number.isdigit():
        return "Invalid credit card number input"

    # 计算步骤1的和
    step1_sum = sum(int(card_number[i]) for i in range(7, -1, -2))
    # 计算步骤2的数字
    step2_digits =  [int(digit) for digit in ''.join(str(int(card_number[i]) * 2) for i in range(6, -1, -2))]
    # 计算步骤2的和
    step2_sum = sum(step2_digits)
    # 计算总和
    total_sum = step1_sum + step2_sum

    # 检查总和是否能被10整除
    if total_sum % 10 == 0:
        return "Valid credit card number"
    else:
        return "Invalid credit card number"

# 用户输入信用卡号并进行验证
card_number = input("请输入8位信用卡号码：")
print(validate_credit_card(card_number))