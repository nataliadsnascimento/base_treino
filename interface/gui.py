from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n===== SISTEMA DE LIVROS =====")
            print("1 - Cadastrar livro")
            print("2 - Listar livros")
            print("3 - Buscar livro por ID")
            print("4 - Atualizar livro")
            print("5 - Excluir livro")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            try:
                if opcao == "1":
                    self.cadastrar_livro()

                elif opcao == "2":
                    self.listar_livros()

                elif opcao == "3":
                    self.buscar_livro()

                elif opcao == "4":
                    self.atualizar_livro()

                elif opcao == "5":
                    self.excluir_livro()

                elif opcao == "0":
                    print("Encerrando o sistema...")
                    break

                else:
                    print("Opção inválida!")

            except ValueError as erro:
                print(f"Erro: {erro}")

    def cadastrar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")

        livro = self.services.create(titulo, autor)

        print(f"\nLivro cadastrado com sucesso! ID: {livro.id}")

    def listar_livros(self):
        livros = self.services.list()

        if not livros:
            print("\nNenhum livro cadastrado.")
            return

        print("\n===== LIVROS CADASTRADOS =====")

        for livro in livros:
            status = "Lido" if livro.lido else "Não lido"

            print(f"\nID: {livro.id}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor or 'Não informado'}")
            print(f"Status: {status}")

    def buscar_livro(self):
        livro_id = int(input("Digite o ID do livro: "))

        livro = self.services.get(livro_id)

        print(f"\nID: {livro.id}")
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor or 'Não informado'}")

    def atualizar_livro(self):
        livro_id = int(input("Digite o ID do livro: "))
        titulo = input("Novo título: ")
        autor = input("Novo autor: ")

        self.services.update(livro_id, titulo, autor)

        print("\nLivro atualizado com sucesso!")

    def excluir_livro(self):
        livro_id = int(input("Digite o ID do livro: "))

        self.services.delete(livro_id)

        print("\nLivro excluído com sucesso!")
