from models.user import User
from psycopg2 import connect

con = connect(host='localhost', user='postgres', password='coderslab', dbname='workshop2')
cur = con.cursor()

a = User()

con.commit()
cur.close()
con.close()
