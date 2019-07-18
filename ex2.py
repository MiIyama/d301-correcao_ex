import random

def embaralhar(lista):
    for i in range(len(lista) -1, 0, -1):
        indice_aleatorio = random.randint(0,i)

        valor_temporario = lista[i]
        lista[i] = lista[indice_aleatorio] 
        lista[indice_aleatorio] = valor_temporario 
    return lista 

valores = [1,2,3,4,5,6,7,8]

embaralhado = embaralhar(valores)
print(embaralhado)

# *****************************************************
# Já ta pronta essa funçao
valores = [1,2,3,4,5,6,7,8]
random.shuffle(valores)
