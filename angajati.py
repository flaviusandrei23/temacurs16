import csv

def adauga_angajat():
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    salariu = input("Salariu: ")

    with open("angajati.csv", "a", newline=" ") as file:
        writer = csv.writer(file)
        writer.writerow([nume, prenume, salariu])



if __name__ == "__main__":
    adauga_angajat()
