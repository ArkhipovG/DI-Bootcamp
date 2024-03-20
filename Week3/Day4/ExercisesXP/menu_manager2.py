import psycopg2

dbname = "restaurant"
user = "postgres"
password = "4744"
host = "localhost"
port = "5432"

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Menu_Items WHERE item_name = '{item_name}'")
            item = cursor.fetchone()
            connection.close()
            if item:
                return item
            else:
                return None

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching item by name:", error)
            return None

    @classmethod
    def all_items(cls):
        try:
            connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Menu_Items")
            items = cursor.fetchall()
            connection.close()
            return items
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching all items:", error)
            return []

# print(MenuManager.all_items())
# print(MenuManager.get_by_name("Burger"))