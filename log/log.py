import math as m


def main():
    a = int(input("Argumento: "))
    b = input("Base (e, 10 o 2): ")

    if a == 0: 
        print("El argumento no puede ser cero")
        return

    if b == 'e':
        b = m.e
        print(f"El logaritmo en base e de {a} es: {lg(a, b)}. {b**(lg(a, b))}")
        return

    b = int(b)
    if b == 10 or b == 2:
        print(f"El logaritmo en base {b} de {a} es: {lg(a, b)}")
    else:
        print("Escoga una base permitida")


def lg(a, b):
    ipi = complex(0, 1)*m.pi
    r = 0

    if a < 0:
        r = m.log(-a) + ipi/m.log(b)
        return complex(round(r.real, 4), round(r.imag, 4))
    else:
        if b == m.e: r = m.log(a)
        if b == 10: r = m.log10(a)
        if b == 2: r = m.log2(a)
        return round(r, 4)


main()
