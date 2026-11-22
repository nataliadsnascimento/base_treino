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