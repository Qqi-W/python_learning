import random

# 生成预设的随机整数
target_number = random.randint(0, 100)

# 猜数游戏
def guess_number_game():
    """
    猜数游戏函数，让用户猜一个预设的随机整数，并根据猜测结果给予提示
    """
    guess_count = 0
    while True:
        user_guess = int(input("请输入你猜测的数字："))
        guess_count += 1
        if user_guess > target_number:
            print("遗憾，太大了")
        elif user_guess < target_number:
            print("遗憾，太小了")
        else:
            print(f"预测{guess_count}次，你猜中了！")
            break

# 执行猜数游戏
guess_number_game()