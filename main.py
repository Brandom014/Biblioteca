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


def cadastrar_livros(titulo, autor, ano):
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
        print(f"erro ao tentar cadastrar livro {erro}")
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

def remover_livro():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        id_livro = int(input("Digite o ID do livro que deseja remover: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conexao.commit()
        if cursor.rowcount > 0:
            print(f"Livro com ID {id_livro} removido com sucesso!")
        else:
            print("Nenhum livro foi encontrado com o ID fornecido.")
    except Exception as erro:
        print(f"Erro ao remover livro {erro}")
    finally:
        if conexao:
            conexao.close

def menu():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        while True:
            print("\nMenu")
            print("1. Cadastrar livro")
            print("2. Listar livros")
            print("3. Atualizar disponibilidade")
            print("4. Remover livro")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": cadastrar_livros()
                case "2": listar_livros()
                case "3": atualizacao_disponibilidade()
                case "4": remover_livro()
                case "5": 
                    print("Acesso encerrado")
                    break
    except Exception as erro:
        print(f"Erro no Menu: {erro}")
    finally:
        if conexao:
            conexao.close()


