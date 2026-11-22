class EquipamentoMenu:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):

        while True:
            print("\n===== MENU DE EQUIPAMENTOS =====")
            print("1 - Cadastrar equipamento")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.create()

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