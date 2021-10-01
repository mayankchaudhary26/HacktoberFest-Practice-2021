l1 = []
l2 = []
n = int(input("Enter student count:"))
for i in range(n):
    aa = input("Enter the name of student :")
    l1.append(aa)
    bb = int(input("Enter Regno. :"))
    l2.append(bb)
for i in range(n-1):
    for j in range(i+1,n):
        if(i[i]>i[j]):
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
            temp2=l2[i]
            l2[i]=l2[j]
            l2[j]=temp2

for i in range(n):
    print(l1[i],",",l2[i])



