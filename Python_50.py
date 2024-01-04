try:
    with open("C:/Users/USER/Documents/sample.txt", "r", encoding="utf-8") as file:
        line = file.readline()

        while line:
            print(line, end='')

            line = file.readline()

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
