# Volatile memory Data persist temporarily like RAM
# Non-Volatile is used to store Daa Permanently like HDD
 
# Types of File 
# 1) Text Files (.txt , .py etc)
# 2) Binary Files () 



# f = open("File.txt")           # open is a built in function in python which help to open file in python. In open there is mode also exist which help you to set the mod of file like write but  by default it will be read represent by "r" you can write mode in the same line of write file name and then give [ , to write mode "w"]  like this


# data = f.read()        # read is a built in function in python which help to read file in python.


# print(data)


# f.close()               # close is a built in function in python which help to close file in python. Which is very important.



# Now Learn How to write in file in python


# str = "Hey Krishna You are Awesome"
# f = open("myfile.txt" , "w")
# f.write(str)
# f.close()



# Now Learn How to append mode in file in python 
# It mainly add your written content to the  end of that file

# str = "Hey Krishna You are Awesome"
# f = open("myfile.txt" , "a")
# f.write(str)
# f.close()



# more functions in file are :-
# 1) readlines      It makes a [list] of every line
# f = open("File.txt")
# lines = f.readlines()
# print(lines , type(lines))
# f.close()


# 2) readline       It reads every line one by one depend how many times it call but at a time it read only a single first line.
# f = open("File.txt")
# lines1 = f.readline()
# lines2 = f.readline()
# lines3 = f.readline()
# print(lines1 , type(lines1), lines2 , type(lines2),lines3 , type(lines3))
# while(lines1 != ""):
#     print(lines1 )
#     lines1 = f.readline()

# f.close()


# With Statement in  python

# str = "Hey Krishna You are Awesome" 
# f = open("myfile.txt" )       # This code with simple way
# f.read()
# f.close()


# with open("File.txt") as f:      # This code with [With] Statement Now you don't need to close manually the file
    # print(f.read())




# Practice

# with open("myfile.txt") as f:
#     data = f.read()
#     if("krishna".lower() in data.lower() ):
#         print("This file contain name")
#     else:
#         print("This file not contain")
# u = int(input( "Enter that number - "))
def generate(y):
    for i in range (1 , 11):
        print(f"{y} X {i} = {i*y}")
        with open("Ch 9 Practice .txt" , "w") as f:
            data = f.read()
            data

for i in range (2 , 21):
    generate(i)