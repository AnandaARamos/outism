from components.signinComponent import loadSigninComponent
from components.signupComponent import loadSignupComponent
from components.placesComponent import loadPlacesComponent
from components.ratingComponent import loadRatingComponent
from components.chatComponent import loadChatComponent
from models import User


def main():
    while True:

        option = int(input("""
        O que você quer fazer?\n
        1- login
        2- cadastro

        opção: """).strip())

        if option == 1:
            user = loadSigninComponent()
        elif option == 2:
            loadSignupComponent()
            continue
        else:
            print("\nOpção inválida")
            continue

        if user == None:
            # caso o usuário não tenha sido autenticado ainda, volta para o menu inicial
            continue

        elif user['profile'] == "COMMON":
            option = int(input("""
            O que você quer fazer?\n
            1- Pesquisar locais
            2- Chat
    
             opção: """).strip())

            if option == 1:
                  loadPlacesComponent(user)
            elif option == 2:
                 loadChatComponent(user['profile'])
            else:
                print("\nOpção inválida")
                continue
        elif user['profile'] == "CORPORATE":
            option = int(input("""
            O que você quer fazer?\n
                1- Ver avaliações
                2- Chat
    
                opção: """).strip())

            if option == 1:
                loadRatingComponent(user)
            elif option == 2:
                loadChatComponent(user['profile'])
            else:
                print("\nOpção inválida")
                continue
        elif user['profile'] == "NGO":
            loadChatComponent(user['profile'])

if __name__ == '__main__':
    main()
