import random

class VacuumEnvironment:
    def __init__(self):
        # 2 rooms, 4 parts each
        self.rooms = {
            "A": [random.choice(["Dirty", "Clean"]) for _ in range(4)],
            "B": [random.choice(["Dirty", "Clean"]) for _ in range(4)]
        }

    def is_clean(self):
        for room in self.rooms:
            if "Dirty" in self.rooms[room]:
                return False
        return True

    def display(self):
        print("\nEnvironment Status:")
        for room in self.rooms:
            print(f"Room {room}: {self.rooms[room]}")


class VacuumAgent:
    def __init__(self, environment):
        self.env = environment
        self.current_room = "A"
        self.position = 0  # index 0-3
        self.performance = 0

    def perceive(self):
        return self.env.rooms[self.current_room][self.position]

    def suck(self):
        if self.perceive() == "Dirty":
            self.env.rooms[self.current_room][self.position] = "Clean"
            self.performance += 10
            print(f"Sucked dirt at {self.current_room}{self.position+1}")
        else:
            print(f"{self.current_room}{self.position+1} already clean")

    def move_right(self):
        if self.position < 3:
            self.position += 1
            self.performance -= 1
            print("Moved Right")

    def move_left(self):
        if self.position > 0:
            self.position -= 1
            self.performance -= 1
            print("Moved Left")

    def switch_room(self):
        self.current_room = "B" if self.current_room == "A" else "A"
        self.position = 0
        self.performance -= 2
        print("Switched Room")

    def run(self):
        while not self.env.is_clean():
            self.env.display()
            print(f"\nAgent at {self.current_room}{self.position+1}")

            if self.perceive() == "Dirty":
                self.suck()
            else:
                if self.position < 3:
                    self.move_right()
                else:
                    if self.current_room == "A":
                        self.switch_room()
                    else:
                        break  # End after cleaning all in B

        print("\nFinal Environment:")
        self.env.display()
        print("\nAll rooms clean!")
        print("Performance Score:", self.performance)


if __name__ == "__main__":
    env = VacuumEnvironment()
    agent = VacuumAgent(env)
    agent.run()