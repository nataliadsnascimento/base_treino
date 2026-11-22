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

    def update(self, filme_id, titulo, descricao=""):
        filme_existente = self.get(filme_id)
        if not titulo or not titulo.strip():
            raise ValueError("O título do filme é obrigatório e não pode estar em branco.")
        filme_existente.titulo = titulo.strip()
        filme_existente.descricao = (descricao or "").strip()
        self.repository.update(filme_existente)
        return filme_existente

    def concluir(self, filme_id):
        filme = self.get(filme_id)
        if filme.assistido:
            raise ValueError(f"O filme '{filme.titulo}' já está marcado como assistido.")
        self.repository.update_status(filme_id, True)
        filme.assistido = True
        return filme

    def reabrir(self, filme_id):
        filme = self.get(filme_id)
        if not filme.assistido:
            raise ValueError(f"O filme '{filme.titulo}' já está marcado como pendente.")
        self.repository.update_status(filme_id, False)
        filme.assistido = False
        return filme

    def delete(self, filme_id):
        self.get(filme_id)
        return self.repository.delete(filme_id)