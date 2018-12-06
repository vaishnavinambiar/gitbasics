#To call a function using python
def func1():
    print "Vaishnavi"
func1()

#To see how function returns a value
def cube(x):
    print(x*x*x)
print cube(4)
            #we can see none as output
def cube(x):
    return(x*x*x)
print cube(4)
            #since we have used return command we will not see 'none' in output

#To add,sub,mul & div using function

def add(x,y):
    print(x+y)
add(10,5)

def sub(x,y):
    print(x-y)
sub(10,5)

def mul(x,y):
    print(x*y)
mul(10,5)

def div(x,y):
    print(x/y)
div(10,5)

#Reversed the order of the value x and y to x=5 and y=10 
def mul(x,y=0):
    print "value of x=",x
    print "value of y=",y

    return x*y
print mul(y=10, x=5)

#Multiple Arguments passed as an array
def array(*args):
    print(args)
array(1,2,3,4,5,6,7,8,9)

#To use the absolute function
def absolute_value(num):   #This function returns the absolute value of the entered number
    if num >= 0:
        return num
    else:
        return -num
print absolute_value(2) #output will be 2
print absolute_value(-4) #output will be 4

#Working with if else statement
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
  #Odd or Even
num =input("Enter a number: ")
if num%2 == 0:
    print "Number is Even"
else:
    print "Number is Odd"
  #Code from LPTHW
def add(a, b):
    print "ADDING: %d+%d" % (a, b)
    return a + b
def subtract(a, b):
    print "SUBTRACTING: %d-%d" % (a, b)
    return a - b
def multiply(a, b):
    print "MULTIPLYING: %d*%d" % (a, b)
    return a * b
def divide(a, b):
    print "DIVIDING: %d/%d" % (a, b)
    return a / b
    print "Let's do some math with just functions!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

#Calculator
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
