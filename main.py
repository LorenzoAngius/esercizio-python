#!/usr/bin/env python3


def main():
    print("Calcolatrice \n")
    numero1 = int(input("Inserisci il primo numero: \n"))
    numero2 = int(input("Inserisci il secondo numero: \n"))
    operazione = input("Inserisci l'operazione che vuoi fare tra le seguenti: \n addizione\n sottrazione\n divisione\n moltiplicazione\n")
    if (operazione == "addizione"):
        print(numero1 + numero2)
    if (operazione == "sottrazione"):
        print(numero1 - numero2)
    if (operazione == "moltiplicazione"):
        print(numero1 * numero2)
    if (operazione == "divisione"):
        print(numero1 / numero2)
# Execute
if __name__ == '__main__':
    main()

