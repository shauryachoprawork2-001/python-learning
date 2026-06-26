#attributes
#class common sabke liye 
# instance sabke liye common na ho

class Student:
    college_name= "abc"

    def __init__(self,name,gpa):
        self.name = name 
        self.gpa = gpa 

stu1=Student("rahul",8)
print(f"his {stu1.name}his name is{stu1.gpa}.")
print(Student.college_name)

#dono tareeke se we can call function
#instance more priority 