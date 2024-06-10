input=open('input3_3.txt','r')
output=open('output3','w')
ver,edge=list(map(int,input.readline().split()))

from collections import defaultdict
graph=defaultdict(list)
for x in range (edge):
    u,v=list(map(int,input.readline().split()))
    graph[u].append(v)
    graph[v].append(u)
def dfs(graph,st,visited=[]):
        visited.append(st)
        
        for nb in graph[st]:
            if nb not in visited:    #here we use depth first search method to traverse an undirected graph  
                dfs(graph,nb,visited)# we visit the unvisited nodes reccursively 
        return visited 
g=dfs(graph,1)
for x in g:
     output.write(f'{x} ')
output.close()
