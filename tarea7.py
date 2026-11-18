# celsius a farenhit
celsius = [0, 15, 35, 38]; 
def faren (celsiii):
   return celsiii*9/5  + 32

convertido = map(faren, celsius)

print (list(convertido))