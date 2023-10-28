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
    new_car = Car("ABC-123", 142)
    for i in range(4):
        match i:
            case 0:
                new_car.accelerate(30)
                new_car.drive(0.5)
            case 1:
                new_car.accelerate(70)
                new_car.drive(2)
            case 2:
                new_car.accelerate(50)
                new_car.drive(3.5)
            case 3:
                new_car.accelerate(-200)
                new_car.drive(1)
        print(vars(new_car))


main()
