# -*- coding: utf-8 -*-

input=open('input1a.txt','r')
output=open('output1a.txt','w')

p=list(map(int,input.readline().split()))#making an array of integers from the output file
rng=p[0]
sum=p[1]
arr=list(map(int,input.readline().split()))#making an array of integers from the output file
b=0  
print(arr)
for x in range (rng):
  for j in range (x+1,rng):

      if arr[x]+arr[j]==sum:  # using nested loop to check if the sum of both can reach target value
        b=1
        output.write(f'{x+1} {j+1}\n')
        break
if b==0 :                           #using a flag of 0 and 1 to handle impossible cases
  output.write(f'impossible')
input.close()
output.close()

