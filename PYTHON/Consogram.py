p=input().lower()
t=0
a='bcdfghjklmnpqrstvwxyz'
def c(a,p,t):
    for i in range(21):
        if a[i] in p:
            t=t+1
    if t==21:
        return('Consogram')
    else:
        return('Not consogram')
k=c(a,p,t)
print(k)
