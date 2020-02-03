from models.user import User
from models.message import Message
from psycopg2 import connect

con = connect(host='localhost', user='postgres', password='coderslab', dbname='workshop2')
cur = con.cursor()

print(User().load_user_by_email(cur, 'mail1@gmail.com').id)

a = User()
a = a.load_user_by_id(cur, 5)
print(a.username, a.email, a.hashed_password)
print()
#a.delete(cur)

b = Message()
b.from_id = 6
b.to_id = 7
b.text = "Druga wiadomość"

for i in b.load_all_messages(cur):
    print(i.from_id, i.to_id, i.text, i.timestamp)
print()
for i in b.load_all_messages_for_user(cur,6):
    print(i.from_id, i.to_id, i.text, i.timestamp)

con.commit()
cur.close()
con.close()