count = 0

for i in range(5):
    number = int(input("숫자: "))
    if number % 2 == 0:
        count += 1

print("짝수 개수:", count)
