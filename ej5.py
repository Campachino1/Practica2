texto = input('ingrese una frase: ').lower()
palabra_clave= input('ingrese una palabra: ').lower()
texto = texto.lower()
texto_md = texto.split(' ')
cant = 0
for palabra in texto_md:
    if (palabra.startswith(palabra_clave))or(palabra.endswith(palabra_clave)):
        cant = cant + 1
print(f'la cantidad de veces que se repite la palabra: {palabra_clave} en el texto son: {cant}')        

