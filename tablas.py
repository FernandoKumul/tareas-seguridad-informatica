# Tabla infinita 1x1 = 1

# el usuario va a definir el multiplicando y el multiplicador  y el tamaño de la tabla
tabla_inicio = int(input("Tabla de inicio: "));
tabla_final = int(input("Tabla final: "));

multiplicador_inicio = int(input("Multiplicador de inicio: "));
multiplicador_final = int(input("Multiplicador final: "));

print("\n")

for i in range(tabla_inicio, tabla_final + 1):
    for j in range(multiplicador_inicio, multiplicador_final + 1):
        print(f"{i} x {j} = {i * j}")
    print("\n")