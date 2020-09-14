print("Hallo! Mit diesem Konverter kannst du Kilometer in Meilen umwandeln.")

while True:
    print("Bitte gib eine Zahl in Kilometer an, welche du umgewandelt haben willst. Bitte nur Zahlen eingeben!")

    km = input("Kilometer: ")

    km = float(km.replace(",", "."))

    miles = km * 0.621371

    print(f"{km} Kilometer entsprechen {miles} Meilen")

    choice = input("Willst du noch etwas umgerechnet haben? (y/n): ")

    if choice.lower() != "y":
        break

print("Vielen Dank für die Verwendung dieses Konverters!")
