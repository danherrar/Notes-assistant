import psycopg2

def conn():
    connection = psycopg2.connect(user = "",
                                password = "",
                                host = "",
                                port = "",
                                database = "")

    cursor = connection.cursor()

    return [connection, cursor]