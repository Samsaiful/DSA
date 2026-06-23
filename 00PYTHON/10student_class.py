class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod
    def welcoome():
        print("welcome")

    def average(self):
       return (self.marks[0]+self.marks[1]+self.marks[2])/3

stu1=student("suman",[77.25,90,87])
print(stu1.average())
student.welcoome()
stu1.welcoome()
        
stu2=student("sarkar",[94,90,92])
print(stu2.average())
student.welcoome()
