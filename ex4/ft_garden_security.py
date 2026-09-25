
class plant:
    def __init__(self, name: str, size: float = 0.1, age:int = 1):

        if size < 0 or age < 0:
            print(f"Your values are negative. Please change your age and/or height to the correct values")
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

    def set_height(self, new_size: float):
        if new_size > 0:
            self.size = new_size
            print(f"New height: {self.size}")
        else:
            print("Enter a valid value")

    def set_age(self, new_age: float):
        self.age = new_age
    
    def get_age(self):
        return self.age

    def get_height(self):
        return self.size


def main():
    rose = plant("Rose", 23.0, 40)
    daisy = plant("Daisy", 33.0, 50)
    cactus = plant("Cactus", 10.0, 100)
    plant("Weed", -1.0, -5)

    print("==Plant Factory Output==")
    rose.show()
    daisy.show()
    cactus.show()

    print("==Getters==")
    print(f"Rose age: {rose.get_age()} days")
    print(f"Rose height: {rose.get_height()}cm")

    print("==Setters==")
    rose.set_age(45)
    rose.set_height(30.0)
    rose.set_height(-2.0)
    print(f"Rose age after update: {rose.get_age()} days")
    print(f"Rose height after update: {rose.get_height()}cm")

    print("==Weekly growth==")
    rose.age2()
    daisy.age2()
    cactus.age2()




if __name__ == "__main__":
    main()