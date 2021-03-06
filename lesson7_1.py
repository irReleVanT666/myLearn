from datetime import datetime
import lesson_7_2


class Transport:
    shop_id = 333
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
            f"price:{self.price}"

    def get_avg_speed(self):
        return (self.min_speed + self.max_speed) /2


class Car(Transport):
    def __init__(self, name, min_speed, max_speed, release_date, color, price, wheels):

        super().__init__(name, min_speed, max_speed, release_date, color, price)
        self.wheels = wheels
    def get_str_by_self(self):
        return super(Car, self).get_str_by_self() + f"|Wheels:{self.wheels}"

honda_accord = Car('Honda Accord', 0, 220, datetime(2020, 1, 20), '#fcba03', 6000, 4)

print(honda_accord.get_avg_speed())
print(honda_accord.get_str_by_self())
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