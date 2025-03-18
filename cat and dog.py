class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} year old. ")

    def speak(self):
        print("I dont know what i say")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Snake(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def show(self):
        print(f"{self.name} is {self.age} year old. "
              f"And {self.colour}")

cat = Cat("Tim", 7)
cat.show()
cat.speak()
print()

dog = Dog("BOB", 10)
dog.show()
dog.speak()
print()

pet = Pet("Liz", 8)
pet.show()
pet.speak()
print()

snake = Snake("ABS", 3, "Yellow")
snake.show()
snake.speak()
print()