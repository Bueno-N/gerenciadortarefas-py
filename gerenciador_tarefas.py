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
        return usuario
    else:
        print("Usuário ou senha incorretos.")
        return None


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

def adicionar_tarefa(usuario_logado):
    descricao = input("Digite a tarefa: ").strip()
    if descricao:
        tarefa = {
            "descricao": descricao,
            "usuario": usuario_logado
        }
        tarefas.append(tarefa)
        salvar_tarefas()
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    else:
        print("Nenhuma tarefa digitada.")

def listar_tarefas(usuario_logado):
    encontrou = False
    print("\n=== SUAS TAREFAS ===")

    for i, tarefa in enumerate(tarefas, start=1):
        if tarefa["usuario"] == usuario_logado:
            print(f"{i} - {tarefa["descricao"]}")
            encontrou = True

    if not encontrou:
        print("Nenhuma tarefa cadastrada.")


def remover_tarefa(usuario_logado):
    tarefas_usuario = []

    for i, tarefa in enumerate(tarefas):
        if tarefa["usuario"] == usuario_logado:
            tarefas_usuario.append((i, tarefa))

    if not tarefas_usuario:
        print("Nenhuma tarefa para remover.")
        return
    
    print("\n === Suas Tarefas ===")
    for num, (indice_real, tarefa) in enumerate(tarefas_usuario, start=1):
        print(f"{num} - {tarefa["descricao"]}")

    try:
        escolha = int(input("Numero da tarefa para remover: "))

        if 1 <= escolha <= len(tarefas_usuario):
            indice_real = tarefas_usuario[escolha -1][0]
            removida = tarefas.pop(indice_real)
            salvar_tarefas()
            print(f"Tarefa '{removida['descricao']}' removida!")
        else:
            print("Numero invalido.")
    except ValueError:
        print("Digite um numero valido")


def editar_tarefa(usuario_logado):
    tarefas_usuario = []

    for i, tarefa in enumerate(tarefas):
        if tarefa["usuario"] == usuario_logado:
            tarefas_usuario.append((i, tarefa))

    if not tarefas_usuario:
        print("Nenhuma tarefa para editar.")
        return
    
    print("\n === SUAS TAREFAS ===")
    for num, (indice_real, tarefa) in enumerate(tarefas_usuario, start=1):
        print(f"{num} - {tarefa["descricao"]}")

    try:
        escolha = int(input("Numero da tarefa para editar: "))

        if 1 <= escolha <= len(tarefas_usuario):
            indice_real = tarefas_usuario[escolha - 1][0]

            nova_descricao = input("Nova descricao: ").strip()

            if nova_descricao:
                tarefas[indice_real]["descricao"] = nova_descricao
                salvar_tarefas()
                print("Tarefa editada com sucesso!")
            else:
                print("Descrição não pode ser vazia.")
        else:
            print("Número inválido")

    except ValueError:
        print("Digite um número válido.")
        
        



def menu_tarefas(usuario_logado):
    while True:
        mostrar_menu()
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            adicionar_tarefa(usuario_logado)
        elif escolha == "2":
            listar_tarefas(usuario_logado)
        elif escolha == "3":
            remover_tarefa(usuario_logado)
        elif escolha == "4":
            editar_tarefa(usuario_logado)
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
            usuario_logado = login()
            if usuario_logado:
                menu_tarefas(usuario_logado)
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            print("Saindo do sistema...")
            return
        else:
            print("Opção inválida.")
    


if __name__ == "__main__":
    main()