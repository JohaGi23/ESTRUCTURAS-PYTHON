#se declaran diccionarios= objetos

clienteUno={
    "id":5,
    "nombre":"edif1",
    "consumo":200
}

clienteDos={
    "id":5,
    "nombre":"edif2",
    "consumo":500
}

#se declara una lista= arreglo
clientesAsociados=[
    clienteUno,
    clienteDos
]

# y ahora que hago con esa lista?
#mi onjetivo sera obtener la informacion de la lista
#recorrer una lista o arreglo
#print(clientesAsociados)
'''for i in range(2):
    print(clientesAsociados[i]["consumo"])'''

#programemos un foreach que es un for
#especializado en recorrer arreglod(listas)

for cliente in clientesAsociados:
    print(cliente ["id"], '=>',cliente["consumo"],'kwh')
    print(f"{cliente["id"]}=>{cliente["consumo"]}kwh")