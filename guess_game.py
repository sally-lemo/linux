#!/usr/bin/env python3
import random
print("猜数字游戏：1-10")
secret = random.randint(1, 10)
while True:
    guess = int(input("请输入猜测: "))
    if guess == secret:
        print("✓ 猜对了！")
        break
    elif guess < secret:
        print("↑ 太小")
    else:
        print("↓ 太大")
