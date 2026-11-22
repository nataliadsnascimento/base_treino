class FilmeUI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n=== GERENCIADOR DE FILMES ===")
            print("1 - Cadastrar filme")
            print("2 - Listar filmes")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            try:
                if opcao == "1":
                    self._cadastrar()
                elif opcao == "2":
                    self._listar()
                elif opcao == "0":
                    print("Saindo do gerenciador de filmes...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError as e:
                print(f"Erro: {e}")

    def _formatar_status(self, assistido):
        return "Assistido" if assistido else "Pendente"

    def _cadastrar(self):
        titulo = input("Título do filme: ")
        descricao = input("Descrição (opcional): ")
        filme = self.services.create(titulo, descricao)
        print(f"Filme '{filme.titulo}' cadastrado com sucesso! (ID: {filme.id})")

    def _listar(self):
        filmes = self.services.list()
        if not filmes:
            print("Nenhum filme cadastrado.")
            return
        print("\n--- Lista de Filmes ---")
        for filme in filmes:
            status = self._formatar_status(filme.assistido)
            print(f"[{filme.id}] {filme.titulo} - {status}")
            if filme.descricao:
                print(f"    Descrição: {filme.descricao}")