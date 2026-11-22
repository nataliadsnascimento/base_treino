class Equipamento:
    def __init__(self, id, nome, descricao, patrimonio, vendido=False):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.patrimonio = patrimonio
        self.vendido = vendido