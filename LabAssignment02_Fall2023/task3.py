input=open('task3.txt','r')
output=open('output3a.txt','w')
x=int(input.readline().strip())
act_list=[]

for i in range(x):
    tmp=list(map(int,input.readline().strip().split()))  # we make an array out of the given tasks
    act_list.append(tmp)
for j in range(len(act_list)):
    flg=False
    for k in range (len(act_list)-j-1):                              #sorts the array according to ending times
                                                                      #used tags to optimize 
        if act_list[k][1]>act_list[k+1][1]:
            act_list[k],act_list[k+1]=act_list[k+1],act_list[k]
            flg=True
    if flg==False:
        break
print(act_list)

i = 0                # first activity is selected from the sorted array 
task=[act_list[0]]

for j in range(1, x):
    if act_list[j][0] >= act_list[i][1]: #we compare the starting time of the initially selected activity with the ending time of other activities whenever our condition gets satisfied we update the ending time 
        task.append(act_list[j])
        i = j 
output.write(f'{len(task)}\n')
for p in task:
    output.write(f'{p[0]} {p[1]}\n')