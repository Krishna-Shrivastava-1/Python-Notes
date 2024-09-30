# These are also collection of data to store data
#Dictionary Allows you in python to store data in key value pairs and it's Synatx for decalring a ditionary is [a = { enter key and values here , and more }]. In this you can directly type the key to get the value
# marks = {
#     "Krishna":100,
#     "Harry" : 99,
#     "Honey Singh" : 40,
#     "list":[1,2,3],
#     0 : "hello"
# }

# print(len(marks))  # With len you can find length of dictionary
# marks = {} # Then it will be a empty dictionary
# print(marks)
# print(marks["Krishna"])
# print(marks["list"])
# print(type(marks))

# Properties of Python Dictionaries
# 1) It is unordered
# 2) It is mutable
# 3) It is indexed
# 4) Cannot contain duplicate keys

# Methods of Dictionary
# 1) .items [It returns all items in dictionary]
# print(marks.items())

# 2) .keys [It returns all keys in dictionary]
# print(marks.keys())

# 3) .value [It returns all values in dictionary]
# print(marks.values())

# 4) .update [It update the value of an particular key as you want Syntax [.update({"key" : "value"})] if the key is not exist then that key will be append at the last  in current dictionary]
# marks.update({"Krishna" : 99})
# print(marks)

# 5) .get [It returns that key value which you want to know if that key in dictionary is not exist then it will return none] ------->
# print(marks.get("Krishna"))
# print(marks["Krishna"])  # Unless If you write this and write a key which is not exist then it will return error so if you want to know a value of  a key then use [.get method]

# 6) .clear [It will empty your dictionary]
# print(marks.clear())

# 7) .copy [It will make a shallow copy of your dictionary]
# print(marks.copy())

# 8) .pop [It will remove the specified key from your dictionary]
# marks.pop("Krishna")
# print(marks)

# 9) .popitem [It will remove the last key and value from your dictionary]
# marks.popitem()
# print(marks)


# Sets it is a collection of well defined objects [In set only type values]
# s = {1,2,3,4,5,6,7}  # It is Set
# e = set()              # It creates empty set 
# print(type(e))
# z = {1,5,2,2,2,2,2,8,5,4} # Set type every value one time not matter how many times it writtened inside the set {It can't repeat elements}
# print(z)

# z = {1,5,2,"krishna",8,5,4}
# print(z)



# Properties of Set
# 1) Sets are unordered.
# 2) Sets are unindexed.
# 3) There is no way to change itme in sets.
# 4) Sets cannot contain duplicate values.

# Operations on Set
# 1) .len # [With len you can find length of set]
# z = {1,5,2,8,5}
# print(len(z)) 


# 2) .remove # [With remove you can remove any value of set]
# z = {1,5,2,8,5}
# z.remove(5)
# print(z) 

# 3) .union # [With union you can unite  values of two different set without any repeatation of same value]
# z1 = {1,5,2,8,5}
# z2 = {8,7,3,6}
# print(z1.union(z2)) 

# 3) .intersection # [With intersection you can take same values of two different sets which are same without any repeatation of same value]
# z1 = {1,5,2,8,5}
# z2 = {8,7,3,6}
# print(z1.intersection(z2)) 

# 4) .subset [It's help to know that value is the subset of that set or not it return true and false]
# z = {1,5,2,8,5}
# print({1,5}.issubset(z))



# Methods of Sets
# z = {1,5,2,8,5,4}
# 1)  .add [ It appends or add your given value in the set ]
# z.add("krishna" )
# z.add(52)
# print(z)

# 2)  .clear [ It empty your set ]
# z.clear()
# print(z)

# 3)  .copy [ It will make a shallow copy of your set ]
# z.copy()
# print(z)


#  4)  .discard [ It will remove that key from your set which you want ]
# z.discard(5)
# print(z)



# Practice

# words = {"billi" : "cat", 
#          "kitaab" : "book", 
#          "chalna" : "walk", 
#          "bhaagna" : "run"}
# word = input("Enter your word - ")
# print(words.get(word))


# s = set()
# n = int(input("Enter number 1 - "))
# s.add(n)
# n = int(input("Enter number 2 - "))
# s.add(n)
# n = int(input("Enter number 3 - "))
# s.add(n)
# n = int(input("Enter number 4 - "))
# s.add(n)
# n = int(input("Enter number 5 - "))
# s.add(n)
# n = int(input("Enter number 6 - "))
# s.add(n)
# n = int(input("Enter number 7 - "))
# s.add(n)
# n = int(input("Enter number 8 - "))
# s.add(n)
# print(s)




# e = set()
# e.add("18")
# e.add(18)
# print(e)




# e = set()
# e.add(20)
# e.add(20.0)
# e.add("20.0")
# print(len(e))               #Because if the values are equal then data type is not matter means it can be an integer or  a floating point number if value is same then in python it will return true.



# d = {}
# name = input("Enter your name - ")
# lang  = input("Enter your language - ")
# d.update({name:lang})

# name = input("Enter your name - ")
# lang  = input("Enter your language - ")
# d.update({name:lang})

# name = input("Enter your name - ")
# lang  = input("Enter your language - ")
# d.update({name:lang})

# name = input("Enter your name - ")
# lang  = input("Enter your language - ")
# d.update({name:lang})
# print(d)


