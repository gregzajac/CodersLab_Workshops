from random import randint

"""Zadanie 1
Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:

Zadać pytanie: "Zgadnij liczbę" i pobrać liczbę z klawiatury.
Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "To nie jest liczba", po czym wrócić do pkt. 1
Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Za mało!", po czym wrócić do pkt. 1.
Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "Za dużo!", po czym wrócić do pkt. 1.
Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "Zgadłeś!", po czym zakończyć działanie programu.
Przykład:
Zgadnij liczbę: cześć
To nie jest liczba.
Zgadnij liczbę: 50
Za mało!
Zgadnij liczbę: 75
Za dużo!
Zgadnij liczbę: 63
Zgadłeś!
"""
def guess_number():
    computer_number = randint(1, 100)
    while True:
        try:
            guessed_number = int(input("Wprowadź liczbę: "))
            if guessed_number == computer_number:
                return "Zgadłeś!"
            elif guessed_number > computer_number:
                print("Za dużo!")
            else:
                print("Za mało!")
        except ValueError:
            print("Nie wprowadziłeś liczby!")

print(guess_number())