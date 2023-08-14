def velocidade (w,x,y,z):
    return (w-x)/(y-z)
ki=float(input('Km final do carro:'))
kf=float(input('Km inicial do carro:'))
hf=float(input('Hora que terminou o trajeto:'))
hi=float(input('Hora que iniciou o trajeto:'))
resultado=velocidade(kf,ki,hf,hi)
print(resultado)


