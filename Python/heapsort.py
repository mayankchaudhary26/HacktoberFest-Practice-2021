#getting heap elements using bottom up approach

def heapBottomUp(l): #bottom uping the heap
 n=len(l)-1
 for i in range(n//2,0,-1):
  k=i
  v=l[k]
  heap=False
  while(not heap and 2*k<=n):
   j=2*k
   if(j<n):
    if(l[j]<l[j+1]):
     j=j+1
   if (v>=l[j]):
    heap=True
   else:
    l[k]=l[j]
    k=j
  l[k]=v
 return l

def heapSort(l): #sort the heap in ascending order
 s=[]
 for i in range(len(l)-1):
  s.insert(0,l[1])
  l[1]=l[-1]
  l=l[:-1]
  l=heapBottomUp(l)
 return s

def main():
 l=['#']   #element at index zero is not used
 n=eval(input("Enter the total number of elements\n"))
 print("Enter the elements:")
 for i in range(n):
  l.append(eval(input()))    #all elements got as input
 l=heapBottomUp(l)
 s=heapSort(l)
 print("\nAfter Sorting\n",s)

main()