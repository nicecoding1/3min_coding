score = []


class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

        self.my_sum = self.kor + self.eng + self.math
        self.my_avg = self.my_sum / 3.0

        print("이름: %s, 국어: %3d, 영어: %3d, 수학: %3d, 총점: %3d, \
평균: %.2f" % (self.name, self.kor, self.eng, self.math, self.my_sum, self.my_avg))


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

            Student(name, kor, eng, math)
except Exception as e:
    print(e)
