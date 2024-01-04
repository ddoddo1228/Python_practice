listStr = ["python", "programming", "seoul", "korea", "university"]

try:
    index = int(input("리스트의 인덱스를 입력하세요: "))
    result = len(listStr[index])
    print(f"{listStr[index]}의 길이는 {result}입니다.")

except IndexError:
    print("리스트의 인덱스를 벗어났습니다. 프로그램을 종료합니다.")

except ValueError:
    print("올바른 숫자를 입력하세요.")

except Exception as e:
    print(f"오류 발생: {e}")
    print("프로그램을 종료합니다.")

else:
    print("프로그램이 정상적으로 실행되었습니다.")

finally:
    print("프로그램을 종료합니다.")
