def CheckArithmetic(arr):
    b = []
    lenght_of_array = len(arr)
    for i in range(0,lenght_of_array-1):
        a = arr[i+1]-arr[i]
        b.append(a)
    if b.count(b[0]) == lenght_of_array-1:
        return True
    
def CheckGeometric(arr):
    b = []
    lenght_of_array = len(arr)
    for i in range(0,lenght_of_array-1):
        a = arr[i+1]/arr[i]
        b.append(a)
    if b.count(b[0]) == lenght_of_array-1:
        return True

def ArrayChallenge(arr):
    if CheckArithmetic(arr):
        return "Arithmetic"
    elif CheckGeometric(arr):
        return "Geometric"
    else:
        return -1

print(ArrayChallenge([5,10,15]))
print(ArrayChallenge([2,4,8,16]))
