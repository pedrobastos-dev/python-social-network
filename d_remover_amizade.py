# d_remover_amizade.py
# Aqui o código desfaz a amizade entre dois usuários.
# Como a amizade é bidirecional, tem que remover nos dois lados,
# igual fez na hora de criar.

from dados import encontrar_usuario_por_id


def remover_amizade(id1, id2):
    # busca os dois usuários
    usuario1 = encontrar_usuario_por_id(id1)
    usuario2 = encontrar_usuario_por_id(id2)

    # checa se os dois existem
    if usuario1 is None:
        print(f"[ERRO] Usuário com ID {id1} não encontrado.")
        return False
    if usuario2 is None:
        print(f"[ERRO] Usuário com ID {id2} não encontrado.")
        return False

    # checa se eles realmente são amigos antes de tentar remover
    if id2 not in usuario1["amigos"]:
        print(f"[AVISO] '{usuario1['nome']}' e '{usuario2['nome']}' não são amigos.")
        return False

    # remove dos dois lados
    usuario1["amigos"].remove(id2)
    usuario2["amigos"].remove(id1)
    print(f"[OK] Amizade entre '{usuario1['nome']}' e '{usuario2['nome']}' removida.")
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

    print("\nAntes:")
    from dados import usuarios
    for u in usuarios:
        print(f"  {u['nome']} – amigos: {u['amigos']}")

    remover_amizade(1, 2)   # deve funcionar
    remover_amizade(1, 2)   # já não são amigos, deve avisar
    remover_amizade(1, 99)  # ID 99 não existe

    print("\nApós:")
    for u in usuarios:
        print(f"  {u['nome']} – amigos: {u['amigos']}")
