animal = ("병아리", "오리", "거위", "송아지", "오리", "암탉")

animal_with_goat = animal + ("염소",)

animal_with_cow = ("얼룩소",) + animal_with_goat[1:]

print(animal_with_cow)
