def sumar(a, b):
    c = a + b
    return c

def restar(a, b):
    return a -b

def multiplicar(a, b):
    return a*b

def div_entera(a, b):
    if b == 0:
        print("Error division sobre cero")
        return
    return a//b

def division(a, b):
    if b == 0:
        print("Error division sobre cero")
        return
    return a//b

def modulo(a, b):
    if b == 0:
        print("Error division sobre cero")
        return
    return a%b

def potencia(a, b):
    return a**b

def main():
    print("Ingresa dos valores")
    x = int(input()) #recibe desde el teclado
    y= int(input())

#MENU
    print("1. Sumar\n2. Restar\n3. Division Entera")
    print("4. Division\n5. Modulo\n6. Potencia\n7. Multiplicar\n")
    op = int(input())

    var = True
    var = False
    # Operadores de c 
    # && ||
    # and or

#while True :
    
    if op == 1:
        print (sumar(x, y))
    elif op ==2:
        print(restar(x, y))
    elif op ==3:
        print(div_entera(x, y))
    elif op ==4:
        print(division(x, y))
    elif op ==5:
        print(modulo(x, y))
    elif op ==6:
        print(potencia(x, y))
    elif op ==7:
        print(multiplicar(x, y))
    else:
        print("Opcion NO valida")

#Quieres decir que este archivo direcatamnte es decir lo ejecuto desde cal.py mando llamar la verison main, si no este archvo no ejecutar la version de main
if __name__ == "__main__":
    main()
