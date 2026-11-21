'''
Variables 
Variables are containers for storing data values.
''' 

age = 21
name = "Sam" 

# Guess the type of the variable age and name?

# If you didn't explicitly specify the data type, you can provide different value too.
age = "Sam"

# Casting 
int_example = int(55.5)
float_example = float(55.5)
string_example = str('55.5') # String can be created by using single or double quotes.

# Guess the output of the following code snippet?
print(int_example)

print(float_example)
print(string_example)

print(int_example + float_example)
#print(int_example + string_example)

# Guess 
# below examples are same or different?
small = 6
Small = 7 

print(type(small))


# Multi Words Variable Names
# Camel Case 
camelCaseAdd = "camel case" # FE languages
# Pascal Case
PascalCaseAdd = "Pascal case" # we don't 
# Snake Case
snake_case = "snake case" # Major 



# Many Values to Multiple Variables
example_1, example_2, example_3 = "value 1", "value 2", "value 3"

# One Value to Multiple Variables
example_4 = example_5 = "orange"


# Unpack a Collection 
student_name, student_age = ["Sam", 21]
print(student_name)
print(student_age)

# Guess the type of below type
english_mark, hidi_mark, cs_mark = (85, 90, 95)

total_marks = english_mark + hidi_mark + cs_mark 
english_mark, hidi_mark, cs_mark = 85, 90, 95
print(english_mark, hidi_mark, cs_mark, total_marks)


# Python - Global Variables 
# Difference between local and global variables

global_variable = "I am a global variable"

def global_function_example():
    global_variable = "I am a local variable"
    print(global_variable)

global_function_example()
print(global_variable)


global_variabl_1 = "I am a global variable"

def global_function_example1():
    global global_variabl_1
    global_variabl_1 = "I am a local variable"
    print(global_variabl_1)

global_function_example1()
print(global_variabl_1)

# no cha