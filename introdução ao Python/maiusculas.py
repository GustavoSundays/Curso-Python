def maiusculas(frase):
    frase_maiuscula = frase.upper()
    letras_maiusculas = ''
    for i in range(len(frase)):
        if frase[i].isnumeric() == False and frase[i].isspace() == False:
            if frase[i] != "!" and frase[i] != "?" and frase[i] != "." and frase[i] != ",":
                if frase_maiuscula[i] == frase[i]:
                    letras_maiusculas += frase[i]
    return letras_maiusculas


frase = maiusculas('PrOgRaMaMoS em python!')
print(frase)