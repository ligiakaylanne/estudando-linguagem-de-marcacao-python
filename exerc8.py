def calculadora (x,y,s):
 return x,y,s
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
op=str(input('Escolha a operação(+,-,*,/):'))
if op == '+':
 print(n1+n2)
if op == '-':
 print(n1-n2)
if op == '*':
 print(n1*n2)
if op == '/':
 print(n1/n2)
