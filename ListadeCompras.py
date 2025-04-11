import os
lista = []
while True:
	print('Selecione uma opção')
	opcao = input('[i]nserir [a]pagar [l]istar')
	
	if opcao == 'i':
		os.system('clear')
		valor = input('Valor: ')
		lista.append(valor)
		
	elif opcao =='a':
		os.system('clear')
		indice_str = input('Escolha o índice para apagar:')
		
		try:
			indice = int(indice_str)
			del lista[indice]
		except ValueError:
			print('Por favor, digite um número inteiro.')
		except IndexError:
			print('índice não existe na lista')
		except Exception:
			print('Erro desconhecido')
		
	elif opcao =='l':
		os.system('clear')
		
		if len(lista)==0:
			print('Nada para listar.')
			
		for i, valor in enumerate(lista):
		print(i, valor)
			
	else:
		print('Opção inválida, escolha uma das listadas')
	
