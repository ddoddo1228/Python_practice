try:
    input_file_path = "C:/Users/USER/Documents/flower_r.txt"
    output_file_path = "C:/Users/USER/Documents/flower_w.txt"

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        content = input_file.read()

    content_upper = content.upper()
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(content_upper)

    print(f"파일이 성공적으로 변환되어 '{output_file_path}'에 저장되었습니다.")

except FileNotFoundError:
    print(f"파일 '{input_file_path}'을 찾을 수 없습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
