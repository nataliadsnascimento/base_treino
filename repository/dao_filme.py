from database.connection import get_connection
from entities.filme import Filme

class DAOFilme:

    def create(self, filme):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO filmes (titulo, descricao, assistido) VALUES (?, ?, ?)",
                (filme.titulo, filme.descricao, int(filme.assistido))
            )
            connection.commit()
            filme.id = cursor.lastrowid
            return filme
        finally:
            connection.close()