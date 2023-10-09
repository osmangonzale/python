def elementos_unicos(lista):
    lista_unicos = list(set(lista))
    return lista_unicos

mi_lista = [1, 2, 2, 3, 4, 4, 5, 6, 6]
lista_sin_duplicados = elementos_unicos(mi_lista)

print("Lista original:", mi_lista)
print("Lista sin duplicados:", lista_sin_duplicados)
