from repository.dao_livro import DAOLivro
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

    def get(self, livro_id):
        item = self.repository.find_by_id(livro_id)

        if item is None:
            raise ValueError("Livro não encontrado!")

        return item
    
    def update(self, livro_id, titulo, autor=None, lido=None):
        item = self.repository.find_by_id(livro_id)

        if item is None:
            raise ValueError("Livro não encontrado!")

        if not titulo or not titulo.strip():
            raise ValueError("O título do livro é obrigatório!")

        item.titulo = titulo.strip()
        item.autor = autor.strip() if autor and autor.strip() else None
        if lido is not None:
            item.lido = bool(lido)
        
        self.repository.update(item)

        return item
    
    def delete(self, livro_id):
        item = self.repository.find_by_id(livro_id)

        if item is None:
            raise ValueError("Livro não encontrado!")

        self.repository.delete(livro_id)
        