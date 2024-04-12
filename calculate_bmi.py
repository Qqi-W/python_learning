#计算BMI指数并获取BMI分类
def calculate_bmi(weight, height):
    # 计算BMI函数，根据体重和身高计算BMI指数，并返回结果
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category_in(bmi):
    # 获取BMI分类函数，根据BMI值返回对应的指标分类信息
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"
    
def get_bmi_category_out(bmi):
    # 获取BMI分类函数，根据BMI值返回对应的指标分类信息
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 25:
        return "正常"
    elif bmi < 30:
        return "偏胖"
    else:
        return "肥胖"

# 输入身高和体重值
height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（公斤）："))

# 计算BMI值
bmi = calculate_bmi(weight, height)

# 输出BMI值
print("您的BMI值为：", bmi)

# 获取国际BMI指标建议值
bmi_category = get_bmi_category_out(bmi)
print("国际BMI指标建议值：", bmi_category)

# 获取国内BMI指标建议值
bmi_category = get_bmi_category_in(bmi)
print("国内BMI指标建议值：", bmi_category)