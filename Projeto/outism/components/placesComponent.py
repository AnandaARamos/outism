from db import searchPlaces, ratePlace
from models import Place, User
from constants import NGO, TAB

def loadMap(places): #chamar o GoogleMaps
    pins = []

    for place in places: #p é a tupla q está na lista places, q vem do db
        pin = {"name": place.name, "lat": place.address.lat, "lng": place.address.lng}
        #varrer os p's de places e pegar nome do local, latitude e longitude e atulaizar o dicionário pin
        pins.append(pin)

    print(pins) # na interface gráfica, o mapa seria impresso com os pins para ser visualizado

def loadPlacesComponent(user):
    while True:
        entrada = input(f"\n{TAB}Digite as info do lugar (nome, bairro ou rua): ").strip()

        if entrada == 'voltar': #simular o toque de volta para tela anterior
            break

        places = searchPlaces(entrada)

        for i, place in enumerate(places):
            print(f"{TAB}{i+1}- ", end="") #imprime a lista q aparece na tela como resultado da busca
            print(f"{places[i]['id']}, {places[i]['name']}", end="") #imprime a lista q aparece na tela como resultado da busca
            if place.type == NGO:
                print(" (ONG)", end="")
            print()

        while True:
            clique = int(input("""
                O que você quer fazer?\n
                1- favoritar
                2- avaliar
                3- ver mapa
                4- sair

                opção: """).strip())

            if clique == 1:
                index = int(input("Digite o id do local que deseja favoritar: ").strip())

                possiveis_locais = searchPlaces(index)
                for i, possivel_local in enumerate(possiveis_locais):
                    print(f"{TAB}{i+1}- ", end="") #imprime a lista q aparece na tela como resultado da busca
                    print(f"{possiveis_locais[i]['name']}", end="") #imprime a lista q aparece na tela como resultado da busca
                    if place.type == NGO:
                        print(" (ONG)", end="")
                    print()

                place_id = int(input("Digite o identificador(id) do local que deseja favoritar: ").strip()) # se tivesse tela, pra ser userfriendly, isso seria o toque no local e o user ñ precisa saber código
                #baseado no q ele digitou eu vou procurar na lista de places qual o ID do nome q ele digitou

                favoritePlace(user.id, place_id)

                print(f"\n{TAB}# Local favoritado")
            elif clique == 2:
                place_id = int(input("Digite o identificador (id) do local: ").strip())
                rating = int(input("Digite a nota: "))
                rating_description = input("Digite o motivo da nota dada: ").strip()

                ratePlace(user['id'], place_id, rating, rating_description)

                print(f"\n{TAB}# Avaliação realizada")
            elif clique == 3:
                print(f"\n{TAB}# MAPA")
                loadMap(places)
            else:
                break
