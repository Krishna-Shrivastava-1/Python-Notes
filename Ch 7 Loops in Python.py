# For doing a work continously or repeatively USe LOOPS
# Loops are of two type 
# 1) For Loop

# for i in range (1, 100):
#     if(i % 7 == 0):
#         print(i)


# for i in range(4):
#     print(i)


# Step Sizing in For loops
# for i in range(0 , 100 , 5):
#     print(i)


# l = ["Krishna" , "Bhaaloo", "Tiger" , "Lion" , "Dragon"]  #Printing List with For Loop
# for i in l:
#     print(i)

# t = ("Krishna" , "Bhaaloo", "Tiger" , "Lion" , "Dragon")  #Printing Tuple with For Loop
# for i in t:
#     print(i)

# s = "Krishna" #Printing String with For Loop
# for i in s:
#     print(i)


# For loops with Else
# l = [1,2,3,4,5,6,7]
# for i in l:
#     print(i)
# else:
#     print("Done")


# 2) While Loop

# n = 1
# while(n<51):
#     print(n)
#     n += 1

# k = "Krishna"
# i= 0
# while (i<5):
#     print(k)
#     i += 1

# l = [1,"Krishna", False , "Harry" , "Python" , "Mowgli"]
# i = 0
# while(i<len(l)):
#     print(l[i])
#     i += 1


# Break Statement  [It exits the Loop right now]
# for i in range (100):
#     if(i == 35):
#         break
#     print(i)



# Continue Statement  [It make sure that if the i value is satisfy the if condition then that value should skip that iteration and after it whole function is run normally]
# for i in range (100):
#     if(i == 35):
#         continue
#     print(i)

# Practice

# y = int(input("Enter that table number- "))
# for i in range (1, 11):
#     print(f"{y} X {i} = {y *i}")

# l = ["Krishna", "Harry" , "Sachin" , "Suhana"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello, {name}")

# y = int(input("Enter that table number- "))
# i = 1 
# while (i <11):
#     print(f"{y} X {i} = {y *i}")
#     i += 1


# n = int(input("Enter that  number- "))
# for i in range (2 , n):
#     if(n % i == 0):
#         print("It's a not prime number")
#         break
# else:
#     print("Number is prime")




# n = int(input("Enter that  number- "))
# i = 1
# sum = 0
# while(i <= n):
#     sum += i
#     i+1

# print(sum)



# !5 = 1 X 2 X 3 X 4 X 5
# product = 1
# n = int(input("Enter that  number- "))
# for i in range (1 , n+1):
#     product = i * product
#     print(product)


# n = int(input("Enter that  number- "))
# s = " *"
# for i in range (1 , n+1):
#     print (s*i)

# n = int(input("Enter that  number- "))
# for i in range(1 , n+1):
#     print(" " * (n-i), end ="")
#     print("*"* (2*i-1), end = "")
#     print("")
    # print(" " * (n-i), end ="")
    # print("*"* (2*i-1), end = "")
    # print("")

# for i in range (1 , n+1):
#     print(" " * (n-i), end="")
#     print("*" * (i), end = "" )
#     print("")



# n = int(input("Enter that  number- "))
# for i in range (1 , n+1):
#    if(i == 1 or  i== n):
#       print("*" * n , end= (""))
#    else:
#       print("*" , end= "")
#       print( " "* (n-2), end="")
#       print("*" , end= "")
#       print()






# y = int(input("Enter that table number- "))
# for i in range (1, 11):
#     print(f"{y} X {11 - i} = {y *(11 - i)}")




age1 , age2 = int(input('Enter age and your friend age - ').split())
if (age1 == age2):
    print('Age are same')
elif(age1 > age2):
    print('your age is greater')
else:
    print('Your friend age is greater')