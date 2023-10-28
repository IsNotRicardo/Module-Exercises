class Car:
    def __init__(self, rn, ms):
        self.reg_number = rn
        self.max_speed = ms
        self.cur_speed = 0
        self.trav_dist = 0


def main():
    new_car = Car("ABC-123", 142)
    print(vars(new_car))


main()
