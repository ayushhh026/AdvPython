# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself
#                 Best for class level data or require access to the class itself
class Student:
    count = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa

    def get_info(self): #INSTANCE METHOD
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls): # used for class variable operations
        return f"total no of students : {cls.count}" # do need to call with object directl call with class
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa {cls.total_gpa / cls.count}"
    
    
student1 = Student("spongebob",4.0)
student2 = Student("sandy",3.0)
student3 = Student("patrick",3.5)

    
print(Student.get_count())

print(Student.get_average_gpa())


'''
Why class methods are preferred (real reasons)
✅ 1. Encapsulation (VERY important)
You hide internal data and expose behavior instead.
Bad practice:
print(Student.count)

Good practice:
print(Student.get_count())

If tomorrow you change how count works, your external code doesn't break.

✅ 2. Central place for logic

Today:
return f"Total no of students: {cls.count}"

Tomorrow:
return f"Active students: {cls.count} (updated)"

You update one method, not 50 print statements.'''