import matematicas
while True:
    print("\n== Menú de operaciones ==")
    print("1. Suma")
    print("2. Resta")
    print("3. división")
    print("4. Multplicación")
    print("5. Raíz cuadrada")
    print("6. Exponente al cuadrado")
    print("7. Cancelar")
    
    opcion = int(input("Elige la operación: "))
    
    if opcion == 1:
        num1 = int(input("Primer número: "))
        num2 = int(input("Segundo número: "))
        print(f"Resultado: {suma.sumar(num1, num2)}")
    elif opcion == 2:
        num1 = int(input("Primer número: "))
        num2 = int(input("Segundo número: "))
        print(f"Resultado: {resta.restar(num1, num2)}")
    elif opcion == 3:
        num1 = int(input("Primer número: "))
        num2 = int(input("Segundo número: "))
        print(f"Resultado: {division.dividir(num1, num2)}")
    elif opcion == 4:
        num1 = int(input("Primer número: "))
        num2 = int(input("Segundo número: "))
        print(f"Resultado: {multiplicacion.multplicar(num1, num2)}")
    elif opcion == 5:
        num1 = int(input("Número: "))
        print(f"Resultado: {raiz.raiz_cuadrada(num1)}")
    elif opcion == 6:
        num1 = int(input("Número: "))
        print(f"Resultado: {exponente.cuadrado(num1)}")
    elif opcion == 7:
        break
    else:
        print("No existe esa opción")