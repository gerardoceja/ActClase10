def main():
    # Escribe tu código abajo de esta línea
    def equivalente(hr,mn,sg):
        st = hr*3600+mn*60+sg
        return st

    print("proceso 1")
    h = int(input("Introduce las horas: "))
    m = int(input("Introduce las minutos: "))
    s = int(input("Introduce las segundos: "))

    eq1 = equivalente(h,m,s)

    print("proceso 2:")
    h = int(input("Introduce las horas: "))
    m = int(input("Introduce las minutos: "))
    s = int(input("Introduce las segundos: "))

    eq2 = equivalente(h,m,s)

    print("proceso 1:", eq1)
    print("proceso 2:", eq2)

if __name__ == '__main__':
    main()
