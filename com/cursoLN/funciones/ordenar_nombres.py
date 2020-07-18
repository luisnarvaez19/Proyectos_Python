'''
  Dada una lista de personas (Con nombre y apellido) ordenarlas ascendentemente por el nombre
'''

# def existeApellido(apellido, nombreCompleto):
#     division = nombreCompleto.split(' ')
#     return apellido == division[1]

def existeApellido(apellido, nombreCompleto):
    return apellido == nombreCompleto.split(' ')[1]

# def cortarNombres(lista):
#     resultado = []
#     for nombre in lista:
#         division = nombre.split(' ')
#         apellido = division[1]
#         resultado.append(apellido)
#     return resultado

def cortarNombres(lista):
    resultado = []
    for nombre in lista:
        resultado.append(nombre.split(' ')[1])
    return resultado

'''
    Esta funcion ordena la Lista de personas dada una lista de apellidos
'''
def ordenar(listaPersonas, listaApellidos):
    resultado = []
    for apellido in listaApellidos:
        for nombre in listaPersonas:
            if existeApellido(apellido, nombre):
                resultado.append(nombre)
    return resultado

personas = ['Marcos Perez', 'Gustavo Adolfo', 'Marina Marques', 'Pedro Barrada']

#  print(sorted(personas))

apellidos = cortarNombres(personas)

apellidos = sorted(apellidos)

final = ordenar(personas, apellidos)

print(final)

