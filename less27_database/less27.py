import mysql.connector as mysql

less27_db = mysql.connect(host='localhost',
                          user='superuser',
                          passwd='SQLroot1717090987h',
                          database='less27_db')  # Подключение к базе данных

try:
    cursor = less27_db.cursor()  # Создаём курсор-связку для работы с БД
    cursor.execute("CREATE DATABASE less27_db") # Создаём БД less27_db
    cursor.execute("SHOW DATABASES") # Показывает список существующих БД
    print(cursor.fetchall()) # Выводит инфо о созданных БД в консоль
    cursor.execute('''CREATE TABLE orders(
        ord_no INT(11),
        purch_amt INT(11),
        ord_date DATE,
        customer_id INT(11),
        salesman_id INT(11))''')
    cursor.execute('SHOW TABLES') # Показывает список существующих таблиц в БД
    print(cursor.fetchall())
    cursor.execute('ALTER TABLE orders MODIFY COLUMN purch_amt FLOAT(8,2)') # Изменяем тип данных в столбце purch_amt с INT на FLOAT
    query = '''INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id)
                VALUES (%s, %s, %s, %s, %s)'''
    values = [
        (1, 150.5, '2012-10-05', 5, 2),
        (2, 65.26, '2012-10-05', 2, 1),
        (3, 2480.4, '2012-10-10', 9, 3),
        (4, 110.5, '2012-08-17', 9, 3),
        (5, 2400.6, '2012-07-27', 7, 1),
        (7, 948.5, '2012-09-10', 5, 2),
        (8, 5760, '2012-09-10', 2, 1),
        (9, 270.65, '2012-09-10', 1, 5),
        (10, 1983.43, '2012-10-10', 4, 6),
        (11, 75.29, '2012-08-17', 3, 7),
        (12, 250.45, '2012-06-27', 8, 2),
        (13, 3045.6, '2012-04-25', 2, 1)
    ]
    cursor.executemany(query, values)  # Вставляем список значений (executemany) в БД
    less27_db.commit()  # Применяем изменения к БД (после любых изменений в БД)
    cursor.execute('DESC orders')
    print(cursor.fetchall())

    query = 'SELECT ord_no, purch_amt, ord_date FROM orders WHERE salesman_id = 02'
    cursor.execute(query)
    print(cursor.fetchall())

    query = 'SELECT DISTINCT salesman_id FROM orders'
    cursor.execute(query)
    print(cursor.fetchall())

    query = 'SELECT ord_date, customer_id, ord_no, purch_amt FROM orders'
    cursor.execute(query)
    print(cursor.fetchall())

    query = 'SELECT * FROM orders WHERE ord_no BETWEEN 1 AND 7 AND ord_no <> 6'
    cursor.execute(query)
    print(cursor.fetchall())

finally:
    less27_db.close()
