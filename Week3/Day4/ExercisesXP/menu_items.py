import psycopg2

dbname = "restaurant"
user = "postgres"
password = "4744"
host = "localhost"
port = "5432"

connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
            )
cursor = connection.cursor()
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item: {self.name}, Price: ${self.price}"

    def save(self):
        try:
            cursor.execute(f"INSERT INTO Menu_Items (item_name, item_price) VALUES('{self.name}', '{self.price}');")
            connection.commit()
            connection.close()
            print("Item saved successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while saving item:", error)

    def delete(self):
        try:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM Menu_Items WHERE item_name = '{self.name}'")
            connection.commit()
            connection.close()
            print("Item deleted successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while deleting item:", error)

    def update(self, new_name=None, new_price=None):
        try:
            if new_name and new_price:
                cursor.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                               (new_name, new_price, self.name))
            elif new_name:
                cursor.execute("UPDATE Menu_Items SET item_name = %s WHERE item_name = %s",
                               (new_name, self.name))
            elif new_price:
                cursor.execute("UPDATE Menu_Items SET item_price = %s WHERE item_name = %s",
                               (new_price, self.name))
            connection.commit()
            connection.close()
            print("Item updated successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while updating item:", error)



# item = MenuItem('Veggie Burger', 37)
# item.save()
#item.delete()
# item.update(new_price=35)