import sqlite3
from prettytable import PrettyTable


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('test_database.db')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Проверяем, есть ли у нас заполненная база (по наличию таблиц)
        self.cursor.execute('SELECT name FROM sqlite_master WHERE name="clients"')
        if not self.cursor.fetchall():
            # Создаем таблицы
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
                        client_id INT PRIMARY KEY,
                        client_name TEXT);
                        """)
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                        product_id INT PRIMARY KEY,
                        product_name TEXT,
                        price REAL);
                        """)
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                        order_id INT PRIMARY KEY,
                        client_id INT NOT NULL,
                        product_id INT NOT NULL,
                        order_name TEXT,
                        FOREIGN KEY (client_id) REFERENCES clients (client_id)
                            ON DELETE CASCADE ON UPDATE NO ACTION,
                        FOREIGN KEY (product_id) REFERENCES products (product_id)
                            ON DELETE CASCADE ON UPDATE NO ACTION);
                        """)
            self.connection.commit()
            clients = [(1, "Иван"), (2, "Константин"), (3, "Дмитрий"), (4, "Александр")]
            products = [
                (1, 'Мяч', 299.99), (2, 'Ручка', 18), (3, 'Кружка', 159.87),
                (4, 'Монитор', 18000), (5, 'Телефон', 9999.9), (6, 'Кофе', 159)]
            orders = [
                (1, 2, 2, 'Закупка 1'), (2, 2, 5, 'Закупка 2'), (3, 2, 1, 'Закупка 3'),
                (4, 1, 1, 'Закупка 4'), (5, 1, 3, 'Закупка 5'), (6, 1, 6, 'Закупка 6'),
                (7, 1, 2, 'Закупка 7'), (8, 4, 5, 'Закупка 8'), (9, 3, 6, 'Закупка 9'),
                (10, 3, 3, 'Закупка 10'), (11, 1, 5, 'Закупка 11')]
            self.cursor.executemany("INSERT INTO clients VALUES(?, ?);", clients)
            self.cursor.executemany("INSERT INTO products VALUES(?, ?, ?);", products)
            self.cursor.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", orders)
            self.connection.commit()

    def clients_orders(self):
        sql = """SELECT client_name, sum(price) as total_sum
                 FROM orders
                 INNER JOIN clients ON clients.client_id = orders.client_id
                 INNER JOIN products ON products.product_id = orders.product_id
                 GROUP BY client_name
                 ORDER BY total_sum DESC"""
        self.cursor.execute(sql)
        print('Cписок клиентов с общей суммой их покупки')
        th = ["Имя", "Общая сумма покупки"]
        table = PrettyTable(th)
        for row in self.cursor.fetchall():
            table.add_row([row[0], row[1]])
        print(table)

    def client_buy_phone(self):
        sql = """SELECT DISTINCT client_name 
                 FROM orders 
                 INNER JOIN clients ON clients.client_id = orders.client_id
                 INNER JOIN products ON products.product_id = orders.product_id
                 WHERE product_name = 'Телефон'"""
        self.cursor.execute(sql)
        print('Список клиентов, которые купили телефон')
        th = ["№", "Имя"]
        table = PrettyTable(th)
        i = 1
        for row in self.cursor.fetchall():
            table.add_row([i, row[0]])
            i += 1
        print(table)

    def products_count(self):
        sql = """SELECT product_name, count(orders.order_id) as count 
                 FROM products 
                 LEFT JOIN orders ON products.product_id = orders.product_id
                 GROUP BY product_name
                 ORDER BY COUNT DESC"""
        self.cursor.execute(sql)
        print('Список товаров с количеством их заказа')
        th = ["Товар", "Кол-во покупок"]
        table = PrettyTable(th)
        for row in self.cursor.fetchall():
            table.add_row([row[0], row[1]])
        print(table)


if __name__ == '__main__':
    try:
        db = DataBase()
        db.create_tables()
        db.clients_orders()
        db.client_buy_phone()
        db.products_count()
    except sqlite3.Error as e:
        print(f'Ошибка при работе с SQLite: {e}')
    finally:
        if db.connection:
            db.connection.close()
            print("Соединение с SQLite закрыто")

