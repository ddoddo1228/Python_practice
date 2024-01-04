name = input("이름을 입력하세요: ")
height = float(input("키를 센티미터 단위로 입력하세요: "))
weight = float(input("체중을 킬로그램 단위로 입력하세요: "))

meter = height / 100

bmi = weight / (meter ** 2)

if bmi < 20:
    result = "저체중"
elif 20 <= bmi < 25:
    result = "정상"
elif 25 <= bmi < 30:
    result = "과체중"
else:
    result = "비만"

print(f"{name}님의 BMI는 {bmi:.2f}이며, 비만도는 {result}입니다.")
