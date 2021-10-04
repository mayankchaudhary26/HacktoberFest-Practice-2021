n =int(input("Enter a number: "))
 
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
    k = 1
    for j in range(1, i+1):
        print(' ', k, sep='', end='')
        k = k * (i - j) // j
    print()