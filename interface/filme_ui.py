class FilmeUI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n=== GERENCIADOR DE FILMES ===")
            print("1 - Cadastrar filme")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            try:
                if opcao == "1":
                    self._cadastrar()
                elif opcao == "0":
                    print("Saindo do gerenciador de filmes...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError as e:
                print(f"Erro: {e}")

    def _cadastrar(self):
        titulo = input("Título do filme: ")
        descricao = input("Descrição (opcional): ")
        filme = self.services.create(titulo, descricao)
        print(f"Filme '{filme.titulo}' cadastrado com sucesso! (ID: {filme.id})")