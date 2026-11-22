from database.connection import get_connection
from entity.livro import livro

class DAOEntity:

    def create(self, livro):
        connection = get_connection()
        
        try:
            connection.execute("""
                INSERT INTO livros (titulo, autor, lido)
                VALUES (?, ?, ?)
            """,(livro.titulo, livro.autor, livro.lido))
            
            connection.commit()            
        finally:
            connection.close()

    def find_all(self):
        connection = get_connection()
        
        try:
            
            cursor = connection.execute("SELECT * FROM livros")
            registros = cursor.fetchall()
            
            
            livros = []
        
        for registro in registros:
            Book = livro(
                id=registro[0],
                titulo=registro[1],
                autor=registro[2],
                lido=bool(registro[3])
            )

            livros.append(livro)

        return livros

    finally:
        connection.close()
        
    def find_by_id(self, livro_id):
    connection = get_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM livros WHERE id = ?",
            (livro_id,)
        )

        registro = cursor.fetchone()

        if registro is None:
            return None

        livro = Livro(
            id=registro[0],
            titulo=registro[1],
            autor=registro[2],
            lido=bool(registro[3])
        )

        return livro

    finally:
        connection.close()

    def update(self, livro):
    connection = get_connection()

    try:
        connection.execute("""
            UPDATE livros
            SET titulo = ?, autor = ?
            WHERE id = ?
        """, (livro.titulo, livro.autor, livro.id))

        connection.commit()

    finally:
        connection.close()
        
    def delete(self, task_id):
        # Excluir
        pass
    