#Introduction to python

#Data Types
x = 3
print(type(x))                   # Int Datatype

Y = "Hello"
print(type(Y))                   # String Datatype

height = 234.32
print(type(height))              # Float Datatype

Result = True
print(type(Result))              # Boolean Datatype

# Multiple Assignment

Name,Age,Class = 'Raj',14,9
print(Name,Age,Class)

# User Input and Type Casting

'''Name = input("Enter your name: ")
print(Name)

Age = int(input("Enter your age: "))   # Int converts String into  an Integer value
print(Age)

Weight = float(input("Enter your weight: "))   # float converts String into Float value
print(Weight)

Class = eval(input("Enter the class: "))     # eval converts String into yhe corresponding Datatype of the value
print(Class)'''

# Math functions 
import math

x = 8.314

print(math.ceil(x))
print(round(x))
print(math.floor(x))
print(pow(2,3))
print(math.factorial(5))

# String 

S = "Umbrella"
print(S)

# String slicing

print(S[1:6:1])

print(S[::-1])            # It reverses the string

# List

Fruits = ['Mango','Apple','Banana','Orange']
print(Fruits)
 
# Indexing of the list

print(Fruits[2])

print()

for i in Fruits:
    print(i)

print(Fruits[::2])               # Slicing in Lists

Fruits.append('Watermelon')         # Adding new element
print(Fruits)
print()

Fruits.insert(5,'Papaya')        # Using insert element
print(Fruits)
print()

Vegetables = ['Potato','Onion','Tomato','Carrot']

Grocery = Fruits + Vegetables
print(Grocery)
print()

# Tuples
 
t1 = ('Apple','Banana','Ice cream','Chocolate')
print(type(t1))
print()

# Sets

A = {'Ice cream','Waffle','Chocolate','Ice cream','Puding'}

print(A)
print(type(A))

#-------------------------------------------------
# If statements 

Age = eval(input('Enter the Age: '))
if Age>18 :
    print("You are eligible  to vote")

else :
    print("You are not eligible to vote")
print()    
 #-------------------------------------------------
 # Use of if elif and else conditions and logical operators   

Age = eval(input("Enter your age: "))
if Age<=13:
    print("You are a child")

elif (Age>13 and Age<18):
    print("You are a teenager")

elif (Age>=18 and Age<60):
    print("You are an adult")  

else :
    print("You are a senior citizen")

#----------------------------------------------------
 
# Loops 

x = 1
while x < 11:                            # It displays numbers from 1 to 10
    print(x)
    x+=1
print()

list = ['Apple','Banana','Mango','Cherry']
for x in list:
    print(x)
print()  

# Conditional statements

x = 0
while x < 10:
    print(x)                               # break is used to terminate the execution
    x+=1
    if x == 5:
        break
print()

#----------------------------------------

i = 0
while i < 10:
    print(i)                               #it continues the execution
    i+=1
    if i == 5:
        continue
print()    
        
#---------------------------------------
# Dictionary

dict = {'Punjab':'Chandigarh','Maharashtra':'Mumbai','Gujrat':'Ahemdabad'}
print(dict)
print()
print(type(dict))
print()        

print(dict.keys())
print(dict.items())

print(dict['Punjab'])


# functions

def multiply(num1,num2):
    result = num1*num2
    return result

print(multiply(2,3))

#---------------------------------------------

def simple_interest(P,R,T):
    result = (P*R*T)/100
    return result

P = eval(input("Enter the Principal: "))
R = eval(input("Enter the Rate: "))
T = eval(input("Enter the Time:  "))

SI = simple_interest(P,R,T)
print('Simple Interest is ',SI)


#----------------------------------------------
# random module

import random
a = random.randint(1,11)
print(a)
print()

Choice = ['Head','Tail']
Toss = random.choice(Choice)
print(Toss)


