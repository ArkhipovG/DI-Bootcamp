import requests
import random
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '4744'
DATABASE = 'countries'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)


def fetch_random_countries(num_countries=10):
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        countries_data = response.json()
        random_countries = random.sample(countries_data, num_countries)
        return random_countries
    else:
        print("Failed to fetch countries data")
        return None


def insert_countries(conn, countries):
    query = "INSERT INTO countries(name, capital, flag, subregion, population) VALUES(%s,%s, %s, %s, %s)"

    try:
        c = conn.cursor()
        c.executemany(query, countries)
        conn.commit()
        print("Countries inserted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error: ", error)
        return None


def main():
    if connection is not None:
        random_countries = fetch_random_countries()
        if random_countries:
            countries_to_insert = [(country['name']['common'], country['capital'][0], country['flag'],
                                    country['subregion'], country['population'])
                                   for country in random_countries]
            insert_countries(connection, countries_to_insert)
        connection.close()
    else:
        print("Error! Cannot create the database connection.")


main()
