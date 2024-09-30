# a = int(input("Enter your age - "))
# if, elif, else Ladder
# if (a>= 18):
#     print("You are above the age of consent")
# elif(a < 0):
#     print("Enter correct age")
# else:
#     print("You are below the age of consent")

# Relational Operator Or Comparision Operator
# These operator used to evaluate the conditions
# Example are:
# 1)Equals [==]
# 2)Greater than Equals [>=]
# 3)Less than Equal [<=] 

#  Logical Operator
# 1) and - True if both conditions are true
# 2) or - True if one operand or condition is true then it return true or else false
# 3) not - Inverts true to falase and false to true


# a = int(input("Enter your age - "))


# if statement no.1 it is independent if
# if(a%2 == 0):
#     print("a is even")
# End of if statement no.1


# if statement no.2
# if (a>= 18):
#     print("You are above the age of consent")
# elif(a < 0):
#     print("Enter correct age")
# else:
#     print("You are below the age of consent")
# End of if statement no.
#  Practice



# {in} keyword in pyhton check that a string or that item is in that variable or not it return true if it is otherwise false

# n = int(input("Enter Your Number 1 - "))
# z = int(input("Enter Your Number 2 - "))
# c = int(input("Enter Your Number 3 - "))
# v = int(input("Enter Your Number 4 - "))
# if(n>z):     # Simple Stright Forward Way
#     print(n)
# elif(n>c):
#     print(n)
# elif(n>v):
#     print(n)
# elif(z>n):
#     print(z)
# elif(z>c):
#     print(z)
# elif(z>v):
#     print(z)
# elif(c>n):
#     print(c)
# elif(c>v):
#     print(c)
# elif(c>z):
#     print(c)
# else:
#     print(v)


#  Another Better way

# a1 = int(input("Enter Your Number 1 - "))
# a2 = int(input("Enter Your Number 2 - "))
# a3 = int(input("Enter Your Number 3 - "))
# a4 = int(input("Enter Your Number 4 - "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest Number a1 : ", a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest Number a2 : ", a2)
# elif(a3>a2 and a3>a1 and a3>a4):
#     print("Greatest Number a3 : ", a3)
# else:
#     print("Greatest Number a4 : ", a4)




# p1 = "Make a lot of money"
# p2 = "Buy now"
# p3 = "subscribe this"
# p4 = "click this"
# comment   = input ("Enter your comment - ")
# if(comment == p1 or p2 or p3 or p4):  #way of writing 1
#     print("It's a Spam")
# else:
#     print("Ok")

# if((p1 in comment) or (p2 in comment) or (p3 in  comment) or (p4 in comment)):
#     print("It's a spam")

# else:
#     print("ok")


# a = input("Enter your name - ")
# if(len(a) < 10):
#     print("Your name has less than 10 words")
# else:
#     print("Your name has more than 10 words")


# n = input("Enter name - ")
# s = ["Krishna" , "Harry" , "Lenovo" , "Apple" , "Samsung"]
# if(n in s):    #in left side write string not list
#     print("This word we have")
# else:
#     print("We don't have")



# post = input("Enter post - ")

# if("Krishna".lower() in post.lower()):
#     print("Post is talking about Krishna")
# else:
#     print("Post is not talking about Krishna")
