class student:
    def __init__(self,subject,cgpa):
        self.subject=subject #they are different for different people so they are caled instance attributes 
        self.cgpa =cgpa
    def get_cgpa(self):
        return self.cgpa 

stu1=student("maths",8)
print(stu1.subject)  
print(stu1.get_cgpa())