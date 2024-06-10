input=open('input2.txt','r')
output=open('output2.txt','w')
rng1=int(input.readline())                                
ls1=list(map(int,input.readline().strip().split()))
rng2=int(input.readline())                              #making two lists of integers from the input file 
ls2=list(map(int,input.readline().strip().split()))
i=0
j=0
ls=[]
while i<rng1 and j <rng2:   
    if ls2[i]<ls1[j]:                   #merging two arrays while initiating using pointers 
        ls.append(ls2[i])
        i+=1
    else:
        ls.append(ls1[j])
        j+=1
ls.extend(ls2[i:])           #appending the which where left out 
ls.extend(ls1[j:])
        
            