class Address:
    def __init__(self, name, neighborhood, street, street2, zipcode, lat, lng, radius):
        self.name = name
        self.neighborhood = neighborhood
        self.street = street
        self.street2 = street2
        self.zipcode = zipcode
        self.lat = lat
        self.lng = lng
        self.radius = radius


class User:
    def __init__(self, email, password, cnpj, first_name, last_name, profile, lat, lng):
        self.first_name = first_name,
        self.last_name = last_name,
        self.email = email
        self.password = password
        self.profile = profile
        self.cnpj = cnpj
        self.lat = lat
        self.lng = lng


class Place:
    def __init__(self, cnpj, name, description, category, address: Address, type, rating=0):
        self.cnpj = cnpj
        self.name = name
        self.description = description
        self.category = category
        self.address = address
        self.type = type

        self.numRatings = 0
        self.benefits = []
        self.projects = []


class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Rating:
    def __init__(self, rating, description):
        self.name = rating
        self.description = description
