import sqlite3
def criar_tabela():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            disponivel TEXT
            )
        """)
        conexao.commit()
    except Exception as erro:
        #caso ocorra algum erro no banco
        print(f"erro ao tentar criar a tabela {erro}")
    finally:
        #sempre fechar a conexao
        if conexao:
            conexao.close()


def cadrastar_livros(titulo, autor, ano):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros(titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, "sim")
        )
        conexao.commit()
    except Exception as erro:
        print(f"erro ao tentar cadrastar livro {erro}")
    finally:
        if conexao:
            conexao.close()
