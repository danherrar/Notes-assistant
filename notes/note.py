import users.connection as connection

connect = connection.conn()

database = connect[0]
cursor = connect[1]


class Note():

    def __init__(self, user_id, title="", body=""):
        self.user_id = user_id
        self.title = title
        self.body = body


    def save(self):
        sql = "INSERT INTO notes (user_id, title, body, date) VALUES (%s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.body)

        cursor.execute(sql, note)
        database.commit()

        result = cursor.rowcount

        return[result, self]
    
    def ls(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"

        cursor.execute(sql)
        result = cursor.fetchall()
        

        return result
    
    def d(self):
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND title LIKE '{self.title}%'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]