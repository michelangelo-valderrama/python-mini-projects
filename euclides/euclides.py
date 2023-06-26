

def main():
    # Se reciben los números
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))

    # Se imprime en pantalla la solución
    print(f"El mcd de {a} y {b} es: {mcd(a,b)}")


def mcd(a, b):
    n,m = 0,0  # n es el número mayor y m el menor
    r,i = 0,1  # r es el resto de una división y t es el valor de retornar

    # Obtener el mayor de a y b
    if a > b:
        n,m = a,b
    else:
        n,m = b,a

    # Se aplica el algoritmo de Euclides para obtener mcm
    while True:
        r = n % m  # resto del número mayor entre el número menor
        
        print(f"{i}. {n} dividido entre {m} es {n//m} y tiene de resto {r}")
        i+=1
        
        # Si el resto es cero, se ha acabado el algoritmo, sino...
        if r != 0:
            n = m  # Se asigna el anterior número menor como el nuevo número mayor 
            m = r  # Se asigna el anterior resto como el nuevo número número menor
        else:
            break 

    # Si el resto entre el número mayor y el número menor  
    # es cero, entonces el número menor es el mcd de ambos
    # números
    return(m)

main()
