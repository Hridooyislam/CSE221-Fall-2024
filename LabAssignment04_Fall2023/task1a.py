import numpy as np
input=open('input1a_2.txt','r')
output=open('output1a','w')
vert,edge=list(map(int,input.readline().split()))
adj_arr=np.zeros((vert+1,vert+1))                       
for x in range (edge):
    u,v,w=list(map(int,input.readline().split()))
    adj_arr[u][v]=w
for x in adj_arr:               #here we use an adjacency matrix to reperesent our weighted graph where we store the weight of the edges in respective cordinates 
    for j in x:
        output.write(f'{int(j)}  ')
    output.write(f'\n')

