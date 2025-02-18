import os

def exibir_nome_do_programa():
    print('neguin sabores\n')

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair')

opcao_escolhida = int(input('escolha uma opção: '))
print(f'você escolheu a opção{opcao_escolhida}\n')

def finalizar_app():
     os.system('cls')
     print('finalizar o app')

if opcao_escolhida == 1:
    print('cadastrar restaurante')
elif opcao_escolhida == 2:
        print('listar restaurante')
elif opcao_escolhida ==3:
        print('ativar restaurante')
else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()

if __name__ == '__main__':
   main()

