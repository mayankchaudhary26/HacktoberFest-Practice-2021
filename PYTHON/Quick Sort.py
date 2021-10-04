def partition(a,l,r):
 p=a[l]
 i=l
 j=r+1
 while True:
  while True:   #i      or while i < j-1: for worst case input error
   i=i+1
   if a[i] >= p:
    break
  while True:   #j
   j=j-1
   if a[j] <= p:
    break
  a[i] , a[j] = a[j] , a[i] #swap i,j
  print(a)
  if i >= j:
   break
 a[i] , a[j] = a[j] , a[i]  #reswap i,j
 print(a)
 a[l] , a[j] = a[j] , a[l]  #swap pivot,j
 print(a)
 return j

def quickSort(a,l,r):
 if l < r:
  s= partition(a,l,r)
  quickSort(a,l,s-1)
  quickSort(a,s+1,r)
  
def main():
 a=[]
 n=eval(input("Enter the number of elements in array : "))
 print("Enter the numbers : ")
 for i in range (n):
  a.append(eval(input()))
 print(a)
 quickSort(a,0,n-1)
 print(a)

main()
