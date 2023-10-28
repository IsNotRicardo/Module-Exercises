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


def main():
    cars = list(range(10))
    for i in range(len(cars)):
        cars[i] = Car(f"ABC-{i + 1}", random.randint(100, 200))

    while True:
        for i in range(len(cars)):
            cars[i].accelerate(random.randint(-10, 15))
            cars[i].drive(1)

            if cars[i].trav_dist >= 10000:
                print(cars[i].reg_number, "won the race!\n")
                break
        else:
            continue
        break

    for i in range(len(cars)):
        print(vars(cars[i]))


main()
