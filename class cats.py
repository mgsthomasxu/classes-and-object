class cat:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def print_details(self):
        return f"{self.name} is a {self.colour} cat aged {self.age}"


    def change_age(self, age):
        self.age = age

cat1 = cat("Spot", 2, "black")
cat2 = cat("Emil", 4, "white")

print(cat.print_details(cat1))
print(cat.print_details(cat2))

cat1.change_age(3)
cat2.change_age(6)


print(cat.print_details(cat1))
print(cat.print_details(cat2))

