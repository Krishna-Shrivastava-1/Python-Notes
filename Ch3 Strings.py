# String Slicing in python

# name = "Krishna" 
# shortname = name[0:3]
# print(shortname)
# Character1 = name[1]
# print(Character1)
# print(name[:6])

#Slicing With Skip value
# a = "Krishna" # First Resolve 1:5 and then take Jump according to that given number
# print(a[1:5:2])

# Functions of string
# 1) Length Function in String
# name = "Krishna is the"
# print(len(name))

# 2) endswith It will is it is end with "a"
# print(name.endswith("a"))

# 3) startswith It will is it is start with "K"
# print(name.startswith("K"))


# 4) Capitalize Its only capitalize the first letter of the first word in string
# print(name.capitalize())

# 5) Upper Its only UpperCase the whole words of string in capital letter
# print(name.upper())

# 6) Lower Its only LowerCase the whole words of string in capital letter
# print(name.lower())

# 7) Title Its only capitalize the first letter of the every word after spacing in string
# print(name.title())

# 7) Find Its only Find the first occurrence of the  word in string
# print(name.find("i"))

# 8) Replace Its only Replace the word from your desired  word in string
#First write old word after comma , Write that word which you want their after replace
# print(name.replace("the" , "Koga"))

# Escape Sequence Characters [For Printing  a New Line In String with this backslashn "\n" for new line , backslasht "\t" for tab space on that line]
# a ="""Krishna is \n\ta good "Boy" """
# print(a)

# Practice
# a = input("Enter your name - ")
# print("Good Evening", a) #Way of writing 1
# print(f"Good Evening  {a} ")   #Way of writing 2 by writng f means marking as a f string so that you can use variables in between strings
# print("Good Evening "+ a ) #Way of writing 3 The Concatenation

# Letter to Fill Name and Date
# letter = '''Dear, |Name|
# You  are Selected
# |Date|         '''
# print(letter.replace("|Name|" , "Krishna").replace("|Date|" ," 17/06/24"))


# Detect Double space [If By Chance it will not get any term which you have said to find in the parent string or double space in our case then it will return "-1" means that term is not exist in our parent string OR If it will get then return index number]
# name = "Krishna is a  Good Boy"
# print(name.find('  '))

# name = "Krishna is a  Good Boy"  # Replacing double space by single space by relace method [name string which is original that will not change by executing any function]
# print(name.replace(('  '), (" ")))
# print(name)

# letter = "Dear Krishna ,\n\tYour Python  Code Notes , Comments and Source Code are Amazing.\nThanks!"
# print(letter)


# import random
# a = int(random.random() * 100)
# print(a)
