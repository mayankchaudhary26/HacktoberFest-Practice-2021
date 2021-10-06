def uncensor(a,b):          #function definition
    """
    
    Parameters
    ----------
    a : Sensored String
    b : String containing the 
    missing vowels according to 
    the sequence of removal
 
    Returns
    -------
    The uncensored string
 
    """
    if isinstance(a,str) and isinstance(b,str):     #datatype testing
        c = 0
        d = 0
        for i in a:             #test for elements in a
            if i == "*":        #test for elements to be replaced
                a = a.replace(a[d],b[c],1)          #replace elements "*" 
                c += 1
            d += 1
        return a 
    else:
        return "Invalid Input"
    
print(uncensor("Wh*r* d*d my v*w*ls g*","eeioeo"))
print(uncensor("*lw*ys w*tch th* c*s*s","Aaaeae"))
print(uncensor("dry cry",""))