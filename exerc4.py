def produto(x,y):
    return x*y
preço=float(input('Qual preço do produto:'))
quant=int(input('Quantos você vai levar:'))
resultado=produto(preço,quant)
print('O valor total a ser pago é',resultado)