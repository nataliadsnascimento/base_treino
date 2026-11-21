from database.connection import get_connection


def install():
    connection = get_connection()

    try:
        # Criar tabela de equipamentos
        connection.execute("""
            CREATE TABLE IF NOT EXISTS equipamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                patrimonio TEXT,
                vendido INTEGER NOT NULL DEFAULT 0
            )
        """)

        # Verificar se existem equipamentos cadastrados
        cursor = connection.execute(
            "SELECT COUNT(*) FROM equipamentos"
        )
        quantidade = cursor.fetchone()[0]

        # Inserir dados iniciais
        if quantidade == 0:
            connection.executemany("""
                INSERT INTO equipamentos
                (nome, descricao, patrimonio, vendido)
                VALUES (?, ?, ?, ?)
            """, [
                ("Notebook Asus", "Ryzen 7", "PAT001", 0),
                ("Monitor Dell", "24 polegadas", "PAT002", 0),
                ("Impressora HP", "Multifuncional", "PAT003", 0)
            ])

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")