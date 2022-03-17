"""
Usários e senhas
"""
usuarios = [('admin', 'admin123'), ('pedrosilva1235', 'qwertt*'), ('brunolaje12', '123456@'), ('teste223', '789645'),
            ('dioguinho123', 'sadsfdsaf'), ('walber42', 'senha1234!')]

# Inserir nome do usuário
nome_usuario = str(input('Nome do usuário: '))

# Verifica se nome do usário está na lista
try:
    a = dict(usuarios)
    b = str(a[nome_usuario])
except:
    # Nome do usario tá errado
    print("Nome de usuário não encontrado")
    quit()

# Inserir senha
senha = str(input('Senha: '))

# Confirma o acesso caso a senha esteja correta
if b == senha:
    print(f'{nome_usuario} seja Bem-Vindo')

else:
    print("Senha incorreta")
