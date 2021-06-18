#2
def covid(patient_name,body_temperature=98):
    print("patien name is",patient_name)
    print("body temperature is",body_temperature)

a = input("enter patient name:")
b = input("enter body temperature")
covid(a,b)
#1
def y(c,d):
    print("ADDITION=",c+d)
    print("SUBTRACTION=",c-d)
    print("MULTIPLICATION=",c*d)
    print("DIVISON=",c//d)
c = int(input("enter the first number:"))
d = int(input("enter the second number:"))
y(c,d)