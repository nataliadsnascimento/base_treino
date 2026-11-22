from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTIS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT,
            lido INTEGER DEFAULT 0
            )
""")

        cursor = connection.execute("SELECT COUNT(*) FROM livros")
        total = cursor.fetchone()[0]
        
        if 	total == 0:
            connection.execute("""
            INSERT INTO livros (titulo, autor, livro)
            VALUES
                ('Vidas secas', 'Graciliamo Ramos', 0),
                ('A hora da estrela', 'Clarice Lispector', 1),
                ('Dom Casmurro', 'Machado de Assis', 2)

        """)
                
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")