print("*******Willkommen zum FizzBuzz-Spiel.*******\n")
print("Zahlen welche sich durch 3 dividieren lassen werden mit einem fizz gekennzeichnet.")
print("Zahlen welche sich durch 5 dividieren lassen werden mit einem buzz gekennzeichnet.")
print("Zahlen die sowohl durch 3 als auch 5 teilbar sind, werden mit einem fizzbuzz gekennzeichnet.\n\n")

while True:

    zahl = input("Wähle eine Zahl zwischen 1 und 100:\n")
    zahl = int(zahl)

    for num in range(1, zahl + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

    choice = input("\nNochmal spielen? (y)Ja (n)Nein\n")
    if choice.lower() != "y":
        break

print("\nDanke fürs Spielen!\nBis zum nächsten mal :-)")
