class Class:
    __students_count = 22
    def __init__(self, name):
        self. name = name
        self.students, self.grades = [], []

    def add_student(self, stud_name: str, grade: float):
        if len(self.students) < 22:
            self.students.append(stud_name)
            self.grades.append(grade)

    def get_average_grade(self):
        aver = float(f'{sum(self.grades)/len(self.grades):.2f}')
        return aver

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {sum(self.grades)/len(self.grades):.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)

a1_class = Class("1A")
a1_class.add_student("Pe", 4.80)
a1_class.add_student("Ge", 6.00)
a1_class.add_student("Am", 3.50)

print(a_class)
