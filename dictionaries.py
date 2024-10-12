person = {
    "name": "John",
    "alter": 30,
    "beruf": "Informatiker"
}

#Zugriff auf Werte über die Schlüssel
print(f"Name: {person['name']}")
print(f"Alter: {person['alter']}")
print(f"Beruf: {person['beruf']}")

# Hinzufügen eines neuen Schlüssel

person["hobby"] = "Programmieren"
print(f"Hobby: {person['hobby']}")


# Ändern eines vorhandenen Werts

person["alter"] = 31
print(f"Neues Alter: {person['alter']}")


# Löschen eines Schlüssels
del person["beruf"]
print("Nach dem Löschen des Berufs:", person)