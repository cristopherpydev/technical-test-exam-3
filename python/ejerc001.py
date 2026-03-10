'''
DADA LISTA DE DICCIONARIOS DUPLICADOS - 

Implementa una función que:

Unifique usuarios duplicados por email (ignorando mayúsculas/minúsculas)
Devuelva una lista sin duplicados
Normalice los emails a minúsculas
Mantenga el primer nombre encontrado

users = [
    {"name": "Ana", "email": "ANA@MAIL.COM"},
    {"name": "Luis", "email": "luis@mail.com"},
    {"name": "ana", "email": "ana@mail.com"},
]
'''

def diccionarios_sin_duplica(lista_diccionario:list[dict])->dict:
    lista_auxiliar = []
    for elemento in lista_diccionario:
        if elemento["email"] not in lista_auxiliar:
            lista_auxiliar.append(elemento["email"].lower())

    return lista_auxiliar

if __name__ == '__main__':
    lista = diccionarios_sin_duplica([
    {"name": "Ana", "email": "ANA@MAIL.COM"},
    {"name": "Luis", "email": "luis@mail.com"},
    {"name": "ana", "email": "ana@mail.com"},
])
    print(lista)