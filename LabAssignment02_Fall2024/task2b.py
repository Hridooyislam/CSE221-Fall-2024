input=open('input2.txt','r')
output=open('output2b.txt','w')
rng1=int(input.readline())                                
ls1=list(map(int,input.readline().strip().split()))
rng2=int(input.readline())                              #making two lists of integers from the input file 
ls2=list(map(int,input.readline().strip().split()))
i=0
j=0
ls=[]
while i<rng1 and j <rng2:   
    if ls2[i]<ls1[j]:                   #merging and also sorting two arrays  using  pointers 
        ls.append(ls2[i])
        i+=1
    else:
        ls.append(ls1[j])
        j+=1
if rng2>rng1:
    ls.extend(ls2[i:])
else:           #appending the left out elements from the arrays 
    ls.extend(ls1[j:])
for x in ls :
    output.write(f'{x} ')
        
            