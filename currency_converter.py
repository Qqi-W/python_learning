# 定义美元兑换成人民币的函数
def usd_to_rmb(usd_amount):
    rmb_amount = usd_amount * 7  # 根据汇率1美元=7人民币进行计算
    return rmb_amount

# 定义人民币兑换成美元的函数
def rmb_to_usd(rmb_amount):
    usd_amount = rmb_amount / 7  # 根据汇率1美元=7人民币进行计算
    return usd_amount

# 按照1美元-7人民币汇率编写一个美元和人民币的双向兑换程序。
print("欢迎使用汇率兑换程序！")
print("1. 美元兑换人民币")
print("2. 人民币兑换美元")
choice = input("请选择兑换类型 (输入1或2): ")

if choice == "1":
    usd_amount = float(input("请输入要兑换的美元金额: $"))
    rmb_amount = usd_to_rmb(usd_amount)  # 使用usd_to_rmb函数将美元金额转换为人民币金额
    print(f"{usd_amount}美元 = {rmb_amount}人民币")
elif choice == "2":
    rmb_amount = float(input("请输入要兑换的人民币金额: "))
    usd_amount = rmb_to_usd(rmb_amount)  # 使用rmb_to_usd函数将人民币金额转换为美元金额
    print(f"{rmb_amount}人民币 = {usd_amount}美元")
else:
    print("无效选择，请输入1或2。")
