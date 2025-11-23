#!/usr/bin/env python3

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Division durch 0 ist nicht erlaubt.")
        return a / b
    else:
        raise ValueError("Ungültiger Operator. Erlaubt sind: + - * /")


def main():
    print("=== Terminal Taschenrechner ===")
    print("Beispiel: 12 * 4")
    print("Zum Beenden: 'exit' eingeben\n")

    while True:
        expression = input("Rechnung eingeben: ").strip()

        if expression.lower() == "exit":
            print("Rechner beendet.")
            break

        try:
            parts = expression.split()

            if len(parts) != 3:
                raise ValueError("Format muss sein: Zahl Operator Zahl")

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            result = calculate(a, operator, b)
            print(f"= {result}\n")

        except Exception as e:
            print(f"Fehler: {e}\n")


if __name__ == "__main__":
    main()
