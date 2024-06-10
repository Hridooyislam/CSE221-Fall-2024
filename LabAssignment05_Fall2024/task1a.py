input=open('input1a.txt','r')
output=open('output1a.txt','w')

from collections import defaultdict 

dag = defaultdict(list)
vert, edge = list(map(int, input.readline().split()))

for x in range(edge):
    v, u = list(map(int, input.readline().strip().split()))
    dag[v].append(u)
def dfs_traversal(st,visited,path):
    path[st]=True
    visited[st]=True
    for nei in dag[st]:
        if visited[nei]==False:              #in this function we use Dfs for every vertices as well as keep the track of the path we are traversing
                                             #if we a node tries to traverse a already visited path it comes as true 
                                             # which detects as a cycle  ( this wwas stolen from my previous assignments task3 :3 )
            if dfs_traversal(nei,visited,path):
                return True 
        elif path[nei]:                   
            return True
    path[st]=False
    return False
        
    
def cycle_detector():
    visited=[False]*(vert+1)
    path=[False]*(vert+1)

    for x in range (vert):
        if visited[x]==False:
            if dfs_traversal(x,visited,path):   # for every unvisited nodes we initiate our dfs traversal
                return True 
    return False
                                                      
def stack_loader(dag, val, visited, stack):
    visited[val] = True 
    for x in dag[val]:
        if visited[x] == False:                            #in this part we use dfs traversal for each neighbor of our current vertice and push them into our stack
            stack_loader(dag, x, visited, stack)
    stack.append(val)

def topological():
    visited = [False] * (vert+1)
    stack = []
   
    for i in range(1,vert+1):
        if visited[i] == False:
            stack_loader(dag, i, visited, stack)     #we call our dfs function for each unvisited vertices 
    return stack

order = topological()
if cycle_detector()==False:      # we check if it is a cycle or not as topological ordreing is not possible without it not being a DAG
   while len(order) != 0:
      x = order.pop()
      output.write(str(x) + ' ')
else:
   output.write('Impossible')

input.close()
output.close()

