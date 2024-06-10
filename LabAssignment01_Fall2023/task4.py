inputfile = open('input4.txt','r')
output = open('output4.txt','w')

rng = int(inputfile.readline())
all = []
name = []
time = []

for i in range(rng):
  temp = (inputfile.readline().strip())
  all.append(temp)
  name.append(temp.split()[0])
  time.append(temp.split()[-1])


for x in range(rng):
  for j in range(rng-x-1):
    if name[j] > name[j+1]:
      name[j], name[j+1] = name[j+1], name[j]
      all[j], all[j+1] = all[j+1], all[j]

    elif name[j] == name[j+1]:
      if time[j] > time[j+1]:
        time[j], time[j+1] = time[j+1], time[j]
        all [j], all[j+1] = all[j+1], all[j]

for i in range(x):
  output.write(f'{all[i]}\n')
inputfile.close()
output.close()

