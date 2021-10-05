def fibonacci(number):
    """
    

    Parameters
    ----------
    number : a positive integer

    Returns
    -------
    True if a number is in the fibonacci
    sequence and False if otherwise. It
    returns Wrong input if number is negative
    and Invalid if input isn't an integer.

    """
    
    if isinstance(number,int) == True:       #test for integers
        if number < 0:                       #test for -ve integers
            return "Wrong Input"
        elif number > 0:                     #test for +ve integers
            a = [1,2]       #create list
            b = 1
            c = 2
            
            for i in range(1,number+1):     #create list of fib numbers
                d = b + c 
                a.append(d)
                b = c 
                c = d
            a = a[:-2]                  #to delete the last two elements
                                        #in the list
            if number in a:
                return "True"
            else:
                return "False"
    elif isinstance(number,int) == False:       #test for non-integers
        return "Invalid"
   
           
print(fibonacci(2))
print(fibonacci(-5))
print(fibonacci(['a']))