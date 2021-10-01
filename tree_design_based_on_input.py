def tree(a=5):
    for i in range(a):
        print('\n')
        for k in range(a-i) :
                if (i-a<=0):
                    print('', end =" "),
        for j in range(-i,i+1):
            #print(j, end =" ")
            if (j==0):
                print('|', end =""),
            elif (((j!=-i and j!=i+1) and i-j!=0) and (j==1 or j==-1) ):
                print('#', end ="")
            elif (((j!=-i and j!=i+1) and i-j!=0) and (j==2 or j==-2) ):
                print('$', end ="")
            elif (((j!=-i and j!=i+1) and i-j!=0) and (j==3 or j==-3) ):
                print('o', end ="")
            else :
                print('*', end =""),
    return 0            
