###################################################

from datetime import datetime

name = 'Honda accord'
max_speed = 220
release_date = datetime(20,1,20)
color = '#fcba03'

honda_accord = {
    'name': "Honda accord",
    'max_speed' : 220,
    release_date: datetime(2020, 1, 20),
    color: '#fcba03',
    'price': 6000,

}

honda_accent2 = {
    'name': "Honda accent2",
    'max_speed': 180,
    release_date: datetime(2021, 1, 20),
    color: '#fcba99',
    'price': 3000,
}

honda_civic= {
    'name': "Honda Civic",
    'max_speed': 180,
    color: (127, 100, 155),
}

cars = [honda_accord, honda_accent2]
def dump_car_to_txt(car):
    return '|'.join(f"{param}:{value}" for param, value  in car.items()) + "\n"


with open('cars.txt', 'wt', encoding='UTF-8') as fh:
    for car in cars:
        fh.write(dump_to_txt(car))
        
        
###############################################################################################        

from datetime import datetime

class Car:
    def __init__(self, name, min_speed, max_speed, release_date, color, price):
        self.name = name
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.release_date = release_date
        self.color = color
        self.price = price
    def get_str_by_self(self):
        return f"name:{self.name}|" \
               f"max_speed:{self.max_speed}" \
               f"min_speed:{self.min_speed}" \
            f"release_date:{self.release_date}" \
            f"color:{self.color}" \
            f"price:{self.price} \n"

    def get_avg_speed(self):
        return (self.min_speed + self.max_speed) /2

honda_accord = Car('Honda Accord', 0, 220, datetime(2020, 1, 20), '#fcba03', 6000)
honda_civic = Car(name='Honda Civic', max_speed=220, min_speed=0, release_date=datetime(2020, 1, 20), color='#fcba03', price=4500)

print(honda_civic.get_str_by_self())
print(honda_civic.get_avg_speed())
# print(honda_accord.release_date)
# print(honda_civic.release_date)
# honda_accent2 = {
#     'name': "Honda accent2",
#     'max_speed': 180,
#     release_date: datetime(2021, 1, 20),
#     color: '#fcba99',
#     'price': 3000,
# }
#
# honda_civic= {
#     'name': "Honda Civic",
#     'max_speed': 180,
#     color: (127, 100, 155),
# }
#
# cars = [honda_accord, honda_accent2]
# def dump_car_to_txt(car):
#     return '|'.join(f"{param}:{value}" for param, value  in car.items()) + "\n"
#
#
# with open('cars.txt', 'wt', encoding='UTF-8') as fh:
#     for car in cars:
#         fh.write(dump_to_txt(car))
