try:
    with open("C:/Users/USER/Documents/score.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        score = int(line.strip())  
        total += score

    average = total / len(lines)

    print(f"합계: {total}, 평균: {average:.2f}")

except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다.")

except ValueError:
    print("파일 내용에 올바른 숫자가 포함되어 있지 않습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
