class Elevator:
    def __init__(self, bf, tf):
        self.bottom = bf
        self.top = tf
        self.current = bf

    def go_to_floor(self, floor):
        while floor != self.current:
            if floor > self.current:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        self.current += 1
        print(f"↑ Is now in floor {self.current}")

    def floor_down(self):
        self.current -= 1
        print(f"↓ Is now in floor {self.current}")


class Building:
    def __init__(self, bf, tf, el):
        self.bottom = bf
        self.top = tf
        self.elevators = list(range(el))

        for i in range(el):
            self.elevators[i] = Elevator(bf, tf)

    def run_elevator(self, el_num, floor):
        print(f"\nElevator {el_num + 1}:")
        self.elevators[el_num].go_to_floor(floor)

    def fire_alarm(self):
        print("\nFIRE ALARM ACTIVATED")
        for i in range(len(self.elevators)):
            if self.elevators[i].current != self.bottom:
                self.run_elevator(i, self.bottom)


def main():
    new_building = Building(0, 10, 5)
    new_building.run_elevator(4, 8)
    new_building.run_elevator(2, 4)
    new_building.run_elevator(4, 3)

    new_building.fire_alarm()


main()
