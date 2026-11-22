from entities.filme import Filme

class FilmeService:

    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo, descricao=""):
        if not titulo or not titulo.strip():
            raise ValueError("O título do filme é obrigatório e não pode estar em branco.")
        novo_filme = Filme(titulo=titulo.strip(), descricao=(descricao or "").strip(), assistido=False)
        return self.repository.create(novo_filme)

    def list(self):
        return self.repository.find_all()

    def get(self, filme_id):
        filme = self.repository.find_by_id(filme_id)
        if not filme:
            raise ValueError(f"Filme com ID {filme_id} não encontrado.")
        return filme