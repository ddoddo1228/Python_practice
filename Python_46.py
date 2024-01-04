try:
    with open("C:/Users/USER/Documents/sample.txt", "r", encoding="utf-8") as file:
        # 첫 번째 줄 읽기
        line = file.readline()

        # 파일 끝까지 반복
        while line:
            # 읽은 내용 출력
            print(line, end='')

            # 다음 줄 읽기
            line = file.readline()

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
