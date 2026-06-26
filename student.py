class student:
    def __init__(self,subject,cgpa):
        self.subject=subject #they are different for different people so they are caled instance attributes 
        self.cgpa =cgpa
    def get_cgpa(self):
        return self.cgpa # jo self ko use kar rahe hi har ek function different hai ye hai instance methods

stu1=student("maths",8)
print(stu1.subject)  
print(stu1.get_cgpa())

#like abh java c++ ki tarah alag alag constructr nhi ho sakte hai toh ismein sirf ek hi constructor hota hai jo end mai likh jata hai sirf ussi ko hi dekhte hai 
