def Bcalculator(num1,num2):
    """
    Parameters
    ----------
    num1 : String binary
    num2 : String binary

    Returns
    -------
    summation of the decimal
    values of num1 and num 2
    using the bn(num) function
    """
    return bn(num1) + bn(num2)

def bn(num):
    """
    Parameters
    ----------
    num : String binary

    Returns
    -------
    d : Decimal value of num

    """
    """"
    code below to check if string is binary
    """
    p = set(num) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        pass
    else : 
        assert False
    """"
    code below to convert string to decimal
    """
    b = len(num)
    e = int(b) -1 
    a = d = 0
    while b != 0:
        c = int(num[a])*(2**e)
        d, a =  d+c , a+1
        b, e = b-1, e-1
    return d
    

print(Bcalculator("10","10"))
print(Bcalculator("101","10"))
