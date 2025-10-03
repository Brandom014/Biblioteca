import sqlite3
def criar_tabela():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            título TEXT NOT NULL,
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
        
