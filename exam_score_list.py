score = []

while True:
    kor  = int(input("국어 점수를 넣어주세요. : "))
    eng  = int(input("영어 점수를 넣어주세요. : "))
    math = int(input("수학 점수를 넣어주세요. : "))

    if kor == 0 and eng == 0 and math == 0:
        break

    my_sum = kor + eng + math
    my_avg = my_sum / 3.0

    score.append((kor, eng, math, my_sum, my_avg))
    print()

print()
j = 1
for i in score:
    print(j, " 국어: %3d, 영어: %3d, 수학: %3d, 총점: %3d, 평균: %.2f" % (i[0], i[1], i[2], i[3], i[4]))
    j += 1

print("총 %d 명 처리하였습니다." % (j-1))
