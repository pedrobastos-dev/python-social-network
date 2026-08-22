# b_remover_usuario.py
# Esse arquivo remove um usuário do sistema.
# O detalhe importante é que quando remove alguém, tem que remover
# essa pessoa da lista de amigos de todo mundo que era amigo dela também.
# Senão ia ficar um ID sobrando na lista de amigos dos outros.

from dados import usuarios, encontrar_usuario_por_id


def remover_usuario(user_id):
    # primeiro verifica se o usuário já existe
    usuario = encontrar_usuario_por_id(user_id)
    if usuario is None:
        print(f"[ERRO] Usuário com ID {user_id} não encontrado.")
        return False

    # passa por cada amigo do usuário que vai ser removido
    # e tira o ID do usuário da lista de amigos deles
    for amigo_id in usuario["amigos"]:
        amigo = encontrar_usuario_por_id(amigo_id)
        if amigo and user_id in amigo["amigos"]:
            amigo["amigos"].remove(user_id)

    # agora sim remove o usuário da lista principal
    usuarios.remove(usuario)
    print(f"[OK] Usuário '{usuario['nome']}' (ID {user_id}) removido com sucesso!")
    return True


# teste isolado do módulo
if __name__ == "__main__":
    from a_adicionar_usuario import adicionar_usuario
    from c_criar_amizade import criar_amizade

    adicionar_usuario(1, "Ana Silva", 22)
    adicionar_usuario(2, "Bruno Costa", 25)
    adicionar_usuario(3, "Carla Dias", 28)
    criar_amizade(1, 2)
    criar_amizade(1, 3)

    print("\nAntes da remoção:")
    for u in usuarios:
        print(f"{u['nome']} – amigos: {u['amigos']}")

    remover_usuario(1)   # remove Ana e limpa os vínculos dela
    remover_usuario(99)  # esse não existe, deve dar erro

    print("\nApós a remoção:")
    for u in usuarios:
        print(f"{u['nome']} – amigos: {u['amigos']}")
