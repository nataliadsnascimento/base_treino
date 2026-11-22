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
    
    def update(self, equipamento_id, nome, descricao, patrimonio):

        equipamento = self.get(equipamento_id)

        if not nome.strip():
            raise ValueError("O nome do equipamento é obrigatório.")

        equipamento.nome = nome.strip()
        equipamento.descricao = descricao
        equipamento.patrimonio = patrimonio

        if not self.repository.update(equipamento):
            raise ValueError("Não foi possível atualizar o equipamento.")

        return equipamento
    
    def delete(self, equipamento_id):

        self.get(equipamento_id)

        if not self.repository.delete(equipamento_id):
            raise ValueError("Não foi possível excluir o equipamento.")

        return True
    
             
    def sell(self, equipamento_id):

        equipamento = self.get(equipamento_id)

        if equipamento.vendido:
            raise ValueError("Equipamento já está vendido.")

        if not self.repository.sell(equipamento_id):
            raise ValueError("Não foi possível realizar a venda.")

        return True
    
    def undo_sale(self, equipamento_id):

        equipamento = self.get(equipamento_id)

        if not equipamento.vendido:
            raise ValueError("Equipamento não está vendido.")

        if not self.repository.undo_sale(equipamento_id):
            raise ValueError("Não foi possível desfazer a venda.")

        return True