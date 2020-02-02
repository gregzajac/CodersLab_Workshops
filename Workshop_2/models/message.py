from datetime import datetime


class Message():

    def __init__(self):
        self.__id = None
        self.from_id = None
        self.to_id = None
        self.text = ""
        self.__timestamp = None

    @property
    def id(self):
        return self.__id

    @property
    def timestamp(self):
        return self.__timestamp

    @staticmethod
    def load_message_by_id(cursor, message_id):
        sql = f"select id, from_id, to_id, text, creation_date from messages where id = %s;"
        cursor.execute(sql, (message_id,))
        row = cursor.fetchone()
        if row:
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.from_id = row[1]
            loaded_message.to_id = row[2]
            loaded_message.text = row[3]
            loaded_message.__timestamp = row[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_messages_for_user(cursor, to_id):
        sql = f"select id, from_id, to_id, text, creation_date from messages where to_id = %s;"
        ret = []
        cursor.execute(sql, (to_id,))
        rows = cursor.fetchall()
        for row in rows:
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.from_id = row[1]
            loaded_message.to_id = row[2]
            loaded_message.text = row[3]
            loaded_message.__timestamp = row[4]
            ret.append(loaded_message)
        if len(ret) > 0:
            return ret
        else:
            return None

    @staticmethod
    def load_all_messages(cursor):
        sql = f"select id, from_id, to_id, text, creation_date from messages"
        ret = []
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.from_id = row[1]
            loaded_message.to_id = row[2]
            loaded_message.text = row[3]
            loaded_message.__timestamp = row[4]
            ret.append(loaded_message)
        if len(ret) > 0:
            return ret
        else:
            return None

    def save_to_db(self, cursor):
        if self.__id == None:
            sql = """insert into messages (from_id, to_id, text, creation_date) 
                    values (%s,%s,%s,%s) returning id"""
            values = (self.from_id, self.to_id, self.text, datetime.now())
            cursor.execute(sql, values)
            self.__id = cursor.fetchone()[0]
            return True
        else:
            sql = """UPDATE Users SET from_id=%s, to_id=%s, text=%s, creation_date=%s
                        WHERE id=%s"""
            values = (self.from_id, self.to_id, self.text, datetime.now())
            cursor.execute(sql, values)
            return True
