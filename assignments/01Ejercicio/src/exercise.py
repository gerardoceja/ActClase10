def main():
    # Escribe tu código abajo de esta línea
    h=int(input("Dame las horas"))
    m=int(input("Dame los minutos"))
    s=int(input("Dame los segundos"))
    h=h*3600
    m=m*60
    print(h+m+s)

if __name__ == '__main__':
    main()
