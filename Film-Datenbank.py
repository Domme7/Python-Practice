filme = {
    "Inception": {
        "Regisseur": "Christopher Nolan",
        "Erscheinungsjahr": 2010,
        "Bewertung": 8.8
    },
    "The Matrix": {
        "Regisseur": "The Wachowskis",
        "Erscheinungsjahr": 1999,
        "Bewertung": 8.7
    },
    "Interstellar": {
        "Regisseur": "Christopher Nolan",
        "Erscheinungsjahr": 2014,
        "Bewertung": 8.6
    }

}

def print_reg(name):
    print(f"Regisseur von {name}: {filme[name]['Regisseur']}")



def print_year(name):
    print(f"Year von {name}: {filme[name]['Erscheinungsjahr']}")


def print_score(name):
    print(f"{name} hat den Score: {filme[name]['Bewertung']}")



print_reg("Inception")
print_year("Inception")
print_score("Inception")

filme["The Dark Knight"] = {
    "Regisseur": "Christopher Nolan",
    "Erscheinungsjahr": 2008,
    "Bewertung": 9.0
}

print_reg("The Dark Knight")
print_year("The Dark Knight")
print_score("The Dark Knight")

print("""



        
        """)      
      
      
    

for film in filme:
    print(f"Name: {film}")
    print(f"Regisseur: {filme[film]['Regisseur']}")
    print(f"Erscheinungsjahr: {filme[film]['Erscheinungsjahr']}")
    print(f"Bewertung: {filme[film]['Bewertung']}")