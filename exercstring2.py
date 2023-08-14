senha=str(input('Digite a senha cadastrada:'))

if len(senha) != 6:
    print('A senha deve ter 6 caracteres.')
if not any(char.isdigit() for char in senha) or not any(char.isalpha() for char in senha):
    print('A senha deve conter letras e números.')
if 'FLA' in senha or 'MENGO' in senha or 'MENGAO' in senha:
    print('Não deve constar as palavras FLA, MENGO ou MENGAO')
if senha[0] == 'A' or senha[-1] == 'F':
    print('Não deve começar com a letra ‘A’ nem terminar com a letra ‘F')
else:
    print("Senha válida.")
