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
 