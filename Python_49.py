def print_alphabets(start_char, end_char):
    start_ord = ord(start_char)
    end_ord = ord(end_char)

    for char_code in range(start_ord, end_ord + 1):
        current_char = chr(char_code)
        print(current_char, end=' ')

    print()

start_char = input("시작문자: ")
end_char = input("끝 문자: ")

print_alphabets(start_char, end_char)
