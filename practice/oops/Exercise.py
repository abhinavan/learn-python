class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, name):
        print("hello , my name is ", self.name)

    def describe(self):
        print(" I am a person ")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def get_student_id(self):
        return self._student_id

    def describe(self):
        print("I am a student")


person = Student("Abhinav", "32", "1")
print("My name is : ", person.name, " age: ", person.age,
      " and student_id :", person.get_student_id())
person.describe()
