#### return functions

# def write_full_name(name, surname):
#     full_name = f"{name} {surname}"
#     return full_name
# student = write_full_name('Sardor', 'Nazar')
# student2 = write_full_name('Olim', 'Olimov')
# print(f"{student} is late for the classes ")
# print(f"{student2} is late for the classes ")

# def write_full_name(name, surname, patronic_name=''):
#     if patronic_name:
#         full_name = f"{name} {patronic_name} {surname}"
#     else:
#         full_name = f"{name} {surname}"
#     return full_name.title()
# student1 = write_full_name('olim', 'azizov', 'hakimovich')
# student3 = write_full_name('sardor', 'nazar')
# print(f"darsga kelishdi: {student1} va {student3}")

################ RETURN Dictionary
#
# def auto_info(company, model, color, type, year, price=None):
#     auto = {'company': company,
#             'model': model,
#             'color': color,
#             'type': type,
#             'year': year,
#             'price': price}
#     return auto
# auto1 = auto_info('Toyota', 'Yaris', 'black', 'Automatic', 2015)
# auto2 = auto_info('GM', 'Malibu', 'white', 'Automatic', 2015, 15000)
# autos = [auto1, auto2]
# print(autos)
#
# print("make a list for our website: ")
# autos = [] # make a list
# while True:
#     print("\n Please, enter below information: ", end='')
#     company=input("manufactor: ")
#     model=input("model: ")
#     color=input("color: ")
#     type=input("type: ")
#     year=input("year: ")
#     price=input("price: ")
#     #make list from user's info
#     #make a list then add info to the list:
#     autos.append(auto_info(company, model, color, type, year, price))
#     # again ask to add or not
#     answer = input("do want to add? (yes/no): ")
#     if answer=='no':
#         break
#
# print("\n Autos in our shop:")
# for auto in autos:
#     if auto['price']:
#         price = auto['price']
#     else:
#         price = "Unknown"
#     print(f"{auto['color'].title()} {auto['model'].title()}, {type} type, price: {price}")


################## RETURN Lists

# def distance(min, max, steps=''):
#     numbers = []
#     while min<max:
#         numbers.append(min)
#         min += 1
#         return numbers
#
# print(distance(0, 10))
# print(distance(10, 21))


########### task 1st and 2nd
#
# def customer_info(name, surname, b_year, b_place, email='', phone_number=None):
#     customer = {'name':name,
#             'surname':surname,
#             'b_year':b_year,
#             'b_place':b_place,
#             'email':email,
#             'phone_number':phone_number}
#     return customer
#
# customers = []
# while True:
#     print("\n Please, enter your information:  ", end='')
#     name = input("name: ")
#     surname = input("surname: ")
#     b_year = input("b_year: ")
#     b_place = input("b_place: ")
#     email = input("email: ")
#     phone_number = input("phone number: ")
#     customers.append(customer_info(name, surname, b_year, b_place, email='', phone_number=None))
#     answer = input("Could you keep it on? (yes/no):  ")
#     if answer != 'yes':
#         break
#
# print("Customer:  ")
# for customer in customers:
#     print(f"{customer['name'].title()} {customer['surname'].title()},"
#           f" was born in {customer['b_year']}, was bor in {customer['b_place']}, phone number is {customer['phone_number']}, email address: {customer['email']}")
#
############ task 3rd
#
# def numbers(x, y, z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max
# print(numbers(2, 4, 1))

############### task 4

# def calculate(radius, pi=3.14):
#     circle = {'radius':radius,
#               'diametr':2*radius,
#               'perimetr':2*radius*pi,
#               'face':2*radius**2}
#     return circle
# print(calculate(20))


