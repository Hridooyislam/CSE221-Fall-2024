input_file=open('input1a.txt','r')
output_file=open('output1a.txt','w')
s=input_file.readline()
print(s)
t=int(s)
for x in range(t):
  s=input_file.readline()
  n=int(s)
  if n%2==0:
    output_file.write(f'{n} is an even number\n')
  else:
    output_file.write(f'{n} is an odd number\n')
output_file.close()
