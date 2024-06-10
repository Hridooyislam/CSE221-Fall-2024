input_2=open("input2.txt",'r')
ouput_2=open("output.txt",'w')
rng=int(input_2.readline())
arr=list(map(int,input_2.readline().split()))
def bubblesort(arr):
    for i in range(len(arr)-1):
            tag=False
            for j in range(): 
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    tag=True
                
            if tag==False:
                break
    return arr
data = bubblesort(arr)
for x in data:
     ouput_2.write(str(x)+' ')
            
        
input_2.close()
ouput_2.close()
''' For the best case scenario in a bubble sort which is O(n) I used flags which would would work as an indicator if the arrays are already sorted or not 
if the array is already sorted the loop would break which would further'''






