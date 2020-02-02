from models.user import User
from models.message import Message
from psycopg2 import connect

con = connect(host='localhost', user='postgres', password='coderslab', dbname='workshop2')
cur = con.cursor()

"""
a = User()
a = a.load_user_by_id(cur, 4)
print(a.username, a.email, a.hashed_password)
a.delete(cur)


b = Message()

b.from_id = 6
b.to_id = 7
b.text = "Druga wiadomość"
#print(b.from_id, b.to_id, b.text, b.timestamp)
b.save_to_db(cur)

for i in b.load_all_messages(cur):
    print(i.from_id, i.to_id, i.text, i.timestamp)
print()
for i in b.load_all_messages_for_user(cur,6):
    print(i.from_id, i.to_id, i.text, i.timestamp)
"""
con.commit()
cur.close()
con.close()