# warmup that can be executed only as script, so read all the instruction first
# provide appropriate instruction to the user on the format of the input
# ensure the entire script runs, including all logic

import sys 

print(sys.argv)
print(type(sys.argv))
# 1 ask user to provide 5 words that can be used as variable name,

a = input("Word 1 ")
b = input("Word 2 ")
c = input("Word 3 ")
d = input("Word 4 ")
e = input("Word 5 ")

# 2 print the vaiable names provided by the user in earlier step

print(a, b, c, d, e)


# 3 Check if all the provided variable names are valid python variable names
# Extract those names, that are invalid into invalid_names list, print it
l1 = (a, b, c, d, e)

invalid_names = []

invalid_keywords = ["for", "else"]
# regex_special_char = 
# first_letter_int

for i in l1:
    if i in invalid_keywords:
        invalid_names.append(i)
print("Invalid inputs ", invalid_names)
# 4 Extract the variable names that are more than 4 chars into sep1, print it

sep1 = []

for i in l1:
    if len(i) > 4:
        sep1.append(i)
print("Variables greater than 4 chars ", sep1)
    

# 5 ask for the user one variable name, 


# 6 Make the script to continue asking for one more variable name, endlessly

# 7 After breaking from endless loop, now re-write the endless var name request
# with a break condition

# Inform user that, this script can accept command line arguments

# Implement simple logic to check if there is a command line argument

# parse the command line arguments provided by the user in to cli variable

# Implement Logic to check how many c-line args are provided, and ask user to provide minimum 5

# Do the 2 / 3 and 4 instruction above

