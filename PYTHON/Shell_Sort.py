def shellSort(data,n):
    h = n//2
    while h > 0:
        shell(data,h,n)
        h = h//2
    
    return data
def shell(data,h,n):
    index = 0
    while (index+h) <= 0:
        index += h
    while index > 0 :
        indexData1 = 0
        indexData2 = indexData1+h
        while indexData2 < index :
            if data[indexData1] > data[indexData2] :
                temp = data[indexData1]
                data[indexData1],data[indexData2] = data[indexData2],temp
            indexData1 = indexData2
            indexData2 += h
        index = index-h   

data = list(map(int,input('Enter Input : ').split(' ')))

print(shellSort(data,len(data)))
