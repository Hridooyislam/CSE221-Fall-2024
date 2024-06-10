input=open('input3.txt','r')
output=open('output3.txt','w')
rng=input.readline()
arr=list(map(int,input.readline().strip().split()))
def inv_counter(a, b):
    count = 0
    lst=[]                            
    i=0                                     
    j=0
    while i<len(a) and j<len(b):  
        if a[i]<b[j]:
            lst.append(a[i])
            i+=1  
        else:                      
            lst.append(b[j])
            count+=len(a)-i #in this part we count the inversions by substracting the current value of iteration with the length
            j+=1
    lst.extend(a[i:])
    lst.extend(b[j:])
    return count
def devider(arr):
    
    cnt=0
    if len(arr)==1:
        return cnt
    mid=len(arr)//2         #in thsi part we devide the array and check for 
                            #inversions using inversion_count funnction and store it in count variable     
    cnt+=devider(arr[:mid])    
    cnt+=devider(arr[mid:])
    cnt+=inv_counter(arr[:mid],arr[mid:])
    return cnt

output.write(f'{devider(arr)}')
output.close()
