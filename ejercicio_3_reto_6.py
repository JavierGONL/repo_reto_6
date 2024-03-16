
PESO_GALLINAS = 6
PESO_GALLOS = 7
PESO_POLLITOS = 1

if __name__ == "__main__":
    gallinas = int(input("Ingrese la cantidad de gallinas: "))
    gallos = int(input("Ingrese la cantidad de gallos: "))
    pollitos = int(input("Ingrese la cantidad de pollitos: "))
    carne_total = ("hay exactamte",gallinas * PESO_GALLINAS) + (gallos * PESO_GALLOS) + (pollitos * PESO_POLLITOS,"kilos de carne en tot")