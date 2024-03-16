
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

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

9. Consultar qué es y cómo funciona *pip* en python.

10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.
