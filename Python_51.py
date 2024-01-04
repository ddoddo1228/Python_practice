try:
    with open("C:/Users/USER/Documents/sosok.txt", "w", encoding="utf-8") as f:
        f.write("송미자 산업정보시스템학과 010-1111-1234\n")
        f.write("이명섭 스페인어과 010-2222-1234\n")
        f.write("아이키 실용무용과 010-3333-1234\n")
        f.write("박태호 영어영문학과 010-4444-1234\n")
        f.write("아이유 실용음악과 010-555-1234\n")

except Exception as e:
    print(f"오류 발생: {e}")
