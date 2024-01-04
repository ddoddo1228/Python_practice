def calculate_expression(expression):
    try:
        result = eval(expression)
        if 0 <= result <= 127:
            return chr(result)
        else:
            print(result)
            return None
    except Exception as e:
        print("올바른 수식이 아닙니다.")
        return None

while True:
    expression = input("수식 입력: ")
    if expression.lower() == "exit":
        break

    char_result = calculate_expression(expression)
    if char_result is not None:
        print(char_result)
