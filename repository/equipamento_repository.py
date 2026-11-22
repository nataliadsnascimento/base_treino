from database.connection import get_connection
from entities.equipamento import Equipamento


class EquipamentoRepository:

    def create(self, equipamento):
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO equipamentos
                (nome, descricao, patrimonio, vendido)
                VALUES (?, ?, ?, ?)
            """, (
                equipamento.nome,
                equipamento.descricao,
                equipamento.patrimonio,
                equipamento.vendido
            ))

            equipamento.id = cursor.lastrowid

            connection.commit()

            return equipamento.id

        finally:
            connection.close()