#task2:
input=open('input2.txt','r')
output=open('output2.txt','w')
rng=int(input.readline().strip())
arr=list(map(int,input.readline().strip().split()))

def maxx(a,b):
  if a>=b:
    return a          # inthis function we find the maximum value 
  return b
def mergeSort(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2          # in thsi part we devide the array and compare each indices usin aour max fucntion
                                   # but we don not sort the array 
        a1 = mergeSort(arr[:mid])  
        a2 = mergeSort(arr[mid:])  
        return maxx(a1, a2)
output.write(str(mergeSort(arr)))
input.close()
output.close()