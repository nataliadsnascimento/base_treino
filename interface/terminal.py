class Terminal:
    
    def __init__(self, service):
        self.service = service

    def menu(self):
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
                    self.cadastrar()

                elif opcao == "2":
                    self.listar()

                elif opcao == "3":
                    self.buscar()

                elif opcao == "4":
                    self.atualizar()

                elif opcao == "5":
                    self.excluir()

                elif opcao == "0":
                    print("Encerrando o sistema...")
                    break

                else:
                    print("Opção inválida!")

            except ValueError as erro:
                print(f"Erro: {erro}")

    def cadastrar(self):
        titulo = input("Título: ")
        autor = input("Autor: ")

        livro = self.service.create(titulo, autor)

        print(f"Livro cadastrado! ID: {livro.id}")

    def listar(self):
        livros = self.service.list()

        if not livros:
            print("Nenhum livro cadastrado.")
            return

        for livro in livros:
            status = "Lido" if livro.lido else "Não lido"
            print(f"\nID: {livro.id}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Status: {status}")

    def buscar(self):
        livro_id = int(input("Digite o ID: "))
        livro = self.service.get(livro_id)

        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")

    def atualizar(self):
        livro_id = int(input("Digite o ID do livro: "))
        titulo = input("Novo título: ")
        autor = input("Novo autor: ")

        self.service.update(livro_id, titulo, autor)

        print("Livro atualizado com sucesso!")

    def excluir(self):
        livro_id = int(input("Digite o ID do livro: "))

        self.service.delete(livro_id)

        print("Livro excluído com sucesso!")