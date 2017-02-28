# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def pideNumero():
    while True:
        try:
            num = int(input ("Cuantos números de la secuencia de Fibonacci quieres que calcule?"))
            break
        except ValueError:
            print ("Error en la introducción de datos")
    #
    return num
#

def fib(num):
    fibonacci = [1,1]
    for a in range(num-2):
        fibonacci.append(fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2])
    return fibonacci
#

num = pideNumero()
fibonacci = fib(num)
print (fibonacci)
