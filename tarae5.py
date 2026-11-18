import csv
import os 

rut = os.path.join(os.getcwd(), "jj.csv")

print(rut)

alumnosAprov = 0
listNotas = [] 


with open (rut, "r", encoding="utf-8") as archivo:
    lector =csv.DictReader(archivo)
    
    for fila in lector:
        #print(fila)
        #los datos que se agregan estan en formato texto que se 
        #tienen que convertir a numero entero
        listNotas.append(int (fila["notas"]))

        print("valor: ", fila["notas"])
      

notaMayor =listNotas[0]

for nume in listNotas:
    if nume > notaMayor:
        notaMayor = nume  
    if nume >= 13:
        alumnosAprov +=1

print("alumnos aprovados " + str(alumnosAprov))
print("mayor nota " + str(notaMayor))
print ("promedio es " + str(sum(listNotas) / len(listNotas)))

#print (len(listNotas))

#print("la mayor nota es " +  max(listNotas) )