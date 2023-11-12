import csv

def adauga_angajat():
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    salariu = input("Salariu: ")

    with open("angajati.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([nume, prenume, salariu])



if __name__ == "__main__":
    adauga_angajat()


import csv

def stergere_angajat():
    nume_sters = input("Introduceti numele angajatului de sters: ")

    with open("angajati.csv", "r") as file:
        reader = csv.reader(file)
        angajati = list(reader)
        angajati_noi = [angajat for angajat in angajati if angajat[0] != nume_sters]


    with open("angajati.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(angajati_noi)


if __name__ == "__main__":
    stergere_angajat()