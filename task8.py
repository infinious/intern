
#1
Elements = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    X = int(input())
    Elements.append(X)
print(Elements)
for C in Elements:
    print ("List Element After Adding +2:", C +2)

#2
n = int(input('Enter number: '))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end="")
    print()

#3
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Sequence: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

  # 4
  num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

    # 5
num = 9
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

# 6
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
else:
    print("Negative number")

# 7
days = int(input("Enter the days:"))
years = days / 365
print("Number of years is:", years)

# 8
import math

a = math.cos(0) + math.sin(90) + math.tan(45)
print(a)

# 9
print("1-Add")
print("2-Substract")
print("3-Multiply")
print("4-Divide")
print("5-Modulus")
print("6-Exit")

n = int(input("Enter the option(1-6):"))
while n > 0:
    if n == 1:
        a = int(input("Enter the 1st value:"))
        b = int(input("Enter the 2nd value:"))
        print("Addition of two numbers:", a + b)
    elif n == 2:
        a = int(input("Enter the 1st value:"))
        b = int(input("Enter the 2nd value:"))
        print("Subtraction of two numbers:", a - b)
    elif n == 3:
        a = int(input("Enter the 1st value:"))
        b = int(input("Enter the 2nd value:"))
        print("Multiplication of two numbers:", a * b)
    elif n == 4:
        a = int(input("Enter the 1st value:"))
        b = int(input("Enter the 2nd value:"))
        print("Division of two numbers:", a // b)
    elif n == 5:
        a = int(input("Enter the 1st value:"))
        b = int(input("Enter the 2nd value:"))
        print("Modulus of two numbers:", a % b)
    elif n == 6:
        exit()
    else:
        print("Invalid Operation")
    n = int(input())

