from install import install

from interface.equipamento_menu import EquipamentoMenu
from service.equipamento_service import EquipamentoService
from repository.equipamento_repository import EquipamentoRepository

from interface.livro_ui import LivroUi
from service.livro_services import Services
from repository.dao_livro import DAOLivro

from interface.filme_ui import FilmeUI
from service.filme_service import FilmeService
from repository.dao_filme import DAOFilme


def main():
    install()

    equipamento_repository = EquipamentoRepository()
    equipamento_service = EquipamentoService(equipamento_repository)
    equipamento_menu = EquipamentoMenu(equipamento_service)

    livro_repository = DAOLivro()
    livro_service = Services(livro_repository)
    livro_menu = LivroUi(livro_service)

    filme_repository = DAOFilme()
    filme_service = FilmeService(filme_repository)
    filme_menu = FilmeUI(filme_service)

    while True:
        print("\n===== SISTEMA GERENCIADOR =====")
        print("1 - Gerenciar equipamentos")
        print("2 - Gerenciar livros")
        print("3 - Gerenciar filmes")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            equipamento_menu.show_principal_menu()
        elif opcao == "2":
            livro_menu.show_principal_menu()
        elif opcao == "3":
            filme_menu.show_principal_menu()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()