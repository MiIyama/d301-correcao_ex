meninos = ['Luiz', 'João', 'Alex', 'Guilherme']
meninas = ['Lais', 'Lolo','Ana']

todos = meninos + meninas

i = 1

for pessoa1 in meninos: #ver se esta certo
    for pessoa2 in todos:
        for pessoa2 in todos:
           if pessoa1 != pessoa2:
            print(f'Parzinho {i}:{pessoa1} e {pessoa2}')
            i +=1

# **********************************************************************************
meninos = ['Luiz', 'João', 'Alex', 'Guilherme']
meninas = ['Lais', 'Lolo','Ana']

todos = meninos + meninas

i = 1

for pessoa1 in meninos: #ver se esta certo
    for pessoa2 in todos:
        for pessoa2 in todos:
           if pessoa1 != pessoa2:
            print(f'Parzinho {i}:{pessoa1} e {pessoa2}')
            i +=1

todos.remove(pessoa1)

# ta pulando de 2 em 2 - errado
# ***************************************************************************** audio: antes 52m a 56min audio 
meninos = ['Luiz', 'João', 'Alex', 'Guilherme']
meninas = ['Lais', 'Lolo','Ana']

todos = meninos + meninas

i = 1
j = 0

for pessoa1 in todos:
    for k in range(j, len(todos)):
        if pessoa1 != todos[k]:
            print(f'Parzinho {i}:{pessoa1} e {todos[k]}')
            i +=1

    j += 1




