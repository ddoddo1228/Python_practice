usage_type = int(input("용도: 1. 주택용, 2. 공업용, 3. 산업용? "))
usage_amount = float(input("사용량(kwh)? "))

if usage_type == 1:
    basic_fee = 190
    rate_per_kwh = 88
elif usage_type == 2:
    basic_fee = 1600
    rate_per_kwh = 182
elif usage_type == 3:
    basic_fee = 7300
    rate_per_kwh = 275
else:
    print("잘못된 용도를 입력했습니다.")
    exit()
total_fee = basic_fee + (usage_amount * rate_per_kwh)

print(f"용도: {usage_type}, 사용량: {usage_amount:,.2f}kwh, 전기요금: {total_fee:,.2f}원")
