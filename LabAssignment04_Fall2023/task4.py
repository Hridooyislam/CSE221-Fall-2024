input=open('input4_2.txt','r')
output=open('output4','w')
ver,edge=list(map(int,input.readline().split()))

from collections import defaultdict
graph=defaultdict(list)
for x in range (edge):
    u,v=list(map(int,input.readline().split()))
    graph[u].append(v)
def dfs_traversal(st,visited,path):
    path[st]=True
    visited[st]=True
    for nei in graph[st]:
        if visited[nei]==False:              #in this function we use Dfs for every vertices as well as keep the track of the path we are traversing
                                             #if we a node tries to traverse a already visited path it comes as true 
                                             # which detects as a cycle  
            if dfs_traversal(nei,visited,path):
                return True 
        elif path[nei]:                   
            return True
    path[st]=False
    return False
def cycle_detector():
    visited=[False]*(ver+1)
    path=[False]*(ver+1)

    for x in range (ver):
        if visited[x]==False:
            if dfs_traversal(x,visited,path):   # for every unvisited nodes we initiate our dfs traversal
                return 'YES'
    return "No"
g=cycle_detector()
output.write(f'{g}') 
output.close()

print(22101324%2)