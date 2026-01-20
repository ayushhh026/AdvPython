# class variable = Shared among all instances of a class
#                  Defined outsided the cosntructor
#                  Allow you to share data among all objects created from that class


class Student: #make first letter Capital S

    class_year = 2025 #class variable  
    num_students =0
    def __init__(self,name,age): #constructor code will alwyas be executed when an obejct is initialized
        self.name = name #instance variable
        self.age = age
        Student.num_students += 1 #use class name to modify class variable

#object or instance of class 
student1=Student("Jake",20)
student2=Student("Spongebob",30)


print(Student.class_year) # access class variable using Class name
print(Student.num_students) # this will give output 2 as there are 2 objects created


print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
