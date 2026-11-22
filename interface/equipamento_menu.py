class EquipamentoMenu:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):

        while True:
            print("\n===== MENU DE EQUIPAMENTOS =====")
            print("1 - Cadastrar equipamento")
            print("2 - Listar equipamentos")
            print("3 - Buscar equipamento por ID")
            print("4 - Atualizar equipamento")
            print("5 - Excluir equipamento")
            print("6 - Marcar equipamento como vendido")
            print("7 - Desfazer venda de equipamento")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.create()

            elif opcao == "2":
                self.list()

            elif opcao == "3":
                self.get()

            elif opcao == "4":
                self.update()

            elif opcao == "5":
                self.delete()

            elif opcao == "6":
                self.sell()

            elif opcao == "7":
                self.undo_sale()

            elif opcao == "0":
                print("Encerrando menu...")
                break

            else:
                print("Opção inválida.")

    def create(self):

        print("\n===== CADASTRO DE EQUIPAMENTO =====")

        nome = input("Nome: ")
        descricao = input("Descrição: ")
        patrimonio = input("Patrimônio: ")

        try:
            id_equipamento = self.services.create(
                nome,
                descricao,
                patrimonio
            )

            print("Equipamento cadastrado com sucesso!")
            print(f"ID: {id_equipamento}")

        except ValueError as erro:
            print(f"Erro: {erro}")

    def list(self):

        print("\n===== LISTAGEM DE EQUIPAMENTOS =====")

        equipamentos = self.services.list()

        if not equipamentos:
            print("Nenhum equipamento cadastrado.")
            return

        for equipamento in equipamentos:

            status = "Vendido" if equipamento.vendido else "Disponível"

            print(f"ID: {equipamento.id}")
            print(f"Nome: {equipamento.nome}")
            print(f"Descrição: {equipamento.descricao}")
            print(f"Patrimônio: {equipamento.patrimonio}")
            print(f"Status: {status}")
            print("-" * 35)

    def get(self):

        print("\n===== BUSCA DE EQUIPAMENTO =====")

        try:
            equipamento_id = int(input("Informe o ID: "))

        except ValueError:
            print("Erro: Informe um ID válido.")
            return

        try:
            equipamento = self.services.get(equipamento_id)

            status = "Vendido" if equipamento.vendido else "Disponível"

            print(f"ID: {equipamento.id}")
            print(f"Nome: {equipamento.nome}")
            print(f"Descrição: {equipamento.descricao}")
            print(f"Patrimônio: {equipamento.patrimonio}")
            print(f"Status: {status}")
            print("-" * 35)

        except ValueError as erro:
            print(f"Erro: {erro}")

    def update(self):

        print("\n===== ATUALIZAÇÃO DE EQUIPAMENTO =====")

        try:
            equipamento_id = int(input("Informe o ID: "))

        except ValueError:
            print("Erro: Informe um ID válido.")
            return

        try:
            equipamento = self.services.get(equipamento_id)

            print("\nDados atuais:")
            print(f"Nome: {equipamento.nome}")
            print(f"Descrição: {equipamento.descricao}")
            print(f"Patrimônio: {equipamento.patrimonio}")

            print("\nInforme os novos dados:")

            nome = input("Novo nome: ")
            descricao = input("Nova descrição: ")
            patrimonio = input("Novo patrimônio: ")

            self.services.update(
                equipamento_id,
                nome,
                descricao,
                patrimonio
            )

            print("Equipamento atualizado com sucesso!")

        except ValueError as erro:
            print(f"Erro: {erro}")

    def delete(self):

        print("\n===== EXCLUSÃO DE EQUIPAMENTO =====")

        try:
            equipamento_id = int(input("Informe o ID: "))

        except ValueError:
            print("Erro: Informe um ID válido.")
            return

        try:
            equipamento = self.services.get(equipamento_id)

            print(f"ID: {equipamento.id}")
            print(f"Nome: {equipamento.nome}")

            confirmacao = input(
                "Confirma a exclusão? (s/n): "
            ).strip().lower()

            if confirmacao == "s":

                self.services.delete(equipamento_id)

                print("Equipamento excluído com sucesso!")

            else:
                print("Exclusão cancelada.")

        except ValueError as erro:
            print(f"Erro: {erro}")

    def sell(self):

        print("\n===== VENDA DE EQUIPAMENTO =====")

        try:
            equipamento_id = int(input("Informe o ID: "))

        except ValueError:
            print("Erro: Informe um ID válido.")
            return

        try:
            equipamento = self.services.get(equipamento_id)

            if equipamento.vendido:
                raise ValueError("Equipamento já está vendido.")

            print(f"ID: {equipamento.id}")
            print(f"Nome: {equipamento.nome}")
            print(f"Patrimônio: {equipamento.patrimonio}")

            confirmacao = input(
                "Confirma a venda? (s/n): "
            ).strip().lower()

            if confirmacao == "s":

                self.services.sell(equipamento_id)

                print("Equipamento marcado como vendido com sucesso!")

            else:
                print("Venda cancelada.")

        except ValueError as erro:
            print(f"Erro: {erro}")

    def undo_sale(self):

        print("\n===== DESFAZER VENDA DE EQUIPAMENTO =====")

        try:
            equipamento_id = int(input("Informe o ID: "))

        except ValueError:
            print("Erro: Informe um ID válido.")
            return

        try:
            equipamento = self.services.get(equipamento_id)

            if not equipamento.vendido:
                raise ValueError("Equipamento não está vendido.")

            print(f"ID: {equipamento.id}")
            print(f"Nome: {equipamento.nome}")
            print(f"Patrimônio: {equipamento.patrimonio}")

            confirmacao = input(
                "Confirma desfazer a venda? (s/n): "
            ).strip().lower()

            if confirmacao == "s":

                self.services.undo_sale(equipamento_id)

                print("Venda desfeita com sucesso!")
                print("Equipamento disponível novamente.")

            else:
                print("Operação cancelada.")

        except ValueError as erro:
            print(f"Erro: {erro}")