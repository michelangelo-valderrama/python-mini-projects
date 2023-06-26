def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if a != 0:
        roots = qua(a, b, c)
        print("x_1 = " + str(roots[0]) + "; " + "x_2 = " + str(roots[1]))
    else:
        print("a no puede ser igual a cero...")
        

def qua(a, b, c):
    if a == 0:
        print("a =/= 0")
        return
    else: 
        x_1 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
        x_2 = (-b-(b**2 - 4*a*c)**(1/2))/(2*a)
        if type(x_1)==type(complex()):
            x_1 = complex(round(x_1.real, 6), round(x_1.imag, 6))
            x_2 = complex(round(x_2.real, 6), round(x_2.imag, 6))
        else:
            x_1 = round(x_1, 6)
            x_2 = round(x_2, 6)
        x = [x_1, x_2]

        r_1 = a*(x_1**2)+b*x_1+c
        r_2 = a*(x_2**2)+b*x_2+c
        if type(r_1)==type(complex()):
            r_1 = complex(round(r_1.real, 2), round(r_1.imag, 2))
            r_2 = complex(round(r_2.real, 2), round(r_2.imag, 2))
        else:
            r_1 = round(r_1, 2)
            r_2 = round(r_2, 2)
        print("x_1 -> " + str(a) + "(" + str(x_1) + ")^2" + " + " + str(b) + "(" + str(x_1) + ")" + " + " + str(c) + " = " + str(r_1))
        print("x_2 -> " + str(a) + "(" + str(x_2) + ")^2" + " + " + str(b) + "(" + str(x_2) + ")" + " + " + str(c) + " = " + str(r_2))
        return x


main()