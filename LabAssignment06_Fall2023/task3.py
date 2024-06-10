

input = open('input3.txt', 'r')
output = open('output3.txt', 'w')
vert, con = list(map(int, input.readline().split()))
parent_tracker = [i for i in range(vert)]
size = [1 for _ in range(vert)]

def finder(i):
    if parent_tracker[i] != i:
        parent_tracker[i] = finder(parent_tracker[i])
        return parent_tracker[i] 

    return i   # this function findes the parent of a node reccursively 

def friendmaker():
    for x in range(con):
        v, u = list(map(int, input.readline().split()))
        fst = finder(v)                          # we find the parent of each nodes
        snd = finder(u)

        if fst != snd: 
            parent_tracker[fst] = snd
            size[snd] += size[fst]       # if they dont have the same parent we union them by connecting second ones parent with the first one 
                                         # we also increase the size of second 
            output.write(f'{size[snd]}\n')
        else:
            output.write(f'{size[fst]}\n') # if they have the same parent we print the first one size 

friendmaker()

input.close()
output.close()
