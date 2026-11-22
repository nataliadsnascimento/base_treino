from database.connection import get_connection


def install():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        # Tabela equipamentos (entidade do colega)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                disponivel INTEGER NOT NULL DEFAULT 1
            )
        """)

        # Tabela filmes (sua entidade)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                assistido INTEGER NOT NULL DEFAULT 0
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM filmes")
        if cursor.fetchone()[0] == 0:
            filmes_iniciais = [
                ("Interestelar", "Ficção científica sobre viagens espaciais e relatividade.", 0),
                ("O Poderoso Chefão", "Clássico drama sobre a família mafiosa Corleone.", 0),
                ("A Viagem de Chihiro", "Animação do Studio Ghibli sobre um mundo espiritual.", 0),
            ]
            cursor.executemany(
                "INSERT INTO filmes (titulo, descricao, assistido) VALUES (?, ?, ?)",
                filmes_iniciais
            )

        connection.commit()
        print("Banco de dados instalado com sucesso!")
    finally:
        connection.close()


if __name__ == "__main__":
    install()