print('Hello, World!')

print(50+6)
print(50/6)
print(2**6) #power
height=10
width=20
area=height*width
print(area)

print(10.04*2*5) # There is full support for floating point; operators with mixed type operands convert the integer operand to floating point


'''
bill = float(input("Enter the bill amount: "))
tip_percent = int(input("Enter the tip percentage: "))
people = int(input("Enter the number of people: "))

tip_amount = bill * tip_percent / 100
total = bill + tip_amount
per_person = total / people

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total with tip: ${total:.2f}")
print(f"Amount per person: ${per_person:.2f}")
'''

## Time converter   

no_of_seconds = int(input("Enter the number of seconds: "))
print(f"Total seconds: {no_of_seconds}")

hours = no_of_seconds // 3600
remaining = no_of_seconds % 3600      # what's left after taking out the hours

minutes = remaining // 60
seconds = remaining % 60

print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")