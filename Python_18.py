grade = [90, 85, 70, 60, 95]

for i in range(len(grade)):
    if grade[i] >= 90:
        print(f"{i+1}번 학생 {grade[i]}점: 장학금 대상")
