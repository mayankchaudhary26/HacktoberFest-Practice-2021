a = int(input())
pizza = []
for i in range(a):
    pizzas = [int(input()),input(),int(input()),int(input())]
    pizza.append(pizzas)
pizza = sorted(pizza)
count = 0
first = 0
last = len(pizza)-1
found = False
code = int(input())
while first <= last and not found:
    midpoint = (first+last)//2
    count +=1
    if pizza[midpoint][0] == code:
        found = True
        print(pizza[midpoint][0])
        print(pizza[midpoint][3])
        print(count)
    else:
        if code < pizza[midpoint][0]:
            last = midpoint-1
        else:
            first = midpoint+1
