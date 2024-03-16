#los imports para el ejercicio 7

def promedio(numero1,numero2,numero3,numero4,numero5):
    solucion_promedio = (numero1 + numero2+ numero3+numero4+numero5)/5
    return  solucion_promedio

def mediana(numero1,numero2,numero3,numero4,numero5):
    numeros = [numero1,numero2,numero3,numero4,numero5]
    numeros.sort()
    return numeros[2]
    # intente darle solucion por medio de casos tipo caso 1 numero1>numero2>numero3>numero4>numero5
    # pero no me funciono porque en total tenia que hacer 120 casos y en el caso 20 me canse y use el codigo de la solucion actual
    # en google encontre que el sort te ordena de menor a mayor y si es par te da el promedio de los dos numeros centrales
    # y si es impar te da el numero central y como es impar siempre el numero del medio es la mediana siempre
    
def promedio_multiplicativo(numero1,numero2,numero3,numero4,numero5)->float:
    return (numero1 * numero2 * numero3 * numero4 * numero5) ** (1/5)

def numeros_de_forma_ascendente(numero1,numero2,numero3,numero4,numero5)->float:
    numeros = [numero1,numero2,numero3,numero4,numero5]
    numeros.sort()
    return numeros
#otra vez habian muchos casos y use la funcion esta del sort :c 

def numeros_de_forma_descendente(numero1,numero2,numero3,numero4,numero5):
    numeros = [numero1,numero2,numero3,numero4,numero5]
    numeros.sort()
    lista_ordenada_descendente = numeros[4],numeros[3],numeros[2],numeros[1],numeros[0]
    return lista_ordenada_descendente
# :C

def la_potencia_del_numero_mayor_elevado_al_numero_menor(numero1,numero2,numero3,numero4,numero5):
    numeros = [numero1,numero2,numero3,numero4,numero5]
    numeros.sort()
    return numeros[4] ** numeros[0]

def raiz_cubica_menor_numero(numero1,numero2,numero3,numero4,numero5):
    numeros = [numero1,numero2,numero3,numero4,numero5]
    numeros.sort()
    return numeros[0] ** (1/3)