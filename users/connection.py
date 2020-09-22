import psycopg2

def conn():
    connection = psycopg2.connect(user = "postgres",
                                password = "kuait",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "notes")

    cursor = connection.cursor()

    return [connection, cursor]