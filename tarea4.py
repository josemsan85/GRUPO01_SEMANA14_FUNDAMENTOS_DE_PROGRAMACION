#texto = input ("pon vocales ")
#contador = 0; 
#vocales = "aeiou"


def contarVocales(texto):
   contador =0; 
   vocales = "aeiouAEIUOáéíóú"

   for letra in texto:
      if letra in vocales:
         contador = contador + 1

   return contador

print (str(contarVocales("halala")))
#print ("se tiene el numero de vocales " + str(contarVocales("chancho")))