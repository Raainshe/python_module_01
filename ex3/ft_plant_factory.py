
class plant:
    def __init__(self, name: str, size: float, age:int):
        self.name = name
        self.size = size
        self.age = age
    def show(self):
        print(f"Created: {self.name}: {self.size}cm and {self.age} days old")
    def age2(self):
        total_growth = 0
        for day in range(7):
            if self.name == "Rose":
                self.size += 0.5
                total_growth += 0.5
                self.age += 1
            if self.name == "Daisy":
                self.size += 0.2
                total_growth += 0.2
                self.age += 1
            if self.name == "Cactus":
                self.size += 0.1
                total_growth += 0.1
                self.age += 1
                
            day += 1

            print(f"Day {day}\n{self.name}: {self.size}cm age: {self.age}")
        print(f"Growth this week: {total_growth}cm")


def main():
    #create classes
    rose = plant("Rose", 23.0, 40.)
    daisy = plant("Daisy", 33.0, 50)
    cactus = plant("Cactus", 10.0, 100)

    print("==Plant Factory Output==")
    rose.show()
    daisy.show()
    cactus.show()
    print("==============")




if __name__ == "__main__":
    main()