import argparse
#from models.user import User

parser = argparse.ArgumentParser(description='Tutaj możemy podać zwięzły opis naszego skryptu')
# parser.add_argument('-u', '--username', help="Argument o konkretnym typie i wartością domyślną", type=int, default=5, required=False)
parser.add_argument('-u', '--username', help="Email użytkownika", type=str)
parser.add_argument('-p', '--password', help="Hasło użytkownika", type=str, required=False)
parser.add_argument('-l', '--list', help="Żądanie wylistowania wszystkich użytkowników", required=False)
parser.add_argument('-d', '--delete', help="Login użytkownika do usunięcia", type=str, required=False)
parser.add_argument('-e', '--edit', help="Login użytkownika do modykacji.", type=str, required=False)
args = parser.parse_args()

if args.username != None:
    if args.password != None:
        pass
    else:
        pass


else:
    print("Brakuje loginu użytkownika")



