input=open('input2_1.txt','r')
# output=open('output2','w')
# ver,edge=list(map(int,input.readline().split()))

# from collections import defaultdict,deque
# graph=defaultdict(list)
# for x in range (edge):
#     u,v=list(map(int,input.readline().split()))
#     graph[u].append(v)
#     graph[v].append(u)
# dicto={}
# def bfs(graph,s):
#     dist=0
#     visited = []
#     queue = deque([s])
#     path=[]
#     while queue:
#         val = queue.popleft()
#         if val not in visited:
#             visited.append(val)
#             path.append(val)           #here we use breadth first search method to traverse a graph 
#                                        # we visit the unvisisted nodes using queue and a auxilary list to keep track of our visited nodes  
#             for neighbor in graph[val]:
#                 if neighbor not in visited:
#                     dist+=1
#                     dicto[neighbor]=dist
#                     queue.append(neighbor)
#     return path

# trav=bfs(graph,1)
# for x in trav:
#     output.write(f'{x} ')
# output.close()