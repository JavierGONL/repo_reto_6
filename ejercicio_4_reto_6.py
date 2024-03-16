

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