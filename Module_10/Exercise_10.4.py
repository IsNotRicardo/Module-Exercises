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


class Race:
    def __init__(self, name, dist, car_num):
        self.name = name
        self.distance = dist
        self.cars = list(range(car_num))

        for i in range(car_num):
            self.cars[i] = Car(f"ABC-{i + 1}", random.randint(100, 200))

    def hour_passes(self):
        for i in range(len(self.cars)):
            self.cars[i].accelerate(random.randint(-10, 15))
            self.cars[i].drive(1)

    def print_status(self):
        for i in range(len(self.cars)):
            print(vars(self.cars[i]))

    def race_finished(self):
        for i in range(len(self.cars)):
            if self.cars[i].trav_dist >= self.distance:
                print(self.cars[i].reg_number, "won the race!\n")
                return True


def main():
    new_race = Race("Grand Demolition Derby", 8000, 10)
    hours = 0

    while not new_race.race_finished():
        new_race.hour_passes()
        hours += 1
        if not hours % 10:
            new_race.print_status()
    new_race.print_status()


main()
