'''
Assignment Operators

=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3 print(x)
'''

# The Walrus Operator 

ages = [10, 21, 31]
numberOfAges = leng(ages)
if (numberOfAges := len(ages)) > 1: 
    print(f"List is too long with {numberOfAges} elements.")

'''
Ternary Operator
'''
myAge = 20
eligibleForVoting = "Eligible for voting" if myAge>=18 else "Not eligible for voting"

# Multiple if else statements 
eligibleFortVoting1 = "Eligible" if myAge>18 else "Exact match " if myAge == 18 else "Not eligible for voting"

'''
Logical operators
'''
# And operator 

isMale = True 
isLegalAge = True 

if isMale and isLegalAge:
    print("You are a male and you are of legal age")
else:
    print("You are either not a male or you are not of legal age")

# Or operator 
if isMale or isLegalAge:
    print("You are either a male or you are of legal age")
else:
    print("You are neither a male nor you are of legal age")

if not isMale:
    print("You are not a male")
else:
    print("You are a male")

'''
Identity operators
'''
x = [1,2,3] # 3000 
y = [1,2,3] # 4000 
z = x  # 3000
print(x is y)
print(x is z)
print("Testing is Not", x is not y)


# Difference between == and is operator 
print("== Check", x == y)  # This will print True because the values are equal


'''
Membership operators 
'''

names = ["Supreme", "Kesh", "Meghan"]
print("Is Kesh in names", "Kesh" in names)
print("Is Tom in names", "Tom" not in names)


'''
Operator Precedence 
'''
print(100 + 5 * 3)
