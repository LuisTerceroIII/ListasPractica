#Practica 5 - Listas
#Ejercicio 1
animals = ["Elefante" , "Jirafa", "Mono"]
def addAnimal(animal):
    animals.append(animal)
#Ejercicio 2
# Recorrer lista por elemento
def printOneForLine(lista):
    for element in lista:
        print(element)
# Recorrer lista por posicion usando for
def printOneForLine2(lista):
    for i in range(len(lista)):
        print(lista[i])
# Recorrer lista por posicion usando while
def printOneForLine3(lista):
    i = 0
    while(i<len(lista)):
        print(lista[i])
        i = i + 1
#Ejercicio 3
def listOfDividers(number):
    dividers = []
    for i in range(1,number + 1):
        if(number % i == 0):
            dividers.append(i)
    return dividers
#Ejercicio 4
def shortestList(list1,list2):
    if(len(list1)<len(list2)):
        return list2
    else:
        return list1
#Ejercicio 5
def areFactors(number, list1):
    list2 = []
    for element in list1:
        if(number % element == 0):
            list2.append(element)
    return len(list1) == len(list2)
#Ejercicio 6
def invertList(list1):
    copy = []
        for i in range(len(list1)-1,-1,-1):
            copy.append(list1[i])
        return copy

def eraseRepeats(list1):
    repeat = 0
    copy = invertList(list1)
    for element in list1:
        for e in copy:
            if(element == e):
                repeat = repeat + 1
    return repeat > len(list1)

#Ejercicio 7
def appearsIn(list1, number):
    index = -1
    for i in range(len(list1)):
        if(number == list1[i]):
            return i
    return index
#Ejercicio 8
def average(list1):
    addition = 0 
    for element in list1:
        addition = addition + element
    return addition/len(list1)

#Ejercicio 9
def maxValue(list1):
    maxElement = list1[0]
    for element in list1:
        if(maxElement<element):
            maxElement = element
    return maxElement
#Ejercicio 10
def indexMax(list1):
    index = 0
    maxElement = list1[0]
    for i in range(len(list1)):
        if(maxElement>element):
            index = i
    return index
#Ejercicio 11
def maxBetween(list1, number1, number2):
    a = 0
    b = 0
    if(number1 < number2):
        a = number1
        b = number2
    else:
        a = number2
        b = number1
######################
    maxE = list1[a]
    index = 0
######################
    for i in range(len(list1)):
        if(i >= a and i <= b):
            if(maxE<=list1[i]):
                maxE = list1[i]
                index = i
    return index

#Ejercicio 12
def swapElement(list1,a,b):
    aux = list1[a]
    list1[a] = list1[b]
    list1[b] = aux
#Ejercicio 13
def frequent(list1, number):
    appear = 0
    for element in list1:
        if(element == number):
            appear = appear + 1
    return appear
#Ejercicio 14
def intersection(list1,list2):
    intersectionList = []
    for element in list1:
        for i in range(len(list2)):
            if(element == list2[i]):
                intersectionList.append(list2[i])
    return intersectionList
#Ejercicio 15
def appear(list1,element):
    for i in range(len(list1)):
        if(element == list1[i]):
            return True
    return False

def union(list1, list2):
    unionList = []
    for element in list1:
        if(not appear(unionList,element)):
            unionList.append(element)
    for i in range(len(list2)):
        if (not appear(unionList,list2[i])):
                unionList.append(list2[i])
    return unionList

#Ejercicio 16
def difference(list1,list2):
    differenceList = []
    for element in list1:
        for i in range(len(list2)):
            if(not appear(list2,element) and not appear(differenceList,element)):
                differenceList.append(element)
    return differenceList

#Ejercicio 17
def mcd(number1, number2):
    dividers1 = listOfDividers(number1)
    dividers2 = listOfDividers(number2)
    cd = union(dividers1,dividers2)
    return maxValue(cd)

#Ejercicio 18
def isPrime(number):
    dividers = 0
    for i in range(1,number+1):
        if(number%i == 0):
            dividers = dividers + 1
    return dividers == 2

def firstsPrimes(number):
    primes = []
    for i in range(1,number+1):
        if(number%i == 0 and isPrime(i)):
            primes.append(i)
    return primes

#Ejercicio 19
def factorize(number):
    play = True
    i = 2
    cont = 0
    factors = []
    while(play):
        if(number%i == 0):
            factors.append(i)
            number = number / i
        else:
            i = i + 1
            cont = cont + 1
            if(cont > 4):
                play = False
    return factors
#Ejercicio 20
def smallerThan(list1, number):
    count = 0
    for element in list1:
        if(element < number):
            count = count + 1
    return count #solo devuelve la cantidad de elementos menores al numero ingresado

def orderMinToMax(list1):
    for e in range(1,len(list1)):
        for i in range(len(list1) - e):
            if(list1[i] > list1[i+1]):
                swapElement(list1,i,i+1)

#Ejercicio 21
def smallerThanX(list1,x):
    for i in range(len(list1)):
        if(list1[i] < x):
            list1[i] = 0 

#Ejercicio 22
def invertString(string):
    copy = ""
    for char in string:
        copy = char + copy
    return copy

def timesEachLetter(string):
    copy = invertString(string)
    cont = 0
    list1 = []
    for char in string:
        for char1 in copy:
            if(char == char1):
                cont = cont + 1
        element = char + " : " + str(cont)
        if(not appear(list1,element)):
            list1.append(element)
        cont = 0
    for elemento in list1:
        print(elemento)

#Ejercicio 23
def timesEachLetter2(string):
    copy = invertString(string)
    cont = ""
    list1 = []
    for char in string:
        for char1 in copy:
            if(char == char1):
                cont = cont + "*"
        element = char + " : " + cont
        if(not appear(list1,element)):
            list1.append(element)
        cont = ""
    for elemento in list1:
        print(elemento)
    
#Ejercicio 24
def pagara(cliente,localidad):
    total = 0
    if(cobertura(cliente) == Oro):
        if(radioDeCobertura(localidad,cliente) == False):
            total = total + 30 
    else:
        if(usados(cliente) >= 5):
            total = total + 50
        if(radioDeCobertura(localidad,cliente) == False):
            total = total + 30
    return total

#Ejercicio 25
def controlRuta100(ruta):
    patentes = darPatentes(ruta)
    for patente in patentes:
        if(controlVelocidad(patente) > 100):
            if(reincidente(patente) == True):
                 enviarMulta(patente,costoActual()*2)
            else:
                 enviarMulta(patente,costoActual())
    
                
    
