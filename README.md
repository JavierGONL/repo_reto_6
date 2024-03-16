
<div align='center'>
<figure> <img src="https://i.postimg.cc/HkMddSNw/error-418.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

# reto_6

1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
import math

PI = math.pi

def calcular_area_superficial(radio:float)->float:
    return 4*PI*radio**2

def calcular_volumen_esfera(radio:float)->float:
    return (4/3) * PI * radio ** 3

if __name__ == "__main__":
    volumen_o_area = float(input("calcular volumen o area(coloca 1 para volumen  y 0 para area superficial): "))
    if volumen_o_area == 1:
        radio = float(input("Ingresa el radio de la esfera: "))
        print("el volumen de la esfera es: ", calcular_volumen_esfera(radio))
    elif volumen_o_area == 0: 
        radio = float(input("Ingresa el radio del area superfical: "))
        print("el area superficial es: ", calcular_area_superficial(radio))
    else:
        print("valor no valido")

  ```

2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*


```python
import math

PI = math.pi

def calcular_area(radio, base, altura):
    area_circulo = PI * radio ** 2
    area_cuadrado = base * altura
    return area_circulo,area_cuadrado

def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

if __name__ == "__main__":
    area_cuadrado_o_circulo = input("area cuadrado o circulo(1 para circulo y 0 para cuadrado): ")
    if area_cuadrado_o_circulo == "1":
        radio = float(input("Ingresa el radio del circulo: "))
        print("el area del circulo es: ", PI * radio ** 2)
        print("el perimetro del circulo es: ", 2 * PI * radio)
    else:
        base = float(input("Ingresa la base del cuadrado: "))
        altura = float(input("Ingresa la altura del cuadrado: "))
        print("el area del cuadrado es: ", base * altura)
        print("el perimetro del cuadrado es: ", 2 * (base + altura))

```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
PESO_GALLINAS = 6
PESO_GALLOS = 7
PESO_POLLITOS = 1

if __name__ == "__main__":
    gallinas = int(input("Ingrese la cantidad de gallinas: "))
    gallos = int(input("Ingrese la cantidad de gallos: "))
    pollitos = int(input("Ingrese la cantidad de pollitos: "))
    carne_total = ("hay exactamte",gallinas * PESO_GALLINAS) + (gallos * PESO_GALLOS) + (pollitos * PESO_POLLITOS,"kilos de carne en total")
```



4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
PANES = 300
BOLSAS_LECHE = 3300
HUEVOS = 350

if __name__ == '__main__':
    P_panes = float(input("Cuantos panes quieres comprar:"))
    L_bolsas_leche = float(input("Cuantas bolsas de leche quieres comprar:"))
    H_huevos = float(input("Cuantos huevos quieres comprar:"))
    pago = float(input("con cuanto vas a pagar:"))
    if pago < (P_panes*PANES + L_bolsas_leche*BOLSAS_LECHE + H_huevos*HUEVOS):
        print("No te alcanza para comprar todo eso")
    else:
        vueltas = pago - (P_panes*PANES + L_bolsas_leche*BOLSAS_LECHE + H_huevos*HUEVOS)
        print("mi mama me mando a comprar",P_panes,"panes,",L_bolsas_leche,"bolsas de leche y",H_huevos, " huevos y me dieron de vueltos ",vueltas,"pesos")
```
5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```python
def interes_compuesto (interes, tiempo, capital):
    interesCompuesto = capital * (1 + interes) ** tiempo 
    return interesCompuesto

if __name__ == '__main__':
    interes = float(input("Ingrese el interes(mensual)(no en % PLS D:): "))
    tiempo = float(input("Ingrese el tiempo(meses): "))
    capital = float(input("Ingrese el capital: "))
    print("El interes compuesto es: ", interes_compuesto(interes, tiempo, capital))
```
6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
if __name__ == "__main__":
    contagiados = input("numero de contagiados(inicial): ")
    numero_dias = input("numero de dias(desde hoy): ")
    tasa_contagio = 2**numero_dias #tasa de contagio exponencial
    print("numero de contagiados en ", numero_dias, "dias: ", contagiados*tasa_contagio)
```
7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python

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
```
8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
```python
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
```
9. Consultar qué es y cómo funciona *pip* en python.
- que es pip?
- pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.
- como funciona?
 puedes instalar paquetes de sofware con el siquiente comando:
  ```
  pip install nombre-paquete
  ```
  También puedes instalar paquetes desde un archivo de texto -por ejemplo, un archivo de requisitos para un proyecto- con el siguiente comando.
  ```
  pip install -r requirements.txt
  ```
  tambien puedes desinstalar programas con el comando
  ```
  pip uninstall nombre-paquete
  ```
10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.
+ listado de programas populares
  ```

  
  ```
