def auto_info(company, model, color, types, year, price=None):
    auto = {'company': company,
            'model': model,
            'color': color,
            'type': types,
            'year': year,
            'price': price}
    return auto
auto1 = auto_info('Toyota', 'Yaris', 'black', 'Automatic', 2015)
auto2 = auto_info('GM', 'Malibu', 'white', 'Automatic', 2015, 15000)
autos = [auto1, auto2]
print(autos)

def auto_enter():
    autos = []
    while True:
        print("\n Please, enter below information: ", end='')
        company = input("manufactor: ")
        model = input("model: ")
        color = input("color: ")
        types = input("type: ")
        year = input("year: ")
        price = input("price: ")
        autos.append(auto_info(company, model, color, types, year, price))
        # again ask to add or not
        answer = input("do want to add? (yes/no): ")
        if answer == 'no':
            break
    return autos





def info_print(auto_info):
    print(f"{auto_info['color'].title()},  {auto_info['company'].upper()}, "
          f"{auto_info['model'].title()}, {auto_info['type']}, "
          f"{auto_info['price']}$, {auto_info['year']} year")
