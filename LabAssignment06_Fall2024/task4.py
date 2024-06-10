input=open('input4.txt','r')
output=open('output4.txt','w')
vert,edge=list(map(int,input.readline().split()))
edges=[]
from collections import defaultdict
graph=defaultdict(list)
for x in range (edge):
    u,v,w=list(map(int,input.readline().split()))
    graph[u].append((v,w))
    graph[v].append((u,w))
    edges.append([u,v,w])
sorted_edges=sorted(edges,key=lambda item:item[2]) # we sort the edges according to their edge weights 
parent_tracker=[i for i in range(vert+1)]

def finder(i):
    if parent_tracker[i] != i:
        parent_tracker[i] = finder(parent_tracker[i])
        return parent_tracker[i]                           # basic dsu functions as previous task

    return i

def friendmaker(v,u):
        fst = finder(v)
        snd = finder(u)

        if fst != snd:
            parent_tracker[fst] = snd
def kruskal():
    x=0
    i=0
    weight=0
    while x<vert-1:     # iterating till n-1
        u,v,w=sorted_edges[i]
        fst=finder(u)           #fiding the parent of 2 nodes 
        snd=finder(v)
        i+=1
        if fst!=snd:            # if they dont have the same parent unionizing them as well as increasing the total weight of MST
            x+=1
            weight+=w
            friendmaker(fst,snd)
    output.write(f'{weight}')
x=kruskal()
output.close()
            

        

