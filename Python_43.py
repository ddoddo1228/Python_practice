def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("숫자 입력: "))
    
    if num < 0:
        print("음수를 입력할 수 없습니다.")
    else:
        result = factorial(num)
        print(f"{num}! = {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")
