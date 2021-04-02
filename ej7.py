NOMBRES =['Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina']
eval1 = """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
 """

eval2= """30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
 """

eval1 = eval1.split(',')
eval1_mod = []
for num in eval1:
    eval1_mod.append(int(num))
eval2 = eval2.split(',')
eval2_mod = []
for num in eval2:
    eval2_mod.append(int(num))
i = 0
Estudiantes = []

for nom in NOMBRES:
    if not(nom.startswith(',')):
        nota = eval1_mod[i] + eval2_mod[i]
        estudiante = {'Nombre' : nom, 'Nota': nota}
        Estudiantes.append(estudiante)
        i = i+1
promedio_total = 0
for E in Estudiantes:
    promedio_total = promedio_total + E.get('Nota')
promedio_total = promedio_total / len(Estudiantes)
print(f"Los siguentes Estudiantes no superaron el promedio de: {promedio_total}")
for E in Estudiantes:
    if (E.get('Nota')<promedio_total):
        print(f"{E.get('Nombre')} con la nota de : {E.get('Nota')}")
        
        
