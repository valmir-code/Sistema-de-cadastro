import psycopg2

print("Biblioteca funcionando!")

conexao = psycopg2.connect(
    host="xxx",
    database="xxx",
    user="postgres",
    password="xxx",
    port="xxx"
)

print("Conectado ao PostgreSQL!")

cursor = conexao.cursor()

# CADASTRO
nome = input("Nome: ")
email = input("E-mail: ")
senha = input("Senha: ")

sql = """
INSERT INTO usuarios (nome, email, senha)
VALUES (%s, %s, %s)
"""

cursor.execute(sql, (nome, email, senha))

conexao.commit()

print("Usuário cadastrado com sucesso!")

# LOGIN
tentativa = 0

while tentativa < 3:

    email = input("E-mail: ")
    senha = input("Senha: ")

    sql = """
    SELECT * FROM usuarios
    WHERE email = %s AND senha = %s
    """

    cursor.execute(sql, (email, senha))

    usuario = cursor.fetchone()

    if usuario:
        print("Acesso liberado!")
        break

    else:
        tentativa += 1
        print("E-mail ou senha incorretos!")

else:
    print("Acesso bloqueado!")

cursor.close()
conexao.close()