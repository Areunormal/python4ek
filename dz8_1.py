class animal:
    def __init__(self, type, age):
        self.type = type
        self.age = age
class mammal(animal):
    def __init__(self, type, age, type_of_food):
        super().__init__(type,age)
        self.type_of_food = type_of_food
class human(mammal):
    def __init__(self, type, age, type_of_food, name, height, weight):
        super().__init__(type, age, type_of_food)
        self.name = name
        self.height = height
        self.weight = weight
class cat(mammal):
    def __init__(self, type, age, type_of_food, breed, height, weight):
        super().__init__(type, age, type_of_food)
        self.breed = breed
        self.height = height
        self.weight =  weight
class dog(mammal):
    def __init__(self, type, age, type_of_food, breed, height, weight):
        super().__init__(type, age, type_of_food)
        self.breed = breed
        self.height = height
        self.weight =  weight