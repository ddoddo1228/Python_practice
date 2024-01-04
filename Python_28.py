def fibonacci_sequence(n):
    fib_list = [1, 1]

    if n <= 2:
        return fib_list[:n]

    for i in range(2, n):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)

    return fib_list

try:
    num = int(input("숫자: "))
    result = fibonacci_sequence(num)
    print(result)
except ValueError:
    print("올바른 숫자를 입력하세요.")
