# FUNCIONALIDADES:
# Atribuir um local a uma nota (certo local recebeu tais avaliações) --> ok
# busca com que notas cada local recebeu --> ok
# Exibir que avaliações determinado usuário fez --> PENDENTE
# Erro principal: se um usuario digitar um produto inexistente ele nao exibe nada

from db import searchPlaces, searchPlaceRatings, searchPlacesByCNPJ
from constants import NGO, TAB
from models import User


# Usuário vai atribuir uma nota a um estabelecimento escolhido pelo nome
# Essas notas serão guardadas em uma LISTA, ao exibir essas notas em uma outra funcionalidade é melhor exibir a MEDIA
# MEDIA = sum(places[index][6])/len(places[index][6])

def loadRatingComponent(user):
    while True:
        user_locals = searchPlacesByCNPJ(user['cnpj'])

        print(f"\n{TAB}# Local(is): ")
        for i, user_local in enumerate(user_locals):
            print(f"{TAB}{i + 1}- ", end="")  # imprime a lista q aparece na tela como resultado da busca
            print(f"{user_locals[i].id}, {user_locals[i].name}",
                  end="")  # imprime a lista q aparece na tela como resultado da busca
            if place.type == NGO:
                print(" (ONG)", end="")
            print()

        place_id = input(f"\n{TAB}Digite o identificador (id) do lugar que desejar visualizar as avaliações: ").strip()

        if entrada == 'voltar':  # simular o toque de volta para tela anterior
            break

        ratings = searchPlaceRatings(place_id)

        print(f"\n{TAB}# Avaliação(ões): ")
        for j, rating in enumerate(ratings):
            print(f"{TAB}{j + 1}- ", end="")  # imprime a lista q aparece na tela como resultado da busca
            print(f"{ratings[j].user}", end="")  # imprime a lista q aparece na tela como resultado da busca
            print(f"{ratings[j].id}, {ratings[j].rating}",
                  end="")  # imprime a lista q aparece na tela como resultado da busca
            print()
