input=open('input4.txt','r')
output=open('output4.txt','w')
tsk,ppl=list(map(int,input.readline().split()))
assign=[]
task_ls=[]                                                    
for x in range (tsk):                                          
    task_ls.append(list(map(int,input.readline().split())))   #storing the tasks in an array from the input file 

def sorter(act_list):
    for j in range(len(act_list)):
        flg=False
        for k in range (len(act_list)-j-1):                              #we sort the array according to ending times
                                                                          #used flags to optimize the bubble sorting algo 

            if act_list[k][1]>act_list[k+1][1]:
                act_list[k],act_list[k+1]=act_list[k+1],act_list[k]
                flg=True
        if flg==False:
            break
    return act_list
task_ls=sorter(task_ls)
count=ppl
for x in range (ppl):
    assign.append(task_ls[x][1]) #assigning initial tasks to m amount of people by storing there task ending time in a list 
print(assign)
for x in range (tsk):
    for j in range (ppl):
        if assign[j]<=task_ls[x][0]:
            assign[j]=task_ls[x][1]   #distributing the tasks among people by checking if ending time can match the starting time of a newly assignable task 
            count+=1                  #taking count of assignable task 
            break
output.write(f'{count}')
