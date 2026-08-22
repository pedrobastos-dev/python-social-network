# g_sair.py
# Esse arquivo é chamado quando o usuário quer encerrar o programa.
# Antes de fechar, limpa toda a lista de usuários da memória.
# Em C isso seria o free(), aqui é usado o clear() que faz a mesma coisa no python.

from dados import usuarios


def sair():
    # guarda quantos usuários tinham antes de limpar, só pra mostrar na mensagem
    total = len(usuarios)

    # limpa tudo da memória antes de encerrar
    usuarios.clear()

    print(f"[OK] Memória liberada. {total} usuário(s) removido(s).")
    print("[OK] Sistema encerrado. Até logo!")


# teste isolado do módulo
if __name__ == "__main__":
    from a_adicionar_usuario import adicionar_usuario
    from c_criar_amizade import criar_amizade

    adicionar_usuario(1, "Ana Silva", 22)
    adicionar_usuario(2, "Bruno Costa", 25)
    criar_amizade(1, 2)

    print(f"Usuários antes de sair: {len(usuarios)}")
    sair()
    print(f"Usuários após sair:     {len(usuarios)}")
