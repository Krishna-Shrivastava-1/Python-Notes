# List are generally use to store similar data type or different types of data type but only use to store in a variable just like creating array in JS but, In Python it is known as Lists

# friends = ["apple" , "Orange" , 7 , 78.5 ,False , "Krishna"]
# friends[0] = "Grapes"
# friends[1] = "banana" 

# # Lists Are Mutable and can be changed these are not like strings which are immutable. In Another Words we can say if you run any function in list then it will change the list actual original list unlike creating an replica of it and run your desired function seperately on it that's why list are mutable 
# {you can change original data} 

# but in string methods where a new string is formed and the original string is not change because strings are immutable {you cannot change original data}
# print(friends[0:4])

# Methods of Lists
# friends = ["apple" , "Orange" , 7 , 78.5 ,False , "Krishna"]
# print(friends)

# 1) .append [Its insert a new data in the array at the last]
# friends.append("Mafia")
# print(friends)

# 2) .sort [Its sort the list in increasing order]
# l1 = [25,55,12,36,47,1,58,5655,112,8,9]
# l1.sort()
# print(l1)

# 3) .reverse [Its reverse the list from end]
# l1 = [25,55,12,36,47,1,58,5655,112,8,9]
# l1.reverse()
# print(l1)

# 4) .insert [Its insert the item or data whichever you want to insert at the middle or any index place whichever you want . For this write index and then which item you want to insert]
# l1 = [25,55,12,36,47,1,58,5655,112,8,9]
# l1.insert(3 , 24 )
# print(l1)

# 5) .pop [Its delete the value or item which you want at a particular index to delete]
# l1 = [25,55,12,36,47,1,58,5655,112,8,9]
# l1.pop(0)
# print(l1)

# 6) .remove [Its remove the value or item directly by writing that value unless writing it's index and whenever the first occurence is come of that value it will be removed]
# l1 = [25,55,12,36,47,1,58,5655,112,8,9]
# l1.remove(1)
# print(l1)



# Tuples {These are also like list but these are immutable not like list which is mutable and these are build by "()" parenthesis}


# a = (1,2,3,"Orange" , 7 , 78.5 ,False , "Krishna") # Normal Simple Tuple
# a[0] = "Visual Studio Code" #It can't be change
# print(a)
# print(type(a))

# a = () # For Empty Tuple
# print(type(a))

# a = (1,) # For Single item Tuple
# print(type(a))

# Methods of Tuple

# 1) .count [If you write an item which is in your tuple then .count  count how many times that item is come in your tuple]
# a = (1,2,3,"Orange" , 7 , 78.5 ,False , "Krishna" , 3 , 3 , 3)
# print(a.count(3))

# 2) .index [If you write an item which is in your tuple then .index  indexes  that item  in your tuple and give the index number for the first occurence]
# a = (1,2,3,"Orange" , 7 , 78.5 ,False , "Krishna" , 3 , 3 , 3)
# print(a.index(3))


# Practice
# fruits = []
# f1 = input("Enter Your Fruits Name - ")
# fruits.append(f1)
# f2 = input("Enter Your Fruits Name - ")
# fruits.append(f2)
# f3 = input("Enter Your Fruits Name - ")
# fruits.append(f3)
# f4 = input("Enter Your Fruits Name - ")
# fruits.append(f4)
# f5 = input("Enter Your Fruits Name - ")
# fruits.append(f5)
# f6 = input("Enter Your Fruits Name - ")
# fruits.append(f6)
# f7 = input("Enter Your Fruits Name - ")
# fruits.append(f7)

# print(fruits)

# Marks = []
# f1 =   int(input("Enter Your Marks - "))
# Marks.append(f1)
# f2 = int( input("Enter Your Marks - "))
# Marks.append(f2)
# f3 = int( input("Enter Your Marks - "))
# Marks.append(f3)
# f4 = int( input("Enter Your Marks - "))
# Marks.append(f4)
# f5 = int( input("Enter Your Marks - "))
# Marks.append(f5)
# f6 =int( input("Enter Your Marks - "))
# Marks.append(f6)
# Marks.sort()
# print(Marks)

# a = (45 , 12 ,"Krishna")
# a[2] = "Apple"
# print(a)


# l = [56, 45, 36, 4]
# print(sum(l)) 
# print(l[0] + l[1] + l[2])  # Another way to add


# a = (1,2,3,"Orange" , 7 , 78.5 ,False , "Krishna" , 3 , 3 , 3)
# print(a.count(3))

# s = 'Silly Python - 561'
# result = ''
# for char in s :
#     if (char == 'l'):
#         result += 'B'
#     elif(char .isalpha()):
#         result += char.upper()
#     elif (char .isdigit()):
#         result += str(int(char)+3)
#     else:
#         result += char

# print(result)


