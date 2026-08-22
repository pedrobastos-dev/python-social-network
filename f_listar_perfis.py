# f_listar_perfis.py
# Esse arquivo mostra todos os usuários cadastrados no sistema.
# Exibe o ID, nome, idade e quantidade de amigos de cada um.
# Se não tiver ninguém cadastrado, o código avisa que a lista está vazia.

from dados import usuarios


def listar_perfis():
    print("\nPerfis cadastrados")

    # checa se tem alguém cadastrado
    if not usuarios:
        print("(nenhum usuário cadastrado)")
        return []

    # cabeçalho da tabela
    print(f"{'ID':<6} {'Nome':<25} {'Idade':<8} {'Nº de Amigos'}")

    # passa por cada usuário e mostra as informações
    for u in usuarios:
        print(f"{u['id']:<6} {u['nome']:<25} {u['idade']:<8} {len(u['amigos'])}")

    return list(usuarios)


# teste isolado do módulo
if __name__ == "__main__":
    from a_adicionar_usuario import adicionar_usuario
    from c_criar_amizade import criar_amizade

    listar_perfis()  # deve mostrar lista vazia

    adicionar_usuario(1, "Ana Silva", 22)
    adicionar_usuario(2, "Bruno Costa", 25)
    adicionar_usuario(3, "Carla Dias", 28)
    criar_amizade(1, 2)
    criar_amizade(1, 3)

    listar_perfis()
