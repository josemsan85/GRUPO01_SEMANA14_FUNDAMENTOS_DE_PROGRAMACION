def clasificarTemperatura (temper):
    # 30 20 10 
    if (temper >= 30 ):
        return "caliente >= 30"
    elif (temper < 30 and temper >= 20):
        return "calido < 30"
    elif (temper < 20 and temper >= 10):
        return "Fresco < 20"
    elif (temper < 10 and temper >= 0):
        return "Frio < 10"

print( clasificarTemperatura (25) )