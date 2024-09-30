# Function is way to seperate an logic of piece of code in a program so that it can easily call later and no need to write same code multiple times.
# a = int(input("Enter your number"))
# b= int(input("Enter your number"))  #Simply write logic
# c =int(input("Enter your number"))
# average = (a+b+c)/3
# print(average)

# With Function Write the logic
# def avg ():                #Function Definition
#     a = int(input("Enter your number  "))
#     b= int(input("Enter your number  "))
#     c =int(input("Enter your number  "))
#     average = (a+b+c)/3
#     print(average)
 
# avg()     #Function call
# avg()
 

# Function with Parameter
# def good(name , ending):
#     print("Good Day " + name)
#     print(ending)
#     return "done"


# a = good("Krishna" , "thankyou")
# print(a)



# def good(name , ending= "hello"):         #Default Parameter
#     print("Good Day " + name)
#     print(ending)

# good("Krihsna" , "bye")
# good("Krihsna")




#Recursion
# n = int(input("Enter the number - "))
# def factorial (n):
#     if(n == 1 or n == 0):
#         return 1
#     return n * factorial(n-1)

# print(factorial(n))


# Practice


# a = 1
# b = 2
# c = 3
# def great (a ,b ,c):
#     if(a>b and a>c):
#         return "a is the greatest"
#     elif(b>a and b>c):
#          return "b is the greatest"
#     else:
#          return "c is the greatest"

# x = great(a ,b ,c)
# print(x)

 