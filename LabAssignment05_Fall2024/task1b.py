input=open('input1b.txt','r')
output=open('output1b.txt','w')

from collections import defaultdict,deque

dag = defaultdict(list)
vert, edge = list(map(int, input.readline().split()))
indeg=[0]*(vert+1)
def topo_sort_bfs(dag):
    for x in range(edge):
        v, u = list(map(int, input.readline().strip().split()))       #we prepare our grph from the input file as well as keep track of the indegrees
        dag[v].append(u)
        indeg[u]+=1
    q = deque()
    for course in range(1, vert+ 1):
        if indeg[course] == 0:                  #we first check out for vertices which have no indegree and enque them in our queue 
            q.append(course)
        print(q)
    order=[]
    while q:
    
        val=q.popleft()
        order.append(val)
        for nei in dag[val]:
            indeg[nei]-=1                       #we use bfs traversal but here instead of working with a visited list we keep track of the indegrees  
            if indeg[nei]==0:                   #if an vertex has an indegree of zero we enque  it 
                q.append(nei)

    return order
ordering=topo_sort_bfs(dag)
if len(ordering)==vert:
    str=''
    for x in ordering:
        str+=f'{x} '                      #in this part we check if its a DAG or not 
    output.write(str)

input.close()
output.close()