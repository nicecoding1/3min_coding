import random 

a = random.randint(1, 100)
count = 1
print("="*20)
print("  숫자 맞추기 게임")
print("="*20)
print()

while(True):
    if count > 7:
        print("실패하였습니다. 정답은 %d 입니다." % a)
        break

    b = int(input("[%d] 숫자를 입력하세요! : " % count)) 

    if a == b:
        print("정답입니다!!!")
        break
    elif a > b:
        print("UP")
    elif a < b:
        print("DOWN")

    count += 1
