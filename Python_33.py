import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

user_radius = float(input("반지름? "))

circle_area = calculate_circle_area(user_radius)

print("원의 넓이 = {:.1f}".format(circle_area))
