import math

"""

n = 'fd\'df'
print(n)gd
gdgsgs
"""

# a = 4
# b = 5
# c = 7
# print(f"a + b + c = {a + b + c}")

# c = "1234"
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# a = int(input("Enter Number: "))
# print(type(a))
# b = int(input("Enter Number: "))
# print(type(b))
# c = a / b
# print(type(c))
# print(c)

speed = int(input("Enter speed: "))
distance = int(input("Enter distance: "))
# time = math.ceil(distance / speed)
print(f"Машина проедет {distance} км за {math.ceil(distance/speed)} дней")
