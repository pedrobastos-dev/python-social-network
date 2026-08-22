# dados.py
# Aqui é onde é guardada a lista de usuários e as funções básicas
# pra encontrar um usuário pelo ID ou checar se ele já existe.
# Todos os outros arquivos importam daqui, então é tipo o "coração", de onde
# os arquivos do projeto pegam as funções, usadas para todos.

# lista que vai guardar todos os usuários cadastrados
usuarios = []


def encontrar_usuario_por_id(user_id):
    # percorre a lista inteira procurando o usuário com aquele ID
    # se achar, retorna ele, senão retorna None (nada)
    for usuario in usuarios:
        if usuario["id"] == user_id:
            return usuario
    return None


def id_existe(user_id):
    # só tem essa função pra checar se um ID já tá cadastrado
    # ela usa a de cima e retorna True ou False
    return encontrar_usuario_por_id(user_id) is not None
