
def checkBit(number, pos): 
    if(number & (1 << (pos - 1))):          # for 1 based indexing
        return 1
    return 0


number = int(input("give the number: "))
pos = int(input("give position to find set bit: "))

if(checkBit(number, pos)):
    print("yes it is set bit")
else: 
    print("no this bit is not set")

