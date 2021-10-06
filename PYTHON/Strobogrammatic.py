def strobogrammatic(num):
    dict = {0 : 0, 1 : 1, 6 : 9, 9 : 6, 8 : 8}
    newNum = ""
    for i in num:
        if dict.get(int(i)) == None:
            newNum = ""
            print("Not strobogrammatic")
            break
        else:
            newNum += str(dict.get(int(i)))
    print("Strobogrammatic!")


num = input("Input number ")
strobogrammatic(num)