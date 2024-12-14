euro = 6.07
dolar = 5.44

def conv(cotacao, real): 
    return real / cotacao  

real = float(input("Real: "))
print("Dólar: ", conv(dolar, real))
print("Euro: ", conv(euro, real))
