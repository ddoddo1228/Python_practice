def calculate_average(num_list):
    if not num_list:
        return 0.00

    average = sum(num_list) / len(num_list)
    return round(average, 2)

num = [15, 25, 33, 17, 88, 25]

result = calculate_average(num)

print(f"리스트 평균: {result:.2f}")
