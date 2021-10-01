def maxProduct(arr):
    n=len(arr) 
    maxm=arr[0]
    maxm_prod=1
    minm_prod=1
    for ele in arr:
        if ele<0:
            maxm_prod,minm_prod=minm_prod,maxm_prod
        maxm_prod=max(ele,ele*maxm_prod)
        minm_prod=min(ele,ele*minm_prod)
            
        if maxm_prod>maxm:
            maxm=maxm_prod
    return maxm
print("Enter array elements with space")
nums=list(map(int,input().split()))
maximum=maxProduct(nums)
print(maximum)