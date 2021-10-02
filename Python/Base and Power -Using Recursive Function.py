# This is Recursive Function Program to calculate the value of power with its base.
# Here the value of Power can be negative as well as possitive integer.
# Value of Power can not be in decimal or in fraction, it will raise the assertion error
# This will also work for decimal value of n(base)

n = float(input("Enter the Base number: "))
m = int(input("Enter the Power: "))


def power (n,m):

    if (m<0):   # For Negative interger of m value
        
        if(m==-1):   #Base structure to exit from Recursive Function
            return (1/n)
        
        else:    
            return (1/n * power(n,m+1)) # Recursive Function Calling
        
        
    else:   #For Possitive interger of m value
        
        if (m==0):   # Base structure to exit from Recursive Function
            return (1)
        else:
            return (n * power (n,(m-1))) # Recursive Function Calling

print(power(n,m)) # Calling of power function
