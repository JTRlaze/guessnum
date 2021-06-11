# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜對的話 要告訴他 比答案大/小


import random
r = random.randint(1, 100)
count = 0
while True:
    count = count + 1
    user = input('請猜數字:')
    user = int(user)
    print('這是你猜的第', count, '次')
    if user == r:
        print('終於猜對了!')
        break
    elif user < r:
        print('比答案小')
    else:
        print('比答案大')

