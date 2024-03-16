

def interes_compuesto (interes, tiempo, capital):
    interesCompuesto = capital * (1 + interes) ** tiempo 
    return interesCompuesto

if __name__ == '__main__':
    interes = float(input("Ingrese el interes(mensual)(no en % PLS D:): "))
    tiempo = float(input("Ingrese el tiempo(meses): "))
    capital = float(input("Ingrese el capital: "))
    print("El interes compuesto es: ", interes_compuesto(interes, tiempo, capital))