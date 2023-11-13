import random


class Car:
    def __init__(self, rn, ms):
        self.reg_number = rn
        self.max_speed = ms
        self.cur_speed = 0
        self.trav_dist = 0

    def accelerate(self, change):
        self.cur_speed += change
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def drive(self, time):
        self.trav_dist += time * self.cur_speed


class ElectricCar(Car):
    def __init__(self, rn, ms, bat):
        super().__init__(rn, ms)
        # battery capacity is measured in kWh
        self.battery = bat


class GasolineCar(Car):
    def __init__(self, rn, ms, tank):
        super().__init__(rn, ms)
        # tank capacity is measured in liters
        self.tank = tank


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    for car in [electric_car, gasoline_car]:
        car.accelerate(random.randint(0, car.max_speed))
        car.drive(3)
        print(f"{car.reg_number}: {car.trav_dist} km")


main()
