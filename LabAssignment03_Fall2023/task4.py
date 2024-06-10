
input=open('input4.txt','r')
output=open('output4.txt','w')
rng=input.readline()
arr=list(map(int,input.readline().strip().split()))
def maximum(arr):
    if len(arr)==1:
        return arr[0]
    mid=len(arr)//2           # we find the mxiamu number of an array using devide and conquer in this function 
    left=maximum(arr[:mid])
    right=maximum(arr[mid:])
    if left>right:            
        return left
    return right
def max_sq_sum(arr):
    temp=0
    
    for x in range(len(arr)-1):
        maxx=maximum(arr[x+1:])   
        sum=arr[x]+maxx**2    # we find out the summation of the squared value of the maximum and i the values if a greater value of sum is found.
        if sum>temp:
            temp=sum
    return temp

w=max_sq_sum(arr)
output.write(f'{w}')
input.close()
output.close()