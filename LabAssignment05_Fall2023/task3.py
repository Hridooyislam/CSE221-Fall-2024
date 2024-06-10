

input=open("input3.txt", "r") 
output=open("output3.txt", "w") 
from collections import defaultdict 

dag = defaultdict(list)
trans_dag=defaultdict(list)
vert, edge = list(map(int, input.readline().split()))

for x in range(edge):
    v, u = list(map(int, input.readline().strip().split()))  #in this part we construct our graph as well as our transpose graph
    dag[v].append(u)
    trans_dag[u].append(v)

def dfs(a_list, visited, stack, current):
    visited[current] = True
    for neigh in a_list[current]:
        if not visited[neigh]:
            dfs(a_list, visited, stack, neigh)    #in this function we push inside our stack by using dfs
    stack.append(current)

def scc_finder(dag):
        visited = [False]*(vert+1)
        stack = []                                         
       
        for i in range(1, vert + 1):
            if not visited[i]:               
                dfs(dag, visited, stack, i)             # in this part we traverse the graph and prepare stack
        visited2 = [False]*(vert + 1)                  
        
        while stack:
            i = stack.pop()                               #in this part pop each value from stack and traverse the graph to chekck for strongly connected components 
            if not visited2[i]:
                scc = []
                dfs(trans_dag, visited2, scc, i)
                st=''
                for x in scc:
                     st+=f' {x}'
                     
                output.write(st + "\n")
scc_finder(dag)
input.close()
output.close()