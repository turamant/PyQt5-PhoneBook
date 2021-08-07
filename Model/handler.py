import MySQLdb


class DataBase:
    host = "localhost"
    user = "user1"
    passwd = "password1"
    db = "phonebook"     #new  резервная

    def __init__(self):
        self.conn = MySQLdb.connect(self.host,
                                    self.user,
                                    self.passwd,
                                    self.db,
                                    use_unicode=True,
                                    charset="utf8")
        self.cur = self.conn.cursor()

    def insert(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            print("Изменения подтверждаю!")
        except Exception as ex:
            print("ОШИБКА insert !!!", ex)
            self.conn.rollback()

    def update(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            print("Изменения подтверждаю!")
        except Exception as ex:
            print("ОШИБКА update !!!", ex)
            self.conn.rollback()

    def delete(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            print("Изменения подтверждаю!")
        except Exception as ex:
            print("ОШИБКА delete !!!", ex)
            self.conn.rollback()

    def read(self, query):
        try:
            self.cur.execute(query)
        except Exception as ex:
            print("Ошибка чтения данных", ex)

    def search(self, query):
        try:
            self.cur.execute(query)
        except Exception as ex:
            print("Ошибка поиска", ex)

    def __del__(self):
        self.conn.close()