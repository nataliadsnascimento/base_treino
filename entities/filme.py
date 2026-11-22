class Filme:

    def __init__(self, titulo, descricao="", assistido=False, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.assistido = bool(assistido)