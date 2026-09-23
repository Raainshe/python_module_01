
class plant:
    def __init__(self, name: str, size: float, age:int):
        self.name = name
        self.size = size
        self.age = age
    def show(self):
        print(f"{self.name}: {self.size}cm and {self.age} days old")
    def age(self):
        for day in range(7):
            if self.name == "Rose":
                self.size += 0.5
                self.age += 1
                
            day += 1

            print(f"Day {day}\n{self.name}: {self.size}cm age: {self.age}")


def main():
    #create classes
    rose = plant("Rose", 23, 40)
    daisy = plant("Daisy", 33, 50)
    cactus = plant("Cactus", 10, 100)

    rose.show()
    daisy.show()
    cactus.show()


if __name__ == "__main__":
    main()