from entities.filme import Filme
from repository.dao_filme import DAOFilme

class FilmeService:

    def __init__(self, repository=None):
        self.repository = repository if repository is not None else DAOFilme()

    def create(self, titulo, descricao=""):
        if not titulo or not titulo.strip():
            raise ValueError("O título do filme é obrigatório e não pode estar vazio.")
        
        filme = Filme(
            titulo=titulo.strip(),
            descricao=descricao.strip() if descricao else "",
            assistido=False
        )
        return self.repository.create(filme)

    def list(self):
        return self.repository.find_all()

    def get(self, filme_id):
        filme = self.repository.find_by_id(filme_id)
        if filme is None:
            raise ValueError(f"Filme com ID {filme_id} não encontrado.")
        return filme

    def update(self, filme_id, titulo, descricao=""):
        if not titulo or not titulo.strip():
            raise ValueError("O título do filme é obrigatório e não pode estar vazio.")
        
        filme = self.get(filme_id)
        filme.titulo = titulo.strip()
        filme.descricao = descricao.strip() if descricao else ""
        self.repository.update(filme)
        return filme

    def delete(self, filme_id):
        self.get(filme_id)
        self.repository.delete(filme_id)

    def marcar_assistido(self, filme_id):
        filme = self.get(filme_id)
        if filme.assistido:
            raise ValueError("Este filme já está marcado como assistido.")
        self.repository.atualizar_status(filme_id, True)
        filme.assistido = True
        return filme

    def reabrir(self, filme_id):
        filme = self.get(filme_id)
        if not filme.assistido:
            raise ValueError("Este filme já está pendente (não assistido).")
        self.repository.atualizar_status(filme_id, False)
        filme.assistido = False
        return filme