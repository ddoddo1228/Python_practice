phone = ("iphone", "galaxy", "xiaomi")
company = ("애플", "삼성", "샤오미")

result = zip(phone, company)

for phone_model, company_name in result:
    print(f"{phone_model} {company_name}")
