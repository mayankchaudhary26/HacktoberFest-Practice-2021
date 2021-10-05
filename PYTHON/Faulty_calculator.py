#faulty calculator
# program for faulty calcultor using function .
print("This program is developed by Gaurang Manchekar")
op=(input(" Please type in the math opertion you would like to complete :\n+ for addition\n- for subtarction\n* for multipliction\n/  for division\n% for modulo\nenter your choice opertor :"))
num1=int(input("Please enter num1 :="))
num2=int(input("Please enter num2 :="))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modules(a,b):
    return a%b
if op=='+':
    if num1==56 and num2==9:
        print(f"Your result {num1}{op}{num2} is :",77)
    else:
        print(f"Your result {num1}{op}{num2} is :",add(num1,num2))
elif op=="-":
    print(f"Your result {num1}{op}{num2} is :",sub(num1,num2))
elif op=="*":
    if num1==45 and num2==3:
        print(f"Your result {num1}{op}{num2} is :",555)
    else:
        print(f"Your result {num1}{op}{num2} is :",mul(num1,num2)) 
elif op=="/":
    if num1==56 and num2==6:
        print(f"Your result {num1}{op}{num2} is :",4)
    else:
        print(f"Your result {num1}{op}{num2} is :",div(num1,num2))
elif op=="%":
    print(f"Your result {num1}{op}{num2} is :",modules(num1,num2))  
else:
    print("Invalid opertion Please choose valid opertor")