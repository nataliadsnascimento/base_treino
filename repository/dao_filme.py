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

    def find_all(self):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id, titulo, descricao, assistido FROM filmes")
            rows = cursor.fetchall()
            return [
                Filme(id=row[0], titulo=row[1], descricao=row[2], assistido=bool(row[3]))
                for row in rows
            ]
        finally:
            connection.close()

    def find_by_id(self, filme_id):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT id, titulo, descricao, assistido FROM filmes WHERE id = ?",
                (filme_id,)
            )
            row = cursor.fetchone()
            if row:
                return Filme(id=row[0], titulo=row[1], descricao=row[2], assistido=bool(row[3]))
            return None
        finally:
            connection.close()

    def update(self, filme):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE filmes SET titulo = ?, descricao = ? WHERE id = ?",
                (filme.titulo, filme.descricao, filme.id)
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()

    def delete(self, filme_id):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM filmes WHERE id = ?", (filme_id,))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()