from random import randint

print('====== VAMOS JOGAR JOKENPÔ ======')
print('')
print('Escolha oque você vai fazer! \n \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA \n')
User = int(input('Qual opção voce escolheu? '))

PC = randint(1,3)
if PC == 1:
	PC = 'Pedra'
elif PC == 2:
	PC = 'Papel'
elif PC == 3:
	PC = 'Tesoura'
	
if User != 1 and User != 2 and User != 3:
	print('[ERRO] escolha uma opção valida.')						
elif User == 1 and PC == 'Papel' or User == 2 and PC == 'Tesoura' or User == 3 and PC == 'Pedra':
	print(f'Você perdeu, eu escolhi {PC}')
elif User == 1 and PC == 'Tesoura' or User == 2 and PC == 'Pedra' or User == 3 and PC == 'Papel':
	print(f'Você ganhou!! eu escolhi {PC}')
else:
	print(f'A gente empatou!! eu escolhi {PC}')