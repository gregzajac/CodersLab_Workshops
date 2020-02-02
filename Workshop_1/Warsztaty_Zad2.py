import random

def lotto():
    guessed_numbers = []  #List of user's  guessed numbers
    i = 0
    while i < 6:
        try:
            guessed_number = int(input("Podaj liczbę od 1 do 49: "))
            if (guessed_number in range(1,50)
                and guessed_number not in guessed_numbers):
                guessed_numbers.append(guessed_number)
                i += 1
            else:
                print("Wprowadź nową liczbę od 1 do 49")
        except ValueError:
            print("To nie jest liczba!")

    computer_numbers = [i for i in range(1,50)]
    random.shuffle(computer_numbers)
    computer_numbers = computer_numbers[:6]

    shoots = list(set(computer_numbers) & set(guessed_numbers))
    if len(shoots) > 0:
        text = f"Komputer wylosował: {computer_numbers}\n " \
               f"Liczba trafień: {len(shoots)}; {shoots}"
    else:
        text = f"Komputer wylosował: {computer_numbers}\n" \
                "Nic nie trafiłeś!"
    return text

print(lotto())