input=open('input2.txt','r')
output=open('outpu2.txt','w')

from collections import defaultdict,deque

dag = defaultdict(list)
vert, edge = list(map(int, input.readline().split()))
indeg=[0]*(vert+1)
def topo_sort_bfs(dag):
    for x in range(edge):
        v, u = list(map(int, input.readline().strip().split()))
        dag[v].append(u)
        indeg[u]+=1                                               # we prepare our grph from the input file as well as keep track of the indegrees
    q = deque()
    for course in range(1, vert+ 1):
        if indeg[course] == 0:
            q.append(course)         # we first check out for vertices which have no indegree and enque them in our queue                             
        print(q)
    order=[]
    while q:
        q = deque(sorted(q))                      # we sort our queue in ascending order which turns it into a priority queue
                                                   
        val=q.popleft()
        order.append(val)
        for nei in dag[val]:
            indeg[nei]-=1
            if indeg[nei]==0:                # we use bfs traversal but here instead of working with a visited list we keep track of the indegrees  
                q.append(nei)                #if an vertex has an indegree of zero we enque  it 

    return order
ordering=topo_sort_bfs(dag)
if len(ordering)==vert:            # in this part we check if its a DAG or not 
    str=''
    for x in ordering:
        str+=f'{x} '
    output.write(str)
input.close()
output.close()