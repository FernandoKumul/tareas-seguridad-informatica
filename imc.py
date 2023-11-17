def imc(peso, altura):
    return peso/ altura**2

def nive_de_peso(imc):
    
    if imc < 18.5:
        return "Peso bajo"
    elif 18.5 <= imc > 25:
        return  "Peso normal"
    elif 25 <= imc > 30:
        return "Sobrepeso"
    else:
        return "Obesidad"