class FilmeUI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n=== GERENCIADOR DE FILMES ===")
            print("1 - Cadastrar filme")
            print("2 - Listar filmes")
            print("3 - Buscar filme por ID")
            print("4 - Atualizar filme")
            print("5 - Excluir filme")
            print("6 - Marcar filme como assistido")
            print("7 - Reabrir filme (não assistido)")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            try:
                if opcao == "1":
                    self._cadastrar()
                elif opcao == "2":
                    self._listar()
                elif opcao == "3":
                    self._buscar_por_id()
                elif opcao == "4":
                    self._atualizar()
                elif opcao == "5":
                    self._excluir()
                elif opcao == "6":
                    self._marcar_assistido()
                elif opcao == "7":
                    self._reabrir()
                elif opcao == "0":
                    print("Saindo do gerenciador de filmes...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError as e:
                print(f"Erro: {e}")

    def _ler_id(self):
        valor = input("Digite o ID do filme: ").strip()
        if not valor.isdigit():
            raise ValueError("O ID deve ser um número inteiro válido.")
        return int(valor)

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

    def _buscar_por_id(self):
        filme_id = self._ler_id()
        filme = self.services.get(filme_id)
        status = self._formatar_status(filme.assistido)
        print(f"\nID: {filme.id}")
        print(f"Título: {filme.titulo}")
        print(f"Descrição: {filme.descricao or '(sem descrição)'}")
        print(f"Situação: {status}")

    def _atualizar(self):
        filme_id = self._ler_id()
        filme_atual = self.services.get(filme_id)
        print(f"Atualizando: {filme_atual.titulo}")
        novo_titulo = input("Novo título: ")
        nova_descricao = input("Nova descrição (opcional): ")
        filme = self.services.update(filme_id, novo_titulo, nova_descricao)
        print(f"Filme ID {filme.id} atualizado com sucesso!")

    def _excluir(self):
        filme_id = self._ler_id()
        self.services.delete(filme_id)
        print(f"Filme ID {filme_id} excluído com sucesso!")

    def _marcar_assistido(self):
        filme_id = self._ler_id()
        filme = self.services.marcar_assistido(filme_id)
        print(f"Filme '{filme.titulo}' marcado como assistido!")

    def _reabrir(self):
        filme_id = self._ler_id()
        filme = self.services.reabrir(filme_id)
        print(f"Filme '{filme.titulo}' reaberto como pendente!")