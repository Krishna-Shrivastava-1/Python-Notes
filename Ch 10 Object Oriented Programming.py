# OOP is also a type of programming in which DRY concept is follow which is {Don' Rapeat Yourself}
# Class is a Blue Print to create Object
# When a form is empty then that for is not own by anybody so we can sa it is an class. But at that time when that dform is filled by somebody then that filled form is of that particular person we can say that is object.

# class employee:  #making class  {It is just a empty template}
    # name = "Krishna"
    # language = "Python"   #this is a class attribute
    # salary = 77000000000

# Krishna = employee       # making object
# Krishna.name = "Krishna Shrivastava" #this is a object OR instance attribute
# print(Krishna.salary , Krishna.language , Krishna.name)

# rohan = employee         # making object
# rohan.name = "Robinson"
# print(rohan.salary , rohan.language , rohan.name)


# Here name is object attribute and salary and language are class attribute as they directly belong to the class.

# Instanace  VS Class Attribute

# class employee:  #making class  {It is just a empty template}
    # name = "Krishna"
    # language = "Python"   #this is a class attribute
    # salary = 77000000000

# Krishna = employee       # making object
# Krishna.language = "Javascript" #this is a object OR instance attribute
# print( Krishna.language)
# Instance attribute stake preference over during assigment and retrival on Class attriute. Yu will only get instance attribute.

# Self Parameter
# class employee:  #making class  {It is just a empty template} this is a class attribute
    # salary = 77000000000
    
    # def geinfo(self):
    #     print(f"The language is {self.language}. The salary is {self.salary} ")
    
    # def greet(self):
    #     print(f"Good morning")

    # They don't need self and marked as a fuction they don't need nothing from object or property.
    # def greet():
    #     print(f"Good morning")

# Krishna = employee()       # making object
# Krishna.language = "Javascript" #this is a object OR instance attribute
# Krishna.geinfo()
# Krishna.greet()
# employee.geinfo(Krishna)

#  Constructor
# class employee:  #making class  {It is just a empty template} this is a class attribute
    # salary = 77000000000
    
    
    # def __init__(self , name ,salary  ,language):    # Dunder method whic start from underscore and these are special method which is automatically called
    #     self.name  = name 
    #     self.salary  =salary 
    #     self.language  =language 
        
    #     print("Iam creating an object")
    
    
    # def geinfo(self):
    #     print(f"The language is {self.language}. The salary is {self.salary} ")
    
    # def greet(self):
    #     print(f"Good morning")

    # They don't need self and marked as a fuction they don't need nothing from object or property.
#     def greet():
#         print(f"Good morning")

# Krishna = employee("Krishna" , 1234561234567 , "Javascript")       # making object
# Krishna.name = "Hello" #this is a object OR instance attribute
# print(Krishna.name ,Krishna.salary , Krishna.language)


# Practice Set
# class programmer:
#     company =  "Microsoft"
#     def __init__(self , name ,salary , pin):
#         self.name = name
#         self.salary = salary
#         self.pin  = pin

# p  = programmer("Krishna" , 78456784500000 , 124587)
# print(p.name , p.salary , p.pin  ,p.company)

# r  = programmer("Rohan" , 784567 , 1245)
# print(r.name , r.salary , r.pin  ,r.company)
        


# class calculator:
#     def __init__(self ,n):
#         self.n = n
    
#     def square(self):
#         print(f"square of {self.n} is {self.n**2}")
    
#     def cube(self):
#         print(f"cube of {self.n} is {self.n**3}")
    
#     def squareroot(self):
#         print(f"squareroot of {self.n} is {self.n**1/2}")
        
# a = calculator(4)
# a.square()
# a.cube()
# a.squareroot()



class demo:
    a = 4

o = demo
print(o.a)
o.a = 0
print(o.a)
print(demo.a)