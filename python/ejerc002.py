'''[1, 2, 3, 4] -> "increasing"
   [4, 3, 2] -> "decreasing"
   [1, 3, 2] -> "mixed"
   
'''

'''Escribe una función que reciba una lista de números y devuelva:

"increasing" si está estrictamente en aumento
"decreasing" si está estrictamente en descenso
"mixed" en cualquier otro caso'''

def determinar_aumento_descenso_mixed(lista_numerica:list[int])->str:
    '''Si el número está en aumento significa que los diferentes números de las posiciones de la lista son crecientes'''
    numero = 0
    numero_anterior = 0
    es_creciente = False
    es_decreciente = False
    for i in range(len(lista_numerica)):
        if i == 0:
            numero_anterior = lista_numerica[i]
        numero = lista_numerica[i]
        if numero > numero_anterior:
            numero_anterior = numero
            es_creciente = True
        elif numero < numero_anterior:
            numero_anterior = numero
            es_decreciente = True
    if es_creciente:
        return "increasing"
    elif es_decreciente:
        return "decreasing"
    return "mixed"

            
        

if __name__ == '__main__':
    print(determinar_aumento_descenso_mixed([1, 2, 3, 4]))
    print(determinar_aumento_descenso_mixed([4, 3, 2]))
    print(determinar_aumento_descenso_mixed([1, 3, 2]))