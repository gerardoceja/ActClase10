def main() :
   #introduce el codigo
   def areaRect(a,1):
       area=1*a
       return area

   def perimetroRect(a,1):
       perimetro=(1*2)+(a*2)
       return perimetro
   def main() :
       x=float(input("Ingresa el ancho: "))
       y=float(input("Ingresa el largo: "))
       print("Quiere calcular el area o el perimetro del rectangulo:")
       print("(a para area y p para perimetro)")
       agnes=input("op: ")

       if agnes== "p":
           pietro=perimetroRect(x,y)
           print("perimetro",pietro)

if __name__=='__main__':
    main()
