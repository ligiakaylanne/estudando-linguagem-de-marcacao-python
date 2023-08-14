def volume(r):
    return 4/3*(r*r*r)
r=float(input('Digite o raio da esfera:'))
resultado=volume(r)
print('Seu volume é {:.1f}'.format(resultado))