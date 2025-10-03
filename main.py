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

def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        for livro in cursor.fetchall():
            print(f"ID:{livro[0]} | Titulo:{livro[1]} | Autor:{livro[2]} | Ano:{livro[3]} | Disponibilidade:{livro[4]}")
        conexao.commit()
    except Exception as erro:
        print(f"erro ao tentar listar livros {erro}")
    finally:
        if conexao:
            conexao.close

def atualizacao_disponibilidade():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        id_livro = int(input("Digite o ID do livro que deseja atualizar a disponibilidade: ").strip())
        nova_disponibilidade = input("Digite a nova disponibilidade (sim/não): ").lower().strip()

        cursor.execute("""
        UPDATE livros SET disponivel = ? WHERE id = ?
        """, (nova_disponibilidade, id_livro))

        conexao.commit()
        if cursor.rowcount > 0:
            print("Disponibilidade atualizada com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido.")
    except Exception as erro:
        print(f"Erro ao atualizar a disponibilidade {erro}")
    finally:
        if conexao:
            conexao.close

