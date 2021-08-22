# This is my first python program!
print("Welcome to python world!\n\n")
num1 = input("Please enter the first number!: \n")
print("num1", id(num1), type(num1), num1)
num1 = int(num1)
print("num1", id(num1), type(num1), num1)
num2 = input("Please enter the secomd number!: \n")
num2 = int(num2)

sum = num1 + num2
print("The sum is:" ,sum)

x = num1 / num2
print("division results:" , x)

y = num1 % num2
print("The result of Y is:", y)

# String format in python
print ("Welcome To Python!")
print('Welcome To\
 Python!')
print("Welcome \"To\" python")
print(""" python is a power full programming language as Java,
 C++ and it is invented by Gudio's """)

number1 = 5132
print("Number1", number1)
print("Decimal Integer %d" %number1)
print("Hexadecimal Integer %x" %number1)

#Testing if structures in python
if num1 == num2:
#print("%d is equal to %d" %(num1,num2))
 print("equal")
 
if num1 >= 79:
  print(num1, " is greater than 79")