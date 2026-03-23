#!/usr/bin/env python3
"""猜数字游戏 - 打包为可执行脚本
使用方法：
  chmod +x guess_game.py
  ./guess_game.py
"""
import random
print("🎮 猜数字游戏：1-10")
secret = random.randint(1, 10)
while True:
    try:
        guess = int(input("请输入猜测: "))
        if guess == secret:
            print("✓ 猜对了！🎉")
            break
        elif guess < secret:
            print("↑ 太小")
        else:
            print("↓ 太大")
    except ValueError:
        print("⚠ 请输入数字！")
