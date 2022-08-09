# calcular raízes de uma equação do segundo grau

def raizes(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)

    print('\nValor de x1: {0}'.format(x1))
    print('Valor de x2: {0}'.format(x2))


if __name__ == '__main__':
    while True:
        print("Calculando...\n")
        a = float(input('valor de a: '))
        b = float(input('valor de b: '))
        c = float(input('valor de c: '))
        raizes(a,b,c)


        continua = input("digite q ou enter para novo cálculo")
        if (continua == 'q'):
            break
