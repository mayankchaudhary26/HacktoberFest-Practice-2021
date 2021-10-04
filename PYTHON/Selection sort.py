def selectionsort(arr):
  i = 0
  while i < len(arr):
    min = arr[i]
    index = i
    for j in range(i+1,len(arr)):
      if arr[j] < min:
        index = j
        min = arr[j]
    arr[i] , arr[index] = arr[index] , arr[i]
    i += 1
  
  return arr

arr = [2,8,4,6,6,0,7]
print(selectionsort(arr))
