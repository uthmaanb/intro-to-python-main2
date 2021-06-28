import random


class Bus:
    def __init__(self, color, driver_name, num_seats):
        self.color = color
        self.driver_name = driver_name
        self.num_seats = num_seats


bus = Bus(["white", "black", "yellow", "silver", "gold", "purple"], "Jacob", "100")
print(bus.color[random.randint(0, 5)])
print(bus.driver_name)
print(bus.num_seats)
