class Student:
    type = "Student"

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    getDesc = getName

s = Student("Ram")
print(s.type)

print(s.getDesc())