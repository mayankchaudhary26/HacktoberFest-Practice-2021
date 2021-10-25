W= 50
N= 3
v=[[60,10],[100,20],[120,30]] #v:w
def fk(w,n,v):
    for i in range(n):
        v[i].append(v[i][1]/v[i][0])
    v.sort(key=lambda x: x[2])
    #print(v)
    i=0
    j=0
    a=0
    while j + v[i][1] <w and i<n:
        j+=v[i][1]
        
        a+=v[i][0]
        i+=1
    
    #print(j,i,a)
    d=w-j
    if i <= n:
        #print(v[i])
        a+=((d * v[i][0]) / v[i][1])
    print(a)
fk(W,N,v)
