

def main():
    # Se recibe la cantidad de números de la sucesión
    t = int(input("¿Cuántos números quiere de la sucesión? "))

    # Se guarda la sucesión en fib
    fib = fibonacci(t)

    print(*[o for o in fib])  # Se imprime en pantalla

    # for i in range(t):
    #     print(f"Término {i+1}: {fib[i]}")
    
    print("Fin de la sucesión")


def fibonacci(t):
    F = [0, 1]  # F es la lista donde se crea la sucesión
    #  F[0]=0, F[1]=1, ... F[n] = F[n-1] + F[n-2]

    # Se crea la sucesión
    for i in range(2,t): F.append(F[i-1] + F[i-2])
    return F


main()
