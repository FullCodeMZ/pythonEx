Nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome com todas as letras maiúsculas é: {}'.format ( Nome.upper()))
print('O seu nome com todas as letras minúsculas é: {} '.format ( Nome.lower()))
print('O seu nome tem {} letras'.format (len(Nome) - Nome.count(' ')))
#print('O seu primeiro nome tem: {} letras '.format (Nome.find(' ')))
se = Nome.split ()
print('O seu primeiro nome é {} e tem {} letras '.format (se [0], len(se [0] )))