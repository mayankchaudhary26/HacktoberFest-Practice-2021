def booths(mcand, plier):

    product= "0000000000000000" + plier + "0"
    
    print()
    print("first number: " + mcand + "  second number: " + plier)
    print()
    print("    #         ACCUMULATOR       MULTIPLIER            OPERATION")
    print()

    for i in range(0,15,2):
        
        a,s = perform_operation(product,mcand,product[len(product)-2:])
        
        if i<10:
            print("Step: " + "0" + str(i) + "      " + product[0:16] + "  " + product[16:32]  +" " + product[32] + "    " + s)
        else:
            print("Step: " + str(i) + "      " + product[0:16] + "  " + product[16:32]  +" " + product[32] + "    " + s)
        
        b,s = perform_operation(a,mcand,a[len(a)-2:])
        
        if (i+1)<10:
            print("Step: " + "0" + str(i+1) + "      " + a[0:16] + "  " + a[16:32]  +" " + a[32] + "    " + s)
        else:
            print("Step: " + str(i+1) + "      " + a[0:16] + "  " + a[16:32]  +" " + a[32] + "    " + s)

        product=b

    print("Step: " + "1" + str(6) + "      " + product[0:16] + "  " + product[16:32]  +" " + product[32])
    print()
    
    return shift(product)[17:33]


def perform_operation(product,mcand,operation):
    
    if operation == "00" or operation == "11":
        return shift(product),"Arithmetic Shift Right(ASR)"
    
    elif operation == "01":
        product = Add(product[0:16],mcand) + product[16:]
        product = shift(product)
        return product,"Add(A->A+M) then Arithmetic Shift Right(ASR)"
    
    elif operation == "10":
        product = subtraction(product,mcand)
        product = shift(product)
        return product,"Subtract(A->A-M) then Arithmetic Shift Right(ASR) "


def subtraction(product,mcand):
    
    carry = "0"
    final_product = ""
    
    for i in range(len(product[:16])-1,-1,-1):
        
        if mcand[i] == "0" and product[:16][i] == "0" and carry == "1":
            final_product = "1" + final_product
        elif mcand[i] == "0" and product[:16][i] == "0" and carry == "0":
            final_product = "0" + final_product
        elif mcand[i] == "1" and product[:16][i] == "0" and carry == "1":
            final_product = "0" + final_product
        elif mcand[i] == "1" and product[:16][i] == "0" and carry == "0":
            final_product = "1" + final_product
            carry = "1"
        elif mcand[i] == "0" and product[:16][i] == "1" and carry == "1":
            final_product = "0" + final_product
            carry = "0"
        elif mcand[i] == "0" and product[:16][i] == "1" and carry == "0":
            final_product = "1" + final_product
        elif mcand[i] == "1" and product[:16][i] == "1" and carry == "1":
            final_product = "1" + final_product
            carry = "1"
        elif mcand[i] == "1" and product[:16][i] == "1" and carry == "0":
            final_product = "0" + final_product

    return final_product + product[16:]


def shift(product):
    
    return "0"+product[:len(product)-1]


def Add(num, num2):
    
    product = ""
    carry = 0
    
    for i in range(len(num)-1,-1,-1):
        
        if num[i]=="0" and num2[i]=="0" and carry==0:
            product="0"+product
            carry=0
        elif num[i]=="0" and num2[i]=="0" and carry==1:
            product="1"+product
            carry=0
        elif num[i]=="1" and num2[i]=="1" and carry==0:
            product="0"+product
            carry=1
        elif num[i]=="1" and num2[i]=="1" and carry==1:
            product="1"+product
            carry=1
        elif num[i]=="1" and num2[i]=="0" and carry==0:
            product="1"+product
            carry=0
        elif num[i]=="0" and num2[i]=="1" and carry==0:
            product="1"+product
            carry=0
        elif num[i]=="1" and num2[i]=="0" and carry==1:
            product="0"+product
            carry=1
        elif num[i]=="0" and num2[i]=="1" and carry==1:
            product="0"+product
            carry=1
    
    return product


def positiveBinaryConversion(n):

    l = [n]
    b = []

    while n > 1:
        n = n//2
        l.append(n)
    
    for i in l[::-1]:
        b.append(str(i%2))
    
    while len(b) < 16:
        b.insert(0,"0")
    
    s=""

    for i in b:
        s+=i

    return s


def twoscompliment(n):
    
    a = (n^65535) + 1
    return bin(a)[3:]


def binToDec(string):

    value= 0
    string=string[::-1]

    for i in range(len(string)):
        if string[i]=="1":
            value= value+(2**i)

    return str(value)


n1 = input("Enter multiplicand: ")
n2 = input("Enter multiplier: ")

if int(n1)>=0:
    num1=positiveBinaryConversion(int(n1))
else:
    num1=twoscompliment(int(n1))

if int(n2)>=0:
    num2=positiveBinaryConversion(int(n2))
else:
    num2=twoscompliment(int(n2))

result_binary = booths(num1, num2)

print("Answer in binary form: " + result_binary)
print()
print("Answer in decimal form: " + binToDec(result_binary))