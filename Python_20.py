num = int(input("숫자 입력: "))
if num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num}은(는) 소수 입니다.")
else:
    print(f"{num}은(는) 소수가 아닙니다.")
