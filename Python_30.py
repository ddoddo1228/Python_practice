lanStr = ("Java", "C", "Python", "R", "Web")

get_char_count = lambda s: (s, len(s))

for language in lanStr:
    result = get_char_count(language)
    print(f"{result[0]:<10} {result[1]}")
