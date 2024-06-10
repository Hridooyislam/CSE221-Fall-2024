input=open('input5_1.txt','r')
output=open('output5.txt','w')
ver,edge,target=list(map(int,input.readline().split()))

from collections import defaultdict,deque
graph=defaultdict(list)
for x in range (edge):
    u,v=list(map(int,input.readline().split()))
    graph[u].append(v)
    graph[v].append(u)
graph={1: [3, 4], 3: [1, 2], 2: [3], 4: [1]}
destination=2
def bfs_shortest_path(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == destination:
            return len(path) - 1, path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
      
            
shortest=bfs_shortest_path(graph,1,target)
output.write(f'Time:{shortest[0]}\n')
st=''
for x in shortest[1]:
    st+=f' {x}'
output.write(f'Shortest Path:{st}')



    

