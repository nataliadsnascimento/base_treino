from entities.equipamento import Equipamento
from repository.equipamento_repository import EquipamentoRepository


class EquipamentoService:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome, descricao, patrimonio):

        # Validar dados
        if not nome.strip():
            raise ValueError("O nome do equipamento é obrigatório.")

        # Criar entidade
        equipamento = Equipamento(
            id=None,
            nome=nome.strip(),
            descricao=descricao,
            patrimonio=patrimonio,
            vendido=False
        )

        # Solicitar persistência
        return self.repository.create(equipamento)
    
    def list(self):
        return self.repository.list()
    
    def get(self, equipamento_id):

        if equipamento_id <= 0:
            raise ValueError("O ID deve ser maior que zero.")

        equipamento = self.repository.get(equipamento_id)

        if equipamento is None:
            raise ValueError("Equipamento não encontrado.")

        return equipamento