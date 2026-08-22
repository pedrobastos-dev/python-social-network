# a_adicionar_usuario.py
# Esse arquivo cuida de cadastrar um novo usuário no sistema.
# Antes de cadastrar, o código verifica se o ID já existe pra não ter duplicação de ID's.
# Cada usuário tem: id, nome, idade e uma lista de amigos (começa vazia).

from dados import usuarios, id_existe


def adicionar_usuario(user_id, nome, idade):
    # primeiro o código checa se já tem alguém com esse ID
    # se tiver, ele avisa e cancela o cadastro
    if id_existe(user_id):
        print(f"[ERRO] Já existe um usuário com o ID {user_id}. Cadastro cancelado.")
        return False

    # cria o usuário como um dicionário (parecido com a struct em C)
    # a lista de amigos começa vazia e vai sendo preenchida depois
    novo_usuario = {
        "id": user_id,
        "nome": nome,
        "idade": idade,
        "amigos": []
    }

    # adiciona o novo usuário na lista global
    usuarios.append(novo_usuario)
    print(f"[OK] Usuário '{nome}' (ID {user_id}) cadastrado com sucesso!")
    return True


# esse bloco só roda se eu executar esse arquivo diretamente
# usei pra testar se a função tava funcionando
if __name__ == "__main__":
    adicionar_usuario(1, "Ana Silva", 22)
    adicionar_usuario(2, "Bruno Costa", 25)
    adicionar_usuario(1, "Carlos Lima", 30)   # esse deve dar erro de ID duplicado

    print("\nUsuários cadastrados:")
    for u in usuarios:
        print(f"ID {u['id']} | {u['nome']} | {u['idade']} anos")
