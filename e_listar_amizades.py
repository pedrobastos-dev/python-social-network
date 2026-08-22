# e_listar_amizades.py
# Esse arquivo lista todos os amigos de um usuário específico.
# Mostra o ID e o nome de cada amigo.
# Se o usuário não tiver amigos, o código avisa que a lista tá vazia.

from dados import encontrar_usuario_por_id


def listar_amizades(user_id):
    # primeiro verifica se o usuário existe
    usuario = encontrar_usuario_por_id(user_id)
    if usuario is None:
        print(f"[ERRO] Usuário com ID {user_id} não encontrado.")
        return None

    print(f"\nAmigos de '{usuario['nome']}' (ID {user_id}):")

    # se a lista de amigos estiver vazia, o código avisa
    if not usuario["amigos"]:
        print("  (nenhum amigo cadastrado)")
        return []

    # percorre os IDs dos amigos e busca os dados de cada um
    amigos = []
    for amigo_id in usuario["amigos"]:
        amigo = encontrar_usuario_por_id(amigo_id)
        if amigo:
            print(f"  ID {amigo['id']} | {amigo['nome']}")
            amigos.append(amigo)

    return amigos


# teste isolado do módulo
if __name__ == "__main__":
    from a_adicionar_usuario import adicionar_usuario
    from c_criar_amizade import criar_amizade

    adicionar_usuario(1, "Ana Silva", 22)
    adicionar_usuario(2, "Bruno Costa", 25)
    adicionar_usuario(3, "Carla Dias", 28)
    adicionar_usuario(4, "Diego Melo", 19)
    criar_amizade(1, 2)
    criar_amizade(1, 3)

    listar_amizades(1)   # Ana tem 2 amigos
    listar_amizades(4)   # Diego não tem amigos
    listar_amizades(99)  # não existe
