# celsius a farenhit
celsius = [0, 15, 35, 38]; 
def faren (celsiii):
   return celsiii*9/5  + 32

convertido = map(faren, celsius)

def soloPar(n):
   return n%2==0; 

#se crea una lista donde solo hay pares. para filtrarlo
convertidoo = [4,7,8,2,4,7]
listaPares = filter(soloPar, convertidoo)

#de celsius a farenhit
print (list(convertido))

#lista pares usando el filter
print (list(listaPares))

#sorted con lambda para diccionarios

#se crea un diccionario de prueba
estudiantes = [

   {"nombres":"Ana", "nota":15},
   {"nombres":"juan", "nota":11},
   {"nombres":"Pedro", "nota":14},
   {"nombres":"Anasta", "nota":6}
]

resulta = sorted(estudiantes, key=lambda x:x ["nota"])
#se han ordenado por orden 
print(resulta)