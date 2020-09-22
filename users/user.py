import users.connection as conect
import datetime
import hashlib


connection = conect.conn()
database = connection[0]
cursor = connection[1]

class User:

    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password

    def register(self):

        date = datetime.datetime.now()

        cipher = hashlib.sha256()
        cipher.update(self.password.encode("utf-8"))

        sql = "INSERT INTO users(name, email, password, date) VALUES(%s, %s, %s, %s)"
        insert = (self.name, self.email, cipher.hexdigest(), date)

        try:

            cursor.execute(sql, insert)
            database.commit()
            result = [cursor.rowcount, self]

        except:
            result = [0, self]

        finally:
            cursor.close()
            database.close()


        return result

    def indentify(self):


        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        cipher = hashlib.sha256()
        cipher.update(self.password.encode("utf-8"))

        user = (self.email, cipher.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        cursor.close()
        database.close()

        return result