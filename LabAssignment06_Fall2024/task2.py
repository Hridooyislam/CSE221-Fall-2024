from collections import defaultdict
import heapq
input=open('input2.txt','r')
output=open('output2.txt','w')
vert,edge=list(map(int,input.readline().split()))
graph=defaultdict(list)
for x in range(edge):
    u,v,w=list(map(int,input.readline().split()))
    graph[u].append((w,v))
alice_src,bob_src=list(map(int,input.readline().split()))

def dijkstra(graph,source):
    dists=[float('inf')]*(vert+1)
    pq=[(0,source)]
    dists[source]=0
    while pq:
        dist,node=heapq.heappop(pq)
        for path,neigh in graph[node]:
            sum=dist+path                       #basic implementtation of dijkstra algo
            if sum<dists[neigh]:
                dists[neigh]=sum
                heapq.heappush(pq,(sum,neigh))
    return dists
def meet_in_the_middle(graph):
     time_taken=float('inf')
     location=-1
     alice = dijkstra(graph, alice_src)
     bob = dijkstra(graph, bob_src)     #calling  dijkstra from 2 different sources which gives us 2 distance arrays
                                                 
     for x in range(1, vert + 1):
          
          if alice[x] != float('inf') and bob[x] !=float('inf'):#handling the case for nodes which have infinite distances[irreachable]

              max_time = max(alice[x], bob[x])#comparing the distances upon each iteration and returning the maximum        
              if max_time < time_taken:
                  time_taken = max_time
                                   #if the maximum time taken is less than the already decalred maximum we replace them 
                  location  = x
     if time_taken==float('inf'):
         output.write( 'impossible')
     else:
         output.write(f'Time:{time_taken}\n')
         output.write(f'node:{location}')
    
meet_in_the_middle(graph)
output.close()
        

 