numero = 45
control = 0 
intentos = 1
print("bienvenido a este programa")
while(control==0):
    print("Intento numero",intentos)
    print("Ingrese un numero")
    num = int(input())
    if(num==numero):
        print("adivinaste el número")
        print("fin del programa")
        control = 1
    elif(num > numero):
        print("el numero ingresado es mayor que el numero que buscas")
        intentos+=1
    elif(num < numero):
        print("el numero ingresado es menor que el numero que buscas")
        intentos+=1
        