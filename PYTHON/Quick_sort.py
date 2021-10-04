def quick_first(list_first):
	pass



def quick_last(list_last):
	print('\n<<<<<<<<<< This is quick sort with pivot as last element >>>>>>>>>>')
	length = len(list_last)


	def partition(list_last, low, high):
		i = low - 1  
		pivot = list_last[high]  

		for j in range(low, high):
			if list_last[j] <= pivot:
				i = i + 1


				list_last[i], list_last[j] = list_last[j], list_last[i]
        
  
		list_last[i + 1], list_last[high] = list_last[high], list_last[i + 1]
		return i + 1


	def quicksort_last(list_last, low, high):
		if len(list_last) == 1:
			return list_last

		elif low < high:
			pi = partition(list_last, low, high)
			
			quicksort_last(list_last, low, pi - 1)  # left partition
			quicksort_last(list_last, pi + 1, high) # Right partition

	quicksort_last(list_last, 0, length - 1) # quicksort call

	print('\nThe sorted list is :: ', list_last)



def quick_mid(list_mid):

	length = len(list_mid)
	
	def listPartition(list1,lb,up):
	    pivot=list1[(up+lb)//2]
	    start=lb
	    end=up-1
	    while start<end:
	        while(list1[start]<pivot):
	            start=start+1
	        while(list1[end]>pivot):
	            end=end-1
	        if start<end:
	            temp=list1[start]
	            list1[start]=list1[end]
	            list1[end]=temp
	    return start

	def quickSort(list1,lb,up):

		if lb<up:
			pos=listPartition(list1,lb,up)
			quickSort(list1,lb,pos)
			quickSort(list1,pos+1,up)

	quickSort(list_mid, 0, length - 1) # quicksort call

	print('\nThe sorted list is :: ', list_mid)



def quick_random(list_random):
	pass



def dict_switch(choice):
	raw_dict = {
      1 : quick_first,
      2 : quick_last,
      3 : quick_mid,
      4 : quick_random
	}

	return raw_dict.get(choice, lambda : print('Wrong Input'))(raw_list)


raw_list = []
value = int(input('Enter the number of values in list :: '))

for i in range(value):
	list_val = int(input(f'Enter the value {i + 1} in list :: '))
	raw_list.append(list_val)

print('\nThe list is :: ', raw_list)


print("""
	1. Enter ->1<- for sorting through first value as pivot
	2. Enter ->2<- for sorting through last value as pivot
	3. Enter ->3<- for sorting through mid value as pivot
	4. Enter ->4<- for sorting through random value as pivot""")

choice = int(input('\nEnter your Choice ::'))
dict_switch(choice)
