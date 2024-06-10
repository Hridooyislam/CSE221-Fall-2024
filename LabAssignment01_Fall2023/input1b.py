input_1b=open('input1b.txt','r')
output_1b=open('output1b.txt','w')
s=input_1b.readline()
k=int(s)
for i in range(k):
  s=input_1b.readline()
  a=s.split( )

  x=int(a[1])
  op=a[2]
  y=int(a[3])
  if op == '+':
    output_1b.write(f'The result of {x}+{y} is {x+y}\n')
  elif op == '-':
    output_1b.write(f'The result of {x}-{y} is {x-y}\n')
  elif op == '*':
    output_1b.write(f'The result of {x}*{y} is {x*y}\n')
  else :
    output_1b.write(f'The result of {x}/{y} is {x/y}\n')
output_1b.close()