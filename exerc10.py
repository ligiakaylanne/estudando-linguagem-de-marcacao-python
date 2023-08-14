def soma (x,y):
    return x,y
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
cod=int(input('Escolha um número de 1 a 4:'))
if cod == 1:
    print((n1+n2)/2)
if cod == 2:
    print(abs(n1-n2))

if cod == 3:
    print(n1*n2) 
if cod == 4:
    print(n1/n2)   
