from db import createPlace, createUser, createAddress, searchCategoryByName, categorizePlace, createCategory
from models import User, Place, Address, Category
from constants import COMMON, CORPORATE, NGO, TAB
from models import Address

def loadSignupComponent():
    while True:
        option = int(input("""
            O que você deseja cadastrar?\n
            1- Usuário comum
            2- Estabelecimento comercial
            3- ONG

            opção: """).strip())

        if option == 1:
            user = User
            user.email = input(f"\n{TAB}# Digite seu email: ").strip()
            user.password = input(f"{TAB}# Digite sua senha: ").strip()
            user.first_name = input(f"{TAB}# Digite seu primeiro nome: ").strip()
            user.last_name = input(f"{TAB}# Digite seu sobrenome: ").strip()
            user.lat, user.lng = input(f"{TAB}# Marque no mapa as suas coordenadas atuais: ").strip().split(",")
            user.profile = "COMMON"
            user.cnpj = None

            createUser(user.email, user.password, user.cnpj, user.first_name, user.last_name, user.profile, user.lat, user.lng, address_id=None)

            print(f"\n{TAB}# Usuário comum cadastrado com sucesso")

            break
        elif option == 2:
            lugar = Place
            endereco = Address
            lugar.cnpj = input(f"\n{TAB}# Digite o CNPJ do estabelecimento: ").strip()
            lugar.name = input(f"{TAB}# Digite o nome do estabelecimento: ").strip()
            lugar.description = input(f"{TAB}# Digite a descrição do estabelecimento: ").strip()
            lugar.manager_id = input(f"{TAB}# Digite o id do gestor do estabelecimento na plataforma: ").strip()

            category_name = input(f"{TAB}# Digite o tipo do estabelecimento: ").strip()

            found_category = searchCategoryByName(category_name)

            if(found_category == null):
                categoria = Category
                categoria.name = category_name
                categoria.description = input(f"{TAB}# Digite a descrição do tipo do estabelecimento: ").strip()
                category = createCategory(categoria)
            else:
                category = found_category

            endereco.neighborhood = input(f"{TAB}# Digite o bairro do estabelecimento: ").strip()
            endereco.street = input(f"{TAB}# Digite a rua e número(se houver) do estabelecimento: ").strip()
            endereco.street2 = input(f"{TAB}# Digite (se houver) o complemento do endereço do estabelecimento: ").strip()
            endereco.lat, endereco.lng = input(f"{TAB}# Marque no mapa a coordenada do estabelecimento: ").strip().split(",")

            address = createAddress(endereco)
            lugar.address_id = address.id

            place = createPlace(lugar)

            place_category = categorizePlace(category.id, place.id)

            while True:
                option = input(f"{TAB}# Deseja adicionar alguma vantagem do estabelecimento? (S/N): ").strip().lower()[0]
            
                if option == "s":
                    benefit = input(f"{TAB}# Digite a vantagem: ").strip()
                    place.addBenefit(benefit)
                else:
                    break

            option = input(f"{TAB}# Deseja adicionar um usuário para este estabelecimento? (S/N): ").strip().lower()[0]

            if option == "s":
                user.email = input(f"\n{TAB}# Digite seu email: ").strip()
                user.password = input(f"{TAB}# Digite sua senha: ").strip()
                user.first_name = input(f"{TAB}# Digite seu primeiro nome: ").strip()
                user.last_name = input(f"{TAB}# Digite seu sobrenome: ").strip()
                user.cnpj = input(f"{TAB}# Digite seu cnpj: ").strip()
                user.lat, user.lng = input(f"{TAB}# Marque no mapa as suas coordenadas atuais: ").strip().split(",")
                user.profile = "CORPORATE"

                createUser(user.email, user.password, user.cnpj, user.first_name, user.last_name, user.profile, user.lat, user.lng, address_id=None)

            print(f"\n{TAB}# Estabelecimento comercial cadastrado com sucesso")
            break
        elif option == 3:
            endereco = Address
            lugar = Place
            lugar.cpnj = input(f"\n{TAB}# Digite o CNPJ da ONG: ").strip()
            lugar.name = input(f"{TAB}# Digite o nome da ONG: ").strip()
            lugar.description = input(f"{TAB}# Digite a descrição da ONG: ").strip()

            endereco.neighborhood = input(f"{TAB}# Digite o bairro da ONG: ").strip()
            endereco.street = input(f"{TAB}# Digite a rua e número(se houver) da ONG: ").strip()
            endereco.street2 = input(f"{TAB}# Digite (se houver) o complemento do endereço da ONG: ").strip()
            endereco.lat, endereco.lng = input(f"{TAB}# Marque no mapa a coordenada da ONG: ").strip().split(",")

            address = createAddress(endereco)
            lugar.address_id = address.id

            place = createPlace(lugar)

            while True:
                option = input(f"{TAB}# Deseja adicionar algum projeto da ONG? (S/N): ").strip().lower()[0]
            
                if option == "s":
                    project = input(f"{TAB}# Digite o nome do projeto: ").strip()
                    place.addProjects(project)
                else:
                    break

            option = input(f"{TAB}# Deseja adicionar um usuário para esta ONG? (S/N): ").strip().lower()[0]

            if option == "s":
                email = input(f"\n{TAB}# Digite seu email: ").strip()
                password = input(f"{TAB}# Digite sua senha: ").strip()
                first_name = input(f"{TAB}# Digite seu primeiro nome: ").strip()
                last_name = input(f"{TAB}# Digite seu sobrenome: ").strip()
                profile = "NGO"
                cnpj= NULL

                createUser(email, password, cnpj, first_name, last_name, profile)

            print(f"\n{TAB}# Estabelecimento comercial cadastrado com sucesso")
            break
        else:
            print(f"\n{TAB}# Opção inválida")
            continue
    