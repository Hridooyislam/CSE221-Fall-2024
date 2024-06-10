input=open('input5.txt','r')
output=open('output5.txt','w')
rng=input.readline()
arr=list(map(int,input.readline().strip().split()))
def partition(arr, start, end):
 
    pivot = arr[end]
 
    i = start - 1
 
    for j in range(start, end):
        if arr[j] <= pivot:
             i+=1
             arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1],arr[end] = arr[end],arr[i + 1]               #using this partition function to find the pivot.initailly we pick the pivot at the end of our initial array.
    return i+1
def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)  # we devide and conquer using the pivot 
        quicksort(A,q+1,r)
    return arr
w=quicksort(arr,0,len(arr)-1)
for x in w:
    output.write(f'{x} ')
input.close()
output.close()

            
