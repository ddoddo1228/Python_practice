global_sum = 0

def calculate_and_print_sum(input_list):
    global global_sum  

    local_sum = sum(input_list)

    global_sum += local_sum

    print("리스트 합계:", global_sum)

num = [1, 3, 5, 7, 9]

calculate_and_print_sum(num)
