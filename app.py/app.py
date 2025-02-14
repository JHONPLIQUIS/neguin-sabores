print('neguin sabores\n')

print('1. cadastrar restaurante')
print('2. listar restaurante')
print('3. ativar restaurante')
print('4. sair')

opcao_escolhida = int(input('escolha uma opção: '))
print(f'você escolheu a opção{opcao_escolhida}\n')

if opcao_escolhida == 1:
    print('cadastrar restaurante')
elif opcao_escolhida == 2:
        print('listar restaurante')
elif opcao_escolhida ==3:
        print('ativar restaurante')
else:
        print('encerrando o programa')

