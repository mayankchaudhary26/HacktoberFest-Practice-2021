import math

def closestPairDistance(l):
 dist=9999
 for i in range(len(l)):
  for j in range(i+1,len(l)):
   dist=min(dist,CalcDist(l[i],l[j]))
 return dist

def CalcDist(a,b):
 return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

def main():
 n=eval(input("Enter number of points\n"))
 l=list()
 for i in range(n):
  x,y=eval(input("Enter the x and y coordinates\n"))
  l.append([x,y])
 dist=closestPairDistance(l)
 print("Closest Pair Distance is {0:.2f}".format(dist))

main()