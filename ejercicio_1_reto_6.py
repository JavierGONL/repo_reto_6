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