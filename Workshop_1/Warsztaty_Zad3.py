from random import randint

def lotto():
    user_number = int(input("Pomyśl liczbę od 1 do 1000, a ja ją zgadnę w max 10 próbach: "))

    min_number = 0
    max_number = 1000
    while True:
        guessed_number = int((max_number - min_number) / 2) + min_number
        print(f"Zgaduję {guessed_number}")

        user_info = input("Napisz 'Za dużo/Za mało/Zgadłeś': ")

        if user_info not in ["Za dużo", "Za mało", "Zgadłeś"]:
            print("Wprowadź 'Za dużo' lub 'Za mało' lub 'Zgadłeś'!")
        else:
            if user_info == "Zgadłeś":
                if guessed_number == user_number:
                    return "Wygrałem!"
                else:
                    print("Nie oszukuj!")
            elif user_info == "Za dużo":
                if guessed_number > user_number:
                    max_number = guessed_number
                else:
                    print("Nie oszukuj!")
            elif user_info == "Za mało":
                if guessed_number < user_number:
                    min_number = guessed_number
                else:
                    print("Nie oszukuj!")

print(lotto())