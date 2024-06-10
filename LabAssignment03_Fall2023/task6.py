input=open('input6.txt','r')
output=open('output6.txt','w')
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
def quickSort(arr,start ,end,k):
    if start>=end:
        return 
    pivot = partition(arr, start, end)
    if pivot == k:
        return arr[k-1]
    elif pivot > k:                                                                                       
        return quickSort(arr, start, pivot - 1, k)         # in this part we find the k-th smallest elemt by comparing it with teh pivot we use the quicksort algorithm in two seperate halves if k is greater tahn pivot we search the left half or else we search the right half 
        
    else:
        return quickSort(arr, pivot + 1, end, k)
Qs = int(input.readline().split()[0])
for char in range(Qs):
    k=int(input.readline())
    find= quickSort(arr,0,len(arr)-1,k)
    output.write(f"{find}\n")
input.close()
output.close()