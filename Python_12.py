number = int(input("어떤 수: "))

ten = format(number, ',d')

two = bin(number)
eight = oct(number)
sixteen = hex(number)

print(f"2진수: {two}, 8진수: {eight}, 10진수: {ten}, 16진수: {sixteen}")
