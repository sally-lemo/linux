#!/usr/bin/env python3
"""猜数字游戏 - 修复版（无缩进错误）
功能：
  - 实时输出（flush）
  - 单次输入即响应
  - 猜中/超限自动退出
  - 防非数字输入
"""
import random
import sys

print("🎮 猜数字游戏：1-10", flush=True)
secret = random.randint(1, 10)
attempts = 0

while attempts < 5:
    try:
        guess = input("请输入猜测: ")
        sys.stdout.flush()
        guess = int(guess.strip())
        attempts += 1
        if guess == secret:
            print("✓ 猜对了！🎉", flush=True)
            break
        elif guess < secret:
            print("↑ 太小", flush=True)
        else:
            print("↓ 太大", flush=True)
    except ValueError:
        print("⚠ 请输入数字！", flush=True)
else:
    print(f"⚠ 机会用尽！答案是 {secret}", flush=True)