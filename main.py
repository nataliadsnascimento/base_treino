from install import install
from interface.gui import UI
from service.services import Services
from repository.dao_entity import DAOEntity


from interface.filme_ui import FilmeUI
from service.filme_service import FilmeService
from repository.dao_filme import DAOFilme


def main():
    install()

    while True:
        print("\n1. Entidade | 2. Filmes | 0. Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            UI(Services(DAOEntity())).show_principal_menu()
        elif opcao == "2":
            FilmeUI(FilmeService(DAOFilme())).show_principal_menu()
        elif opcao == "0":
            break


if __name__ == "__main__":
    main()