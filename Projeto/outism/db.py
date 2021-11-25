from models import User, Place, Address
from datetime import datetime

import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', port='3306', database='outism')
cursor = conn.cursor(buffered=True, dictionary=True)

def validateUser(email, password):
    query = "SELECT * FROM `users` WHERE `email` = '%s' AND `password` = '%s'" % (email, password)
    cursor.execute(query)
    user = cursor.fetchone()

    return user

def createUser(email, password, cnpj, first_name, last_name, profile, lat, lng, address_id):
    query_create = "insert into users (email, password, cnpj, first_name, last_name, profile, lat, lng, address_id, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query_create, (email, password, cnpj, first_name, last_name, profile, lat, lng, address_id, datetime.now()))
    conn.commit()

    query_fetch = "SELECT * FROM `users` WHERE `email` = '%s' AND `password` = '%s'" % (email, password)
    cursor.execute(query_fetch)
    novo_usuario = cursor.fetchone()

    return novo_usuario


def createAddress(address):
    query_create = "insert into `addresses` (`name`, `neighborhood`, `description`, `street`, `street2`, `zipcode`, `lat`, `lng`, `radius`, `city_id`, `created_at`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    new_address = cursor.execute(query_create, (address.name, address.neighborhood, address.description, address.street, address.street2, address.zipcode, address.lat, address.lng, address.radius, address.city_id, datetime.now(),))
    conn.commit()

    return new_address


def createPlace(place):
    query_create = "insert into `places` (`manager_id`, `address_id`, `cnpj`, `name`, `logo`, `created_at`) values (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query_create, (place.manager_id, place.address_id, place.cnpj, place.name, place.logo, datetime.now()))
    conn.commit()

    query_fetch = "SELECT * FROM `places` WHERE `manager_id` = %s AND `cnpj` = %s AND `name` = %s" % (place.manager_id, place.cnpj, place.name)
    cursor.execute(query_fetch)
    new_place = cursor.fetchone()

    return new_place


def createCategory(category):
    new_category = cursor.execute("insert into categories (name, description, created_at) values (%s, %s, %s)",
                                (category.name, category.description, datetime.now()))
    conn.commit()

    return new_category


def favoritePlace(user_id, place_id):
    new_place = cursor.execute("insert into users_favorite_places (user_id, place_id, created_at) values (%s, %s, %s)",
                             (user_id, place_id, datetime.now(),))
    conn.commit()

    return new_place


def categorizePlace(category_id, place_id):
    new_place = cursor.execute("insert into places_categories (category_id, place_id, created_at) values (%s, %s, %s)",
                             (category_id, place_id, datetime.now(),))
    conn.commit()

    return new_place


def ratePlace(user_id, place_id, rating, description):
    new_place = cursor.execute(
        "insert into places_ratings (user_id, place_id, rating, description, created_at) values (%s, %s, %s, %s, %s)",
        (category_id, place_id, rating, description, datetime.now()))
    conn.commit()

    return new_place


def returnFavoritesPlaces(user_id):
    cursor.execute(
        "select places.* from places inner join users_favorite_places on places.id = users_favorite_places.place_id where user_id = %s",
        (user_id,))

    favorites_places = cursor.fetchall()
    return favorites_places


def searchUser(id):
    cursor.execute("select id, email, first_name, last_name, profile, lat, lng, profile from users where id = %s",(id))
    usuario = cursor.fetchone()

    return usuario


def getPlaces():
    cursor.execute("select places.*, addresses.neighborhood, addresses.street, round(avg(places_ratings.rating),2) as media FROM places inner JOIN addresses LEFT JOIN places_ratings ON places.id = places_ratings.place_id")
    places = cursor.fetchall()

    return places


def searchAddresses(id):
    cursor.execute("select * from addresses where id = %s", (id))
    address = cursor.fetchone()

    return address


def searchPlacesById(id):
    cursor.execute(
        "select places.*, addresses.neighborhood, addresses.street from places inner join addresses on places.address_id = addresses.id LEFT JOIN places_ratings on places.id = places_ratings.place_id where places.id = %s",
        (id))
    place = cursor.fetchone()

    return place


def searchPlacesByCNPJ(cnpj):
    cursor.execute(
        "select places.*, addresses.neighborhood, addresses.street from places inner join addresses on places.address_id = addresses.id LEFT JOIN places_ratings on places.id = places_ratings.place_id where places.cnpj = %s",
        (cpnj,))
    places = cursor.fetchall()

    return places


def searchPlaces(key):
    cursor.execute(
        "select places.*, addresses.neighborhood, addresses.street, round(avg(places_ratings.rating),2) as media from places inner join addresses on places.address_id = addresses.id LEFT JOIN places_ratings on places.id = places_ratings.place_id where (addresses.neighborhood LIKE '%%s%') OR (places.name LIKE '%%s%') OR (addresses.street LIKE '%%s%')",
        (key, key, key,))
    places = cursor.fetchall()

    return places

def searchCategoryByName(name):
    cursor.execute("select id, name, description from categories where UPPER(name) = UPPER(%s)", (string(name),))
    category = cursor.fetchone()

    return category

def searchCategoryById(id):
    cursor.execute("select id, name, description from categories where id = %s", (id,))
    category = cursor.fetchone()

    return category

def searchPlaceRatings(id):
    cursor.execute(
        "select places_ratings.rating, places_ratings.description, concat(users.first_name, ' ', users.last_name) as user from places_ratings inner join users on places_ratings.user_id = users.id where place_id = %s",
        (id))
    ratings = cursor.fetchall()

    return ratings


def updateAddress(address, id):
    updated_address = cursor.execute(
        "update addresses set city_id = %s, name = %s, neighborhood = %s, picture = %s, street = %s, street2 = %s, zipcode = %s, lat = %s, lng = %s, radius = %s, modified_at = %s where id = %s",
        (address, datetime.now(), id,))
    conn.commit()

    return updated_address


def updatePlace(place, id):
    updated_place = cursor.execute(
        "update places set manager_id = %s, address_id = %s, cnpj = %s, name = %s, logo = %s, modified_at = %s where id = %s",
        (place, datetime.now(), id,))
    conn.commit()

    return updated_place


def updateUser(user, id):
    updated_user = cursor.execute(
        "update users set password = %s, first_name = %s, last_name = %s, lat = %s, lng = %s, email = %s, photo = %s, modified_at = %s where id = %s",
        (user, datetime.now(), id,))
    conn.commit()

    return updated_user


def deletePlace(id):
    cursor.execute("delete from places where id = %s", (id,))
    conn.commit()


def deleteAddress(id):
    cursor.execute("delete from addresses where id = %s", (id,))
    conn.commit()


def deleteUser(id):
    cursor.execute("delete from users where id = %s", (id,))
    conn.commit()