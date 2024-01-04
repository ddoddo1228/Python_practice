try:
    file_path = "C:/Users/USER/Documents/sungjuk.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    header = "이 름   국어   영어   수학"
    print(header)
    print("=====   ====   ====   ====")

    for line in lines:
        data = line.split()
        formatted_line = f"{data[0]:<5} {data[1]:<6} {data[2]:<6} {data[3]:<6}"
        print(formatted_line)

except FileNotFoundError:
    print(f"파일 '{file_path}'을 찾을 수 없습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
