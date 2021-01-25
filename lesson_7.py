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