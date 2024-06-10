input=open('input4_2.txt','r')
output=open('output4','w')
ver,edge=list(map(int,input.readline().split()))
print(ver,edge)
from collections import defaultdict
graph=defaultdict(list)
for x in range (edge):
    u,v=list(map(int,input.readline().split()))
    graph[u].append(v)
print(graph)
ver,edge=(4,4)
graph={3: [1, 2], 1: [4], 4: [3]}
def cycle(graph,checker,vertex,result,stack):
    checker[ver]=True
    stack.append(vertex)
    for x in graph[ver]:
        if checker[x]==False:
            result=cycle(graph,checker,x,result,stack )
            if result=='Yes':
                return 'Yes'
            if x in stack :
                return 'Yes'
    stack.pop()
    return result
stack=[]
checker=[False]*(ver+1)
j=cycle(graph,checker,ver,result,stack)