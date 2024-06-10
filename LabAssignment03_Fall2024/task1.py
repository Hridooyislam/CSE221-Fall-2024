#task1:
input=open('input1.txt','r')
output=open('output1.txt','w')
rng=input.readline().strip()
arr_1=list(map(int,input.readline().strip().split()))
def merge(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:               
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2             #in this code we devide the array from left to mid and mid to right using reccursion.after that we use a function called merger where we sort and merge the elements.
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

j=mergeSort(arr_1)
for x in j:
  output.write(f'{x}  ')
input.close()
output.close()






