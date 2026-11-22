from repository.dao_entity import DAOEntity
from entities.livro import livro

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo, autor=None):
        if not titulo or not titulo.strip():
            raise ValueError("O título do livro é obrigatório!")

        novo_livro = livro(
            titulo=titulo.strip(),
            autor=autor.strip() if autor and autor.strip() else None,
            lido=False
        )

        novo_livro.id = self.repository.create(novo_livro)
        return novo_livro
    
    def list(self):
        return self.repository.find_all()

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass