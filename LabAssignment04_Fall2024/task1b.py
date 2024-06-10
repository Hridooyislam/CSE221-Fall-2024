input=open('input1a_2.txt','r')
output=open('output1b.txt','w')
vert,edge=list(map(int,input.readline().split()))
adj_list=[[] for i in range(vert+1)]
for x in range(edge):
    u,v,w=list(map(int,input.readline().split()))
    adj_list[u].append((v,w))          # here we use adjaceny list to represent our graph 
for x in range(vert):
    output.write(f'{x}:{str(adj_list[x])[1:-1]}\n')
output.close