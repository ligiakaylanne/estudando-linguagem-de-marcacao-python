def converte(x,y,z):
    return x,y,z
h=int(input('Digite a Hora:'))
m=int(input('Digite os minutos:'))
s=int(input('Digite os segundos:'))
converte=(h*3600)+(m*60)+s
print ('{}h {}m e {}s correspondem a {}segundos'.format(h,m,s,converte))