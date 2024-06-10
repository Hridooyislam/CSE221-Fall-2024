input=open('input3.txt','r')
output=open('output3.txt','w')
rng=int(input.readline())
main_arr=list(map(int,input.readline().split()))
aux=list(map(int,input.readline().split()))
print(aux)
for x in range (rng):
  flg=False
  for j in range(rng-x-1):
    if aux[j]<aux[j+1]:
      aux[j],aux[j+1]=aux[j+1],aux[j]
      main_arr[j],main_arr[j+1]=main_arr[j+1],main_arr[j]
      flg=True
    
    elif aux[j]==aux[j+1]:
      if main_arr[j+1]<main_arr[j]:
        main_arr[j],main_arr[j+1]=main_arr[j+1],main_arr[j]
    if flg==False:
      break 

     


for x in range(rng):
  output.write(f'ID : {main_arr[x]} Mark : {aux[x]} \n')
output.close()
input.close()     

