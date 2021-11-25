from constants import TAB
from models import User
from db import validateUser


def loadSigninComponent():
    while True:
        email = input(f"\n{TAB}# Digite seu email: ").strip()
        password = input(f"{TAB}# Digite sua senha: ").strip()

        user = validateUser(email, password)

        if user == None:
            print(f"\n{TAB}# Email ou senha inválidos")
            continue
        else:
            break

    print(f"\n{TAB}# Acesso realizado com sucesso")
    return user



