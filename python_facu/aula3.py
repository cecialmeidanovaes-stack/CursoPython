#Gerenciador de lista de Compras

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar item")
    print("4. Sair")

def adicionar_item(lista):
    item= input("Digite o nome do item a ser adicionado: ").strip()
    if item in lista:
        print (f"O item '{item}' já está na lista.")
    else:
        lista.append(item)
        print(f"Item '{item}'adicionado com sucesso!")

def remover_item(lista):
    item = input("Digite o nome do item a ser removido:").strip()
    if item in lista:
        lista.remove(item)
        print(f"Item '{item}' removido com sucess!.")
    else:
        print(f"Item '{item}' não esta na lista.")
def listar_itens(lista ):
    if lista:
        print("\nItens na lista de compras.")
        for i, item in enumerate(lista, start=1):
            print(f"{i}.{item}")
    else:
        print(f"O item ‘{item}’ não está na lista.")

def listar_itens(lista):        
    if lista:
         print("\nItens na lista de compras:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")
    else:
        print("A lista de compras está vazia.")

# Programa principal

lista_compras = []
while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionar_item(lista_compras)
        elif opcao == 2:
            remover_item(lista_compras)
        elif opcao == 3:
            listar_itens(lista_compras)
        elif opcao == 4:
            print ("Encerrando o programa. Boa sorte com suas compras")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número correspondente à opção.")