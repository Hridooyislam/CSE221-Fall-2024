
input = open('input1.txt', 'r')
output = open('output1.txt', 'w')
from collections import defaultdict
import heapq

vert, edge = list(map(int, input.readline().split()))
graph = defaultdict(list)

for x in range(edge):
    u, v, w = list(map(int, input.readline().split()))
    graph[u].append((v, w))

src = int(input.readline())

def dijkstra(graph, source):
    dists = [float('inf')] * (vert + 1)
    prio_queue = [(0, source)]
    dists[source] = 0

    while prio_queue:
        dist, node = heapq.heappop(prio_queue)  #in this function we are using the  bfs traversal technic.but instead using a normal queue we are using the heapqueue to find the edge with smallest weight.

        for neigh, weight in graph[node]:
            sum = dist + weight
            if sum < dists[neigh]:            #here we are comparing the total value of the already recorded distance of the node and the newly found wieght while traversing the nieghbors
                                            # if the newly found total weight is lesser than the previously recorded edge weighr we replace the weight with the newly found total weight  
                dists[neigh] = sum
                heapq.heappush(prio_queue, (sum, neigh))

    for x in range(len(dists)):
        if dists[x] == float('inf'):
            dists[x] = -1
    return dists

dists = dijkstra(graph, src)

for x in range(1, len(dists)):
    output.write(f'{dists[x]} ')

output.close()
 