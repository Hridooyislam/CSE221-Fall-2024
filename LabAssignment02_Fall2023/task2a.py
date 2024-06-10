input=open('input2.txt','r')
output=open('output2a.txt','w')
rng1=int(input.readline())                                
ls1=list(map(int,input.readline().strip().split()))
rng2=int(input.readline())                              #making two lists of integers from the input file 
ls2=list(map(int,input.readline().strip().split()))
def merge(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:        #base case of our reccursive call 
        return list1

    if list1[0] < list2[0]:
        return [list1[0]] + merge(list1[1:], list2)
    else:                                                           #here we compare the first index of arrays and merge the arrays reccursively 
        return [list2[0]] + merge(list1, list2[1:])
data=merge(ls1,ls2) 
for x in data:
    output.write(f'{x}  ')   
            