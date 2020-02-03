import argparse
from psycopg2 import connect
from models.user import User


parser = argparse.ArgumentParser(description='Skrypt do zarządzania użytkownikami')
parser.add_argument('-u', '--username', help="login (email) użytkownika", type=str, required=False)
parser.add_argument('-p', '--password', help="Hasło użytkownika", type=str, required=False)
parser.add_argument('-l', '--list', help="Żądanie wylistowania wszystkich użytkowników", required=False)
parser.add_argument('-d', '--delete', help="Login użytkownika do usunięcia", type=str, required=False)
parser.add_argument('-e', '--edit', help="Login użytkownika do modykacji", type=str, required=False)
parser.add_argument('-n', '--newpass', help="Nowe hasło użytkownika", type=str, required=False)
args = parser.parse_args()

con = connect(host='localhost', user='postgres', password='coderslab', dbname='workshop2')
cur = con.cursor()

if args.username != None and args.password != None:
    if args.edit == None and args.delete == None:
        existing_emails = [i.email for i in User().load_all_users(cur)]
        if args.username in existing_emails:
            print("Użytkownik już istnieje!")
        else:
            user = User()
            user.email = args.username
            user.set_password(args.password, '12345')
            user.save_to_db(cur)
    else:
        if args.edit != None:
            if args.newpass != None
                pass  #nadajemy nowe hasło

else:
    pass

con.commit()
cur.close()
con.close()