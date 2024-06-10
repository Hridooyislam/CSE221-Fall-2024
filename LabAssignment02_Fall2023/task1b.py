input=open('input1b.txt','r')
output=open('output1b.txt','w')
p=list(map(int,input.readline().split()))

rng=p[0]
sum=p[1]


arr=list(map(int,input.readline().split()))
lst=len(arr)-1
x=0
tag=False
while x<lst:

  if arr[x]+arr[lst]==sum:

    output.write(f'{x+1}  {lst+1}')
    tag=True
    break

  if arr[x]+arr[lst]<sum:
    x+=1                                #traversing the array using two pointer method
  else:
    lst-=1
if tag==False:
   output.write(f'impossible')       # using flags to check impossible cases


input.close()
output.close()