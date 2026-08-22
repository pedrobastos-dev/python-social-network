# c_criar_amizade.py
# Aqui eu cria a amizade entre dois usuários.
# A amizade é bidirecional, ou seja, se Ana é amiga de Bruno,
# Bruno também é amigo de Ana. Então o código adiciona nos dois lados.
# Também impede que alguém vire amigo de si mesmo ou que
# a mesma amizade seja cadastrada duas vezes.

from dados import encontrar_usuario_por_id


def criar_amizade(id1, id2):
    # não faz sentido ser amigo de si mesmo
    if id1 == id2:
        print("[ERRO] Um usuário não pode ser amigo de si mesmo.")
        return False

    # busca os dois usuários pelo ID
    usuario1 = encontrar_usuario_por_id(id1)
    usuario2 = encontrar_usuario_por_id(id2)

    # checa se os dois existem
    if usuario1 is None:
        print(f"[ERRO] Usuário com ID {id1} não encontrado.")
        return False
    if usuario2 is None:
        print(f"[ERRO] Usuário com ID {id2} não encontrado.")
        return False

    # checa se já são amigos pra não duplicar
    if id2 in usuario1["amigos"]:
        print(f"[AVISO] '{usuario1['nome']}' e '{usuario2['nome']}' já são amigos.")
        return False

    # adiciona nos dois lados pra ficar bidirecional
    usuario1["amigos"].append(id2)
    usuario2["amigos"].append(id1)
    print(f"[OK] Amizade criada entre '{usuario1['nome']}' e '{usuario2['nome']}'.")
    return True


# teste isolado do módulo
if __name__ == "__main__":
    from a_adicionar_usuario import adicionar_usuario

    adicionar_usuario(1, "Ana Silva", 22)
    adicionar_usuario(2, "Bruno Costa", 25)
    adicionar_usuario(3, "Carla Dias", 28)

    criar_amizade(1, 2)   # deve funcionar
    criar_amizade(1, 2)   # já são amigos, deve avisar
    criar_amizade(1, 1)   # não pode ser amigo de si mesmo
    criar_amizade(1, 99)  # ID 99 não existe

    print("\nAmigos:")
    from dados import usuarios
    for u in usuarios:
        print(f"  {u['nome']} – amigos IDs: {u['amigos']}")
