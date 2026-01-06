import json

usuarios = {}
tarefas = []

def carregar_usuarios():
    global usuarios
    try:
        with open("usuarios.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        usuarios = {}

def salvar_usuarios():
    with open("usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)


def cadastrar_usuario():
    usuario = input("Digite um nome de usuario: ").strip()

    if usuario in usuarios:
        print("Usuario já existe.")
        return
    
    senha = input("Digite uma senha: ").strip()

    if not usuario or not senha:
        print("Usuário e senha não podem ser vazios.")
        return
    
    usuarios[usuario] = senha
    salvar_usuarios()
    print("Usuário cadastrado com sucesso!")

def login():
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False


def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            tarefas.extend(dados)
    except FileNotFoundError:
        pass 

def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefa")
    print("3 - Remover tarefa")
    print("4 - Editar tarefa")
    print("5 - Sair")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    else:
        print("Nenhuma tarefa digitada.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n === TAREFAS CADASTRADAS ===")
    for i, tarefa in enumerate (tarefas, start=1):
        print(f"{i} - {tarefa}")

def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    listar_tarefas()
    try:
        numero = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= numero <= len(tarefas):
            tarefa_removida = tarefas.pop(numero - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!" )
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def editar_tarefa():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    listar_tarefas()

    try:
        numero = int(input("Digite o número da tarefa que deseja editar: "))
        if 1 <= numero <= len(tarefas):
            nova_tarefa = input("Digite o novo texto da tarefa: ").strip()

            if nova_tarefa:
                tarefas[numero - 1] = nova_tarefa
                salvar_tarefas()  
                print("Tarefa editada com sucesso!")
            else:
                print("O texto da tarefa não pode ser vazio.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")


def menu_tarefas():
    while True:
        mostrar_menu()
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            remover_tarefa()
        elif escolha == "4":
            editar_tarefa()
        elif escolha == "5":
            salvar_tarefas()
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


def main():
    carregar_usuarios()
    carregar_tarefas()

    while True:
        print("\n1 - Login")
        print("2 - Cadastrar usuários")
        print("3 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            if login():
                menu_tarefas()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            print("Saindo do sistema...")
            return
        else:
            print("Opção inválida.")
    


if __name__ == "__main__":
    main()