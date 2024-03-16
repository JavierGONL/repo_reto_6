#los imports para el ejercicio 7

def promedio(numero1,numero2,numero3,numero4,numero5):
    solucion_promedio = (numero1 + numero2+ numero3+numero4+numero5)/5
    return  solucion_promedio

def mediana(numero1,numero2,numero3,numero4,numero5):
    while (numero1 > numero2 or numero2 > numero3 or numero3 > numero4 or numero4 > numero5):
        if numero1 > numero2:
            numero1,numero2 = numero2,numero1
        if numero2 > numero3:
            numero2,numero3 = numero3,numero2
        if numero3 > numero4:
            numero3,numero4 = numero4,numero3
        if numero4 > numero5:
            numero4,numero5 = numero5,numero4
    return numero3
    
def promedio_multiplicativo(numero1,numero2,numero3,numero4,numero5)->float:
    return (numero1 * numero2 * numero3 * numero4 * numero5) ** (1/5)

def numeros_de_forma_ascendente(numero1,numero2,numero3,numero4,numero5):
    while (numero1 > numero2 or numero2 > numero3 or numero3 > numero4 or numero4 > numero5):
        if numero1 > numero2:
            numero1,numero2 = numero2,numero1
        if numero2 > numero3:
            numero2,numero3 = numero3,numero2
        if numero3 > numero4:
            numero3,numero4 = numero4,numero3
        if numero4 > numero5:
            numero4,numero5 = numero5,numero4
    return [numero1,numero2,numero3,numero4,numero5]

def numeros_de_forma_descendente(numero1,numero2,numero3,numero4,numero5):
    while (numero1 > numero2 or numero2 > numero3 or numero3 > numero4 or numero4 > numero5):
        if numero1 > numero2:
            numero1,numero2 = numero2,numero1
        if numero2 > numero3:
            numero2,numero3 = numero3,numero2
        if numero3 > numero4:
            numero3,numero4 = numero4,numero3
        if numero4 > numero5:
            numero4,numero5 = numero5,numero4
    return [numero5,numero4,numero3,numero2,numero1] 
# :C

def la_potencia_del_numero_mayor_elevado_al_numero_menor(numero1,numero2,numero3,numero4,numero5):
    while (numero1 > numero2 or numero2 > numero3 or numero3 > numero4 or numero4 > numero5):
        if numero1 > numero2:
            numero1,numero2 = numero2,numero1
        if numero2 > numero3:
            numero2,numero3 = numero3,numero2
        if numero3 > numero4:
            numero3,numero4 = numero4,numero3
        if numero4 > numero5:
            numero4,numero5 = numero5,numero4
    return numero5 ** numero1

def raiz_cubica_menor_numero(numero1,numero2,numero3,numero4,numero5):
    while (numero1 > numero2 or numero2 > numero3 or numero3 > numero4 or numero4 > numero5):
        if numero1 > numero2:
            numero1,numero2 = numero2,numero1
        if numero2 > numero3:
            numero2,numero3 = numero3,numero2
        if numero3 > numero4:
            numero3,numero4 = numero4,numero3
        if numero4 > numero5:
            numero4,numero5 = numero5,numero4
    return numero1 ** (1/3)