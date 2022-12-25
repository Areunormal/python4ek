class human():
    def __init__(self, gender, age, name, height, weight, ):
        self.gender = gender
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight
class student(human):
    def __init__(self, gender, age, name, height, weight, count_of_hmwrks, count_of_marks, type):
        super().__init__(gender, age, name, height, weight)
        self.count_of_hmwrks = count_of_hmwrks
        self.counf_of_marks = count_of_marks
        self.type = type
    def __eq__(self, other ):
        if self.count_of_hmwrks > other.count_of_hmwrks:
            return ("U pervogo studenta bolshe")
        if self.count_of_hmwrks < other.count_of_hmwrks:
            return ("U vtorogo studenta bolshe")
        if self.count_of_hmwrks == other.count_of_hmwrks:
            return ("odinakovo")


Dima = student("male", 15, "Dima", 170, 50, 15, 16 , "excellent pupil")
Egor = student("male", 13, "Egor", 180, 100, 12, 2 , "bad pupil")
print(Egor==Dima)