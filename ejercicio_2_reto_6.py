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