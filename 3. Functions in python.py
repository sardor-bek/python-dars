# function is a collection of instructions  or collection of code

# def salom_ber(ism, familya):
#     '''Foydalanuvchi ismini qabul qluvchi va unga salom beruvchi funksiya!'''
#     print(f"Foydalanuvchi ismi:  {ism.title()}\n"
#           f"Foydalanuvchi familyasi: {familya.title()}")
# salom_ber('Sardor', 'Bek')
#
# def age_counter(name, b_year):
#     '''User age counter function'''
#     print(f"{name.title()} is {2021-b_year} years old")
# age_counter(name='Sardor', b_year=1997)

##### practice 1

# def finding_b_year(name, age):
#     '''Ask user name and age, and calculate his birth year'''
#     print(f"name: {name.title()}\n"
#           f"age: {2021-age}")
# finding_b_year('Sardor', 24)

##### practice 2

# def calculating_square(number):
#     '''Asking a number and calculating square and cub'''
#     print(f"number: {number}\n"
#           f"square: {number**2}\n"
#           f"cub: {number**3}")
# calculating_square(2)

##### practice 3

# def calculating_odd_even(number):
#     '''Finding even number or odd number via asking number'''
#     if number%2:
#         print(f"{number} is odd ")
#     else:
#         print(f"{number} is even")
# calculating_odd_even(4)
# calculating_odd_even(5)

#### practice 4

# def big_or_small(num1, num2):
#     '''to find which number is bigger'''
#     if num1 > num2:
#         print(f"{num1} is bigger than {num2}")
#     elif num1 < num2:
#         print(f"{num1} is smaller than {num2}")
#     else:
#         print(f"{num1} and {num2} are equal")
# big_or_small(9, 2)

#### PRACTICE 5

# def user_xy(x, y):
#     '''to upgrade x to y'''
#     print(f"{x**y}")
# user_xy(3, 3)

##### practice 6

# def user_xy(x, y=2):
#     '''to upgrade x to y'''
#     print(f"{x**y}")
# user_xy(3)

##### practice 7

# def user_number(number):
#     '''to check user number is to divide with residual'''
#     for n in range(2,11):
#         if number%n:
#             print(f"{number} is not divided to {n} without residual")
#         else:
#             print(f"{number} is divided to {n}")
# user_number(70)