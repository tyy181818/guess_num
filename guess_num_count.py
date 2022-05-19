import random
r = random.randint(1,100)
count = 0
while True :
    num = input('1~100，請猜數字: ')
    num = int(num)
    count += 1
    print('這是你猜的第', count, '次')
    if num == r :
        print('恭喜你猜對了!')
        break
    elif num > r :
        print('再小一點')
    elif num < r :
        print('再大一點')
    
   