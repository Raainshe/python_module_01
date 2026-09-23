
class plant:
    def __init__(self, name: str, size: int, age:int):
        self.name = name
        self.size = size
        self.age = age
    def show(self):
        print(f"{self.name}: {self.size}cm and {self.age} days old")

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