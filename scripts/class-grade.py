class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return self.score >= Grade.minimum_passing

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))

# Output
print(f"{pieter.name} received a grade of: {pieter.grades[0].score}")
print("Passing status:", pieter.grades[0].is_passing())