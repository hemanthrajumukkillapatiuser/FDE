'''
Strings 
'''

double_quotes_string = "This is double quotes string"
single_quotes_string = 'This is single quotes string'


# We can use single quotes inside double quotes and vice versa.
string_with_single_quotes = "This is a string with 'single quotes' inside"
string_with_double_quotes = 'This is a string with "double quotes" inside'

# Multi-line strings 
'''
This is a multi-line string
'''

# Strings are arrays in python, There are no character data type in python, a single character is simply a string with a length of 1.
# we can access the characters in a string using indexing, and we can also use slicing to get a substring from a string.
# negative indexing is also supported in python, where -1 is the last character, -2 is the second last character and so on.
print("First character", double_quotes_string[0])
print("Last character", double_quotes_string[-1])
print("Last character", double_quotes_string[-2])

# Looping through a string
for char in string_with_single_quotes:
    print(char)

# check length of string 
print("Length of single quotes string", len(single_quotes_string))


# check if substing is present in string
if 'Jeevan' in double_quotes_string:
    print("Yes, 'Jeevan' is present in the string")
else:
    print("No, 'Jeevan' is not present in the string")

# check if substring is not present in string
if 'Jeevan' not in double_quotes_string:
    print("Yes, 'Jeevan' is not present in the string") 
else:
    print("No, 'Jeevan' is present in the string")


'''
Slicing of string
'''
# with lower and upper bound 
lower_and_upper_bound = double_quotes_string[0:5]

# with higher bound only 
higher_bound = double_quotes_string[:5]

# with lower bound only 
lower_bound = double_quotes_string[5:]

'''
Modifying strings 
'''

# string lower case 
lower_case_string = double_quotes_string.lower() # home work  

upper_case_string = double_quotes_string.upper() # home work 

# remove whitespace from the beginning and end of the string
string_with_whitespace = "   This is a string with whitespace   ".strip() # home work 

# replace a substring with another substring
replaced_string = double_quotes_string.replace("double", "single") # home work 

# split a string into a list of substrings
split_string = double_quotes_string.split(" ") # You can use any deliminator to split the string, in this case we are using space as a deliminator.

# Concatination of strings
concatinated_string = "Jeevan" + " " + "Chandra"

'''
Format strings 
'''


# f strings introduced in python 3.6 
my_age = 25.5 
formatted_string = f"My name is jeevan and my age is {my_age}"

# Placeholder and modifiers 
formatted_string_modifiers = f"My name is jeevan and my age is {my_age: .2f}"


# Escaping characters in strings 
escaping_string = "String with quotes \"quote example\""

'''
String methods

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

'''