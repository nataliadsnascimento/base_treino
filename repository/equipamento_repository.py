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

    def list(self):
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, nome, descricao, patrimonio, vendido
                FROM equipamentos
            """)

            registros = cursor.fetchall()

            equipamentos = []

            for registro in registros:
                equipamento = Equipamento(
                    id=registro[0],
                    nome=registro[1],
                    descricao=registro[2],
                    patrimonio=registro[3],
                    vendido=bool(registro[4])
                )

                equipamentos.append(equipamento)

            return equipamentos

        finally:
            connection.close()

    def get(self, equipamento_id):
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, nome, descricao, patrimonio, vendido
                FROM equipamentos
                WHERE id = ?
            """, (equipamento_id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            equipamento = Equipamento(
                id=registro[0],
                nome=registro[1],
                descricao=registro[2],
                patrimonio=registro[3],
                vendido=bool(registro[4])
            )

            return equipamento

        finally:
            connection.close()
            
    def update(self, equipamento):
        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE equipamentos
                SET nome = ?,
                    descricao = ?,
                    patrimonio = ?
                WHERE id = ?
            """, (
                equipamento.nome,
                equipamento.descricao,
                equipamento.patrimonio,
                equipamento.id
            ))

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()