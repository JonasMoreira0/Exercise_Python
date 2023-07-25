'''
Faça um programa que peça ao usuário para digitar um umero inteiro, 
informe se o número é par ou impar. Caso o usuario não digite o número 
inteiro, informe que não a número inteiro.
'''
num = float(input('Digite um numero: '))
resultado_1 = num % 2
resultado_2 = num // 1 

if resultado_1 == 0:
        print(f'O seu numero é par')
else:
        print(f'O seu numero é impar')
    
if resultado_2 != num:
    print('Numero não é inteiro!')
    
'''
Faça um pograma que pergunte a hora ao usuário e, baseando-se horário
descrito, exiba a saudação aproprida. 
Ex Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
hora = float(input('Me informe as horas? '))

if hora <= 11:
    print(f'Bom dia! h:{hora:.2f}')

elif hora <= 17:
    print(f'Boa tarde! h:{hora:.2f}')

else:
    print(f'Boa noite! h:{hora:.2f}')

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 ou 6 letras, escreva
"seu nome é normal"; Maior que 6 escreva "Seu nome é muito grande".
'''
nome = input('informe o seu nome: ')

if nome <= (nome[0:4]):
    print('Seu nome tem é curto')

elif nome <= (nome[4:5]):
    print('Seu nome é normal')
    
else:
    print('Seu nome é grande')