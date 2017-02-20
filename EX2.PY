#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

while True:
    try:
        num = int(input ("Introduzca un número entero: "))
        divisor = int(input ("Introduzca un divisor: "))
        break
    except ValueError:
        print("Eso no parecen números enteros ¬¬ ")

if (num%2 == 0):
    par = "par"
else:
    par = "impar"

if (num%divisor==0):
    divisible = "divisible"
else:
    divisible = "no divisible"

if (num%4==0 and divisor!=4):
    cuatro = "y es multiplo de 4!"
else:
    cuatro = ""

print ("{} es un número {}, {} entre {} {}".format(num, par, divisible, divisor, cuatro))
