class Student:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    

student1=Student()
student1.set_name("Abhishek")
name=student1.get_name()
print(name)
print(student1.name)