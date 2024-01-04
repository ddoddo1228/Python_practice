second = int(input("초를 입력하세요: "))

hours = second// 3600
remain = second % 3600
minutes = remain // 60
seconds = remain % 60

print(f"입력받은 {second} 초는 {hours} 시간 {minutes} 분 {seconds} 초이다.")
