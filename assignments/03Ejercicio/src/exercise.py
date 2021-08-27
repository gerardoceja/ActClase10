def main() :
   #introduce el codigo
   def operaciones(num1,num2,letra):
       if letra== "s":
           suma= num1+num2
           return suma
       elif letra== "r":
           resta= num1-num2
           return resta
       elif letra== "m":
           multi= num1*num2
           return multi
       elif letra== "d":
           divi= num1/num2
           return divi
   def main() :
           tob=int(input("introudcir valor 1: "))
           andr=int(input("introudcir valor 2: "))
           tom=input("introducir clave  (s, r, m, d): ")
           calculo= operaciones(tob,andr,tom)
           print("resultado:",calculo)
        



if __name__=='__main__':
    main()
