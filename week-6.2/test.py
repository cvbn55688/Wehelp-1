from mysql.connector import Error
from mysql.connector import pooling

try:
    connection_pool = pooling.MySQLConnectionPool(host = 'localhost',
                                                port= "3306",
                                                user = 'root',
                                                password = 'zxc55332',
                                                database = 'website_HW',
                                                pool_name="my_pool",
                                                pool_size = 3
                                                )

    # print("Printing connection pool properties ")
    # print("Connection Pool Name - ", connection_pool.pool_name)
    # print("Connection Pool Size - ", connection_pool.pool_size)

    # Get connection object from a pool
    connection_object = connection_pool.get_connection()
    print(connection_object)

    if connection_object.is_connected():
        db_Info = connection_object.get_server_info()
        print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)

        cursor = connection_object.cursor()
        cursor.execute("select * from member;")
        record = cursor.fetchall()
        print(record)

except Error as e:
    print("Error while connecting to MySQL using Connection pool ", e)
finally:
    # closing database connection.
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
        print("MySQL connection is closed")