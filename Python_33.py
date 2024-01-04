def print_items_and_calculate_sum(num_list):
    print(" ".join(map(str, num_list)))

    total = sum(num_list)

    print(f"합계: {total}")
num = [15, 25, 33, 17, 88, 25]

result = print_items_and_calculate_sum(num)
