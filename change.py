def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(float(expense))
    print("Dinero recibido")
    print(int(money))
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    vuelto = money - expense
    print(int(vuelto))
    pesos = int(vuelto)
    centavos = (vuelto - pesos)*100
    print("Centavos:")
    print(int(centavos))
#change()