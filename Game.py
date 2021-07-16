from random import randint
from time import sleep

print('====== VAMOS JOGAR JOKENPÔ ======')
print('')
print('Escolha oque você vai fazer! \n \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA \n')
User = int(input('Qual você quer? '))

PC = randint(1,3)
if PC == 1:
	PC = 'Pedra'
elif PC == 2:
	PC = 'Papel'
elif PC == 3:
	PC = 'Tesoura'
	
if User == 1:
	User = 'Pedra'
elif User == 2:
	User = 'Papel'
elif User == 3:
	User = 'Tesoura'
	
if User != 'Pedra' and User != 'Papel' and User != 'Tesoura':
	print('[ERRO] escolha uma opção valida.')
							
if User == 'Pedra' and PC == 'Papel' or User == 'Papel' and PC == 'Tesoura' or User == 'Tesoura' and PC == 'Pedra':	
	print('JO')
	sleep(0.5)
	print('KEN')
	sleep(0.5)
	print('PÔ')
	sleep(0.5)	
	print(f'Você escolheu {User}, Eu escolhi {PC} \n EU GANHEI!!')
elif User == 'Pedra' and PC == 'Tesoura' or User == 'Papel' and PC == 'Pedra' or User == 'Tesoura' and PC == 'Papel':
	print('JO')
	sleep(0.5)
	print('KEN')
	sleep(0.5)
	print('PÔ')
	sleep(0.5)	
	print(f'Você Escolheu {User}!! Eu escolhi {PC} \n VOCÊ GANHOU!!')
elif User == PC:
	print('JO')
	sleep(0.5)
	print('KEN')
	sleep(0.5)
	print('PÔ')
	sleep(0.5)
	print(f'Nós dois escolhemos {PC} \n EMPATOU!!')