# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print ("Lista original")
for i in range(len(a)):
    if (i != (len(a))-1):
        print ("{}, ".format(a[i]), end="")
    else:
        print ("{}.".format(a[i]))
    #
#

menores5 = []
while True:
    try:
        lt = int(input ("Inserte el valor de corte: "))
        break
    except ValueError:
        print ("Inserte un valor entero")
#

for item in a:
    if (item<lt):
        menores5.append(item)
    #
#

for i in range(len(menores5)):
    if (i != (len(menores5))-1):
        print ("{}, ".format(menores5[i]), end="")
    else:
        print ("{}.".format(menores5[i]))
#
