# METHODS
class Person():
    def __init__(self, id, name):
        # ATTRIBUTES
        self.id = id
        self.name = name

    def Display(self):
        print("Person Name: " + self.name + " Person ID: " + str(self.id))


# INHERITANCE
class Student(Person):
    def __init__(self, id, name, Majors):
        self.id = id
        self.name = name
        self.Majors = Majors

    def Display(self):
        print("Student Name: " + self.name + " Student ID: " + str(self.id) + " with majors: " + self.Majors)


class Faculty(Person):

    def __init__(self, id, name, Department):
        self.id = id
        self.name = name
        self.Department = Department

    def Display(self):
        print("Faculty Name: " + self.name + " Faculty ID: " + str(self.id) + " with department: " + self.Department)


# INSTANCES OF CLASS : OBJECTS
First_Person = Person(101, "Nikki")
First_Student = Student(150, "Nidhi", "Python")
First_Faculty = Faculty(200, "Netto", "Mathematics")

# POLYMORPHISM
First_Person.Display()
First_Student.Display()
First_Faculty.Display()
