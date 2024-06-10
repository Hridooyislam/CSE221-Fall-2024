import numpy as np 
input =open("input6_2.txt", "r")
output = open("output6.txt", "w")
row,col=list(map(int,input.readline().split()))
visited=np.zeros((row,col))
matrix = []
for i in range(row): 
    matrix.append(list(input.readline().strip()))
def diamond_finder(matrix, i, j):
    if i < 0 or i >= row or j < 0 or j >= col or matrix[i][j] == '#' or visited[i][j] == 1.0:
        return 0  
        #this is the base condition where we check out for corner as well 
        #as obstacles and if our diamond was previously visited or not                                                 
                                                         
    count = 0
    if matrix[i][j] == 'D':
        count = 1               #here we check for diamonds if we find one we take count of it and make cahnges in the visited array 
    visited[i][j]=1.0           

    count  += diamond_finder(matrix, i-1, j)
    count  += diamond_finder(matrix, i+1, j) # here we traverse left-right and up-down of the node reccursively and take count of diamonds
    count  += diamond_finder(matrix, i, j-1)
    count  += diamond_finder(matrix, i, j+1)

    return count 

def max_diamonds(matrix):
    cur = 0

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '.':
                collection = diamond_finder(matrix, i, j)    # we check for diamonds if we find a path 
                if collection >=cur:  # here we find the maximum amout of diamonds in each traversal        
                    cur=collection              

    return cur 



result = max_diamonds(matrix)
output.write(f'{result}')