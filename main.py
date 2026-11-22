from install import install

from interface.equipamento_menu import EquipamentoMenu
from service.equipamento_service import EquipamentoService
from repository.equipamento_repository import EquipamentoRepository


def main():

    install()

    equipamento_repository = EquipamentoRepository()
    equipamento_service = EquipamentoService(equipamento_repository)
    equipamento_menu = EquipamentoMenu(equipamento_service)

    while True:

        print("\n===== SISTEMA GERENCIADOR =====")
        print("1 - Gerenciar equipamentos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            equipamento_menu.show_principal_menu()

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()