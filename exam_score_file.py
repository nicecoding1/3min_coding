score = []

try:
    with open("exam_score.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            name, kor, eng, math = line.split(',')
            math = math.strip()

            if kor.isdigit() == False:
                kor = 0
            if eng.isdigit() == False:
                eng = 0
            if math.isdigit() == False:
                math = 0

            kor = int(kor)
            eng = int(eng)
            math = int(math)

            my_sum = kor + eng + math
            my_avg = my_sum / 3.0
            score.append((name, kor, eng, math, my_sum, my_avg))
except Exception as e:
    print(e)

print()
j = 1
for i in score:
    print(j, "이름: %s, 국어: %3d, 영어: %3d, 수학: %3d, \
총점: %3d, 평균: %.2f" % (i[0], i[1], i[2], i[3], i[4], i[5]))
    j += 1

print("총 %d 명 처리하였습니다." % (j-1))
