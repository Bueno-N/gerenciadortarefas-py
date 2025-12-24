import json

tarefas = []

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
        
def main():
    carregar_tarefas()

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

if __name__ == "__main__":
    main()