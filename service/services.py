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
        livro = self.repository.find_by_id(livro_id)

        if livro is None:
            raise ValueError("Livro não encontrado!")

        return livro
    
    def update(self, livro_id, titulo, autor=None):
        livro = self.repository.find_by_id(livro_id)

        if livro is None:
            raise ValueError("Livro não encontrado!")

        if not titulo or not titulo.strip():
            raise ValueError("O título do livro é obrigatório!")

        livro.titulo = titulo.strip()
        livro.autor = autor.strip() if autor and autor.strip() else None

        self.repository.update(livro)

        return livro
    
    def delete(self, task_id):
        pass