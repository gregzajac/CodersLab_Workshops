from models import generate_salt, password_hash, check_password
#from psycopg2 import connect

class User:
    def __init__(self):
        self.__id = None
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt):
        self.__hashed_password = password_hash(password, salt)

    def save_to_db(self, cursor):
        if self.__id == None:
            sql = """INSERT INTO Users(username, email, hashed_password)
                                VALUES(%s, %s, %s) RETURNING id"""
            values = (self.username, self.email, self.hashed_password)
            cursor.execute(sql, values)
            self.__id = cursor.fetchone()[0]
            return True
        else:
            sql = """UPDATE Users SET username=%s, email=%s, hashed_password=%s
                        WHERE id=%s"""
            values = (self.username, self.email, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True

    def delete(self, cursor):
        sql = "DELETE FROM Users WHERE id=%s"
        cursor.execute(sql, (self.__id,))
        self.__id = -1
        return True

    @staticmethod
    def load_user_by_id(cursor, user_id):
        sql = "SELECT id, username, email, hashed_password FROM users WHERE id=%s"
        cursor.execute(sql, (user_id,))
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT id, username, email, hashed_password FROM Users"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            ret.append(loaded_user)
        if len(ret) > 0:
            return ret
        else:
            return None

"""    @staticmethod
    def load_user_by_email(cursor, email):
        sql = "SELECT id, username, email, hashed_password FROM users WHERE email=%s"
        cursor.execute(sql, (email,))
        data = cursor.fetchone()
        if data:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None"""