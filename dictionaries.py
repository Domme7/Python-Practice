person = {
    "name": "John",
    "age": 30,
    "beruf": "Informatiker"
}

#Zugriff auf Werte über die Schlüssel
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Beruf: {person['beruf']}")

# Hinzufügen eines neuen Schlüssel

person["hobby"] = "Programmieren"
print(f"Hobby: {person['hobby']}")