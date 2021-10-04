n = int(input("Type the number you want to find the factorial for: "))
val = 1

for i in range(1,n+1):
  val *= i
  
print("Factorial {} is {}".format(n, val))
