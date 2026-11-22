from database.connection import get_connection
from entities.livro import livro

class DAOLivro:

    def create(self, livro_obj):
        connection = get_connection()

        try:
            cursor = connection.execute("""
                INSERT INTO livros (titulo, autor, lido)
                VALUES (?, ?, ?)
            """,(livro_obj.titulo, livro_obj.autor, int(livro_obj.lido)))
            
            connection.commit()
            return cursor.lastrowid

        finally:
            connection.close()

    def find_all(self):
        connection = get_connection()

        try:
            
            cursor = connection.execute("SELECT id, titulo, autor, lido FROM livros")
            registros = cursor.fetchall()

            livros = []
        
            for registro in registros:
                item = livro(
                    id=registro[0],
                    titulo=registro[1],
                    autor=registro[2],
                    lido=bool(registro[3])
                )

                livros.append(item)
            return livros

        finally:
            connection.close()

    def find_by_id(self, livro_id):
        connection = get_connection()

        try:
            cursor = connection.execute(
                "SELECT id, titulo, autor, lido FROM livros WHERE id = ?",
                (livro_id,)
            )

            registro = cursor.fetchone()

            if registro is None:
                return None

            item = livro(
                id=registro[0],
                titulo=registro[1],
                autor=registro[2],
                lido=bool(registro[3])
            )
            return item
        finally:
            connection.close()

    def update(self, livro_obj):
        connection = get_connection()

        try:
            connection.execute("""
                UPDATE livros
                SET titulo = ?, autor = ?, lido = ?
                WHERE id = ?
            """, (livro_obj.titulo, livro_obj.autor, int(livro_obj.lido), livro_obj.id))

            connection.commit()

        finally:
            connection.close()

    def delete(self, livro_id):
        connection = get_connection()

        try:
            connection.execute(
                "DELETE FROM livros WHERE id = ?",
                (livro_id,)
            )

            connection.commit()

        finally:
            connection.close()
