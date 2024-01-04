movie_list = [("오징어게임", 50.45), ("이터널스", 35.46), ("그레비티", 9.8), ("노타임투다이", 52.5), ("스파이더맨", 15.47)]

# movie_list를 예매율을 기준으로 내림차순 정렬합니다.
sorted_movie_list = sorted(movie_list, key=lambda x: x[1], reverse=True)

# 헤더 출력
print("영화 제목\t예매율\t순위")
print("=========\t======\t====")

# 정렬된 리스트를 출력합니다.
for rank, (title, booking_rate) in enumerate(sorted_movie_list, start=1):
    print(f"{title}\t{booking_rate}%\t{rank}")
