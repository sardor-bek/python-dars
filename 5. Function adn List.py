# def summa(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(summa(2, 2, 3))

def student_info(name,surname,**info):
    info['name'] = name
    info['surname'] = surname
    return info
student1 = student_info('Sardor', 'Nazar', course='1st', falucty='CS50')
print(student1)