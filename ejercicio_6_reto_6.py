

if __name__ == "__main__":
    contagiados = input("numero de contagiados(inicial): ")
    numero_dias = input("numero de dias(desde hoy): ")
    tasa_contagio = 2**numero_dias #tasa de contagio exponencial
    print("numero de contagiados en ", numero_dias, "dias: ", contagiados*tasa_contagio)