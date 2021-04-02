frase = input('ingrese una frase: ').lower()


frase = frase.split(' ')

palabras_repetidas = []
palabras_sinrepetir = []



for palabra in frase:
    if not(palabra in palabras_repetidas):
        if (frase.count(palabra)==1):
            palabras_sinrepetir.append(palabra)
        else:
            palabras_repetidas.append(palabra)
print(palabras_sinrepetir)

