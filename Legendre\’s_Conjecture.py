# Python program to verify Legendre\'s Conjecture
# for a given n
  
import math 
  
def isprime( n ):
      
    i = 2
    for i in range (2, int((math.sqrt(n)+1))):
        if n%i == 0:
            return False
    return True
      
def LegendreConjecture( n ):
    print ( "Primes in the range ", n*n
            , " and ", (n+1)*(n+1)
            , " are:" )
              
      
    for i in range (n*n, (((n+1)*(n+1))+1)):
        if(isprime(i)):
            print (i)
              
n = 50
LegendreConjecture(n)
