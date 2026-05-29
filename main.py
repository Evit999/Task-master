tasks = []

def add_task(task):
    tasks.append(task)
    print(f"A tarefa '{task}' foi adicionada.")

def list_tasks():
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Tarefas:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(index):
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"A tarefa '{removed_task}' foi removida.")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            task = input("Digite a tarefa: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                index = int(input("Digite o número da tarefa a ser removida: "))
                remove_task(index)
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
