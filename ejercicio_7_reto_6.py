
from ejercicio_8_reto_6 import *

if __name__ == "__main__":
    print("se le va a pedir 5 numeros :] ")
    numero1 = float(input("numero 1:"))
    numero2 = float(input("numero 2:"))
    numero3 = float(input("numero 3:"))
    numero4 = float(input("numero 4:"))
    numero5 = float(input("numero 5:"))
    print("El promedio de los numeros es:", promedio(numero1,numero2,numero3,numero4,numero5))
    print("La mediana de los numeros es:", mediana(numero1,numero2,numero3,numero4,numero5))
    print("El promedio multiplicativo de los numeros es:", promedio_multiplicativo(numero1,numero2,numero3,numero4,numero5))
    print("Los numeros de forma ascendente son:", numeros_de_forma_ascendente(numero1,numero2,numero3,numero4,numero5))
    print("Los numeros de forma descendente son:", numeros_de_forma_descendente(numero1,numero2,numero3,numero4,numero5))
    print("La potencia del numero mayor elevado al numero menor es:", la_potencia_del_numero_mayor_elevado_al_numero_menor(numero1,numero2,numero3,numero4,numero5))
    print("La raiz cubica del menor numero es:", raiz_cubica_menor_numero(numero1,numero2,numero3,numero4,numero5))