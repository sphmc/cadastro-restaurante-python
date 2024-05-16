import os

#restaurantes = ["KFC","Pizza Hut"]

restaurantes = [{"nome": "Cantina toscana" , "categoria": "Italiana", "ativo": True},
                {"nome": "Sushi da Praça", "categoria": "Japonesa", "ativo": False},
                {"nome": "Churrascaria Gaúcha", "categoria": "Brasileira", "ativo": True},
                {"nome": "Padaria Pão Doce", "categoria": "Padaria", "ativo": True}]


def exibir_nome_do_programa():
    print("""
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀   █▀█ █▄░█ █░░ █ █▄░█ █▀▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄   █▄█ █░▀█ █▄▄ █ █░▀█ ██▄""")
    print("")

def menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
   
def finalizar_app():
    print("\nFinalizando ...")
 
def opcao_invalida():
    print("\nNão temos essa opção.\n")
    input("Digite enter para voltar ao menu principal")  
    main()
   
def cadastrar_restaurante():
    os.system('cls')
    print("\n\nCadastre-se: ")
    nome_restaurante= input("coloque o nome do seu restaurante: ")
    restaurantes.append(nome_restaurante)
    categoria= input("coloque a categoria do seu restaurante: ")
    dados_do_restaurante = {'nome': nome_restaurante.ljust(20)}, {"categoria" : categoria.ljust(20)}, {'ativo': False.ljust(20) }
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante{nome_restaurante} foi cadastrado!')
    input("Digite enter para voltar ao menu")  
    main()
   
def listar_restaurantes():
    print(f"\naqui esta a lista de restaurantes do sistema: ")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        print(f"--", nome_restaurante)
        print(f"categoria:", categoria_restaurante, "\n")
        
    input("Digite enter para voltar ao menu")  
    main()
    
def alternar_estado_do_restaurante () :
    print('alternando o estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False 
    
    for restaurante in restaurantes :
        if nome_restaurante == restaurante ['nome'] :
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mansagem = f' o restaurante{nome_restaurante} foi ativada com sucesso' if restaurante[ 'ativo'] else f' o restaurante {nome_restaurante} foi desativado'
            print(mansagem)        
    if  not restaurante_encontrado:
        print('o restaurante não foi encontrado')
        
        
        
    

def escolher_opção():
    try:
        opcao = int(input("\nEscolha uma opção: "))
               
        if(opcao == 1):
           cadastrar_restaurante()

        elif(opcao == 2):
            listar_restaurantes()
               
        elif(opcao == 3):
            alternar_estado_do_restaurante()
               
        elif(opcao == 4):
            finalizar_app()
           
        else:
            opcao_invalida()
           
    except:
        opcao_invalida()

   
def main():
    os.system('cls')
    exibir_nome_do_programa()
    menu()
    escolher_opção()
   
if __name__ == '__main__':
    main()