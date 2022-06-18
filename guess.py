# 產生一個隨機整數(1~100)(不要印出來)
# 讓使用者重複(loop)輸入數字去猜
# 猜對的話 印出"恭喜猜對了!"
# 猜錯的話 要提示 比答案大/小
import random

r = random.randint(1, 100)
while True: 
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜猜對了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
		