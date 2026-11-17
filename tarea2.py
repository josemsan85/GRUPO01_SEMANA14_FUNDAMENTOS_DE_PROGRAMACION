def calcular (a,b, operador):
    if (operador == "-" ):
        return a - b
    elif (operador == "+"):
        return a+b 
    elif(operador == "*"):
        return a*b 
    elif(operador == "/"):
        #se anida otro if para hacer la comparacion con el 
        #denominador igual cero en division
        if (b==0):
            return None
        else :
         return a/b 
   
    return None

print ( str ( calcular(4,0,"7") ))