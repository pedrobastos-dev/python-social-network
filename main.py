# main.py
# Esse é o arquivo principal do projeto. Ele junta todos os outros módulos
# e exibe um menu pro usuário escolher o que quer fazer.
# Cada opção chama a função do arquivo correspondente.

from a_adicionar_usuario import adicionar_usuario
from b_remover_usuario   import remover_usuario
from c_criar_amizade     import criar_amizade
from d_remover_amizade   import remover_amizade
from e_listar_amizades   import listar_amizades
from f_listar_perfis     import listar_perfis
from g_sair              import sair


def exibir_menu():
    # mostra as opções disponíveis e retorna o que o usuário digitou
    print("\n|------------------------------|")
    print("|      REDE SOCIAL – MENU      |")
    print("|------------------------------|")
    print("|  a) Adicionar usuário        |")
    print("|  b) Remover usuário          |")
    print("|  c) Criar amizade            |")
    print("|  d) Remover amizade          |")
    print("|  e) Listar amigos de usuário |")
    print("|  f) Listar todos os perfis   |")
    print("|  g) Sair                     |")
    print("|------------------------------|")
    return input("Escolha uma opção: ").strip().lower()


def ler_int(prompt):
    # fica pedindo até o usuário digitar um número válido
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("[ERRO] Digite um número inteiro válido.")


def main():
    try:
        while True:
            opcao = exibir_menu()

            if opcao == "a":
                user_id = ler_int("ID do novo usuário: ")
                nome    = input("Nome completo: ").strip()
                idade   = ler_int("Idade: ")
                adicionar_usuario(user_id, nome, idade)

            elif opcao == "b":
                user_id = ler_int("ID do usuário a remover: ")
                remover_usuario(user_id)

            elif opcao == "c":
                id1 = ler_int("ID do primeiro usuário: ")
                id2 = ler_int("ID do segundo usuário:  ")
                criar_amizade(id1, id2)

            elif opcao == "d":
                id1 = ler_int("ID do primeiro usuário: ")
                id2 = ler_int("ID do segundo usuário:  ")
                remover_amizade(id1, id2)

            elif opcao == "e":
                user_id = ler_int("ID do usuário: ")
                listar_amizades(user_id)

            elif opcao == "f":
                listar_perfis()

            elif opcao == "g":
                sair()
                break

            else:
                print("[AVISO] Opção inválida. Escolha entre a e g.")

    except KeyboardInterrupt:
        # se o usuário fechar com Ctrl+C, ainda libera a memória antes de sair
        print("\n\n[AVISO] Programa interrompido pelo usuário.")
        sair()


if __name__ == "__main__":
    main()