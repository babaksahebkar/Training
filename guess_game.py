import random

number = random.randint(1, 100)
attempts = 0

print("Ich denke an eine Zahl zwischen 1 und 100. Rate sie.")

while True:
    guess = input("Dein Tipp: ")

    if not guess.isdigit():
        print("Bitte eine Zahl eingeben.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("Zu niedrig.")
    elif guess > number:
        print("Zu hoch.")
    else:
        print(f"Richtig! Du hast {attempts} Versuche gebraucht.")
        break
