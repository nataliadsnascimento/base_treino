from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        # Criar tabela no banco de dados
        connection.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                assistido INTEGER NOT NULL DEFAULT 0
            )
        """)

        # Inserir dados iniciais (OBRIGATÓRIO!!!!)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM filmes")
        if cursor.fetchone()[0] == 0:
            filmes_iniciais = [
                ("Interestelar", "Ficção científica sobre viagens espaciais e buracos de minhoca.", 1),
                ("O Poderoso Chefão", "Clássico do cinema sobre a família mafiosa Corleone.", 0),
                ("A Viagem de Chihiro", "Animação do Studio Ghibli sobre uma garota em um mundo espiritual.", 1),
            ]
            cursor.executemany(
                "INSERT INTO filmes (titulo, descricao, assistido) VALUES (?, ?, ?)",
                filmes_iniciais
            )

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")