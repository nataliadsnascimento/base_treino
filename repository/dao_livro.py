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
        # Consultar todas as entidades
        pass

    def find_by_id(self, task_id):
        # Consultar pelo ID
        pass

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass
    