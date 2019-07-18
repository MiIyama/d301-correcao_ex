print("Qual a sua idade?")
idade = int(input())

print("Qual o valor do emprestimo?")
valor_emprestimo = float(input())

print("Qual o seu salario?")
salario = float(input())

print("Quantas parcelas?")
qtd_parcelas = int(input())

def emprestimo(idade, valor_emprestimo, salario, qtd_parcelas):
    if idade <= 22 and idade >= 55 and valor_emprestimo <=1000 and valor_emprestimo > salario * 15 and qtd_parcelas <= 3 and qtd_parcelas >= 20:
        print("Não aceito")
    else:
        print("Aceito")
    montante = valor_emprestimo * (1 + 0.08) ** qtd_parcelas
    montante = round(montante,2)
    parcela = montante/qtd_parcelas
    parcela = round(parcela,2)
    print(f'O valor total do empréstimo é de {montante} e o valor da parcela é de {parcela}')

emprestimo(idade, valor_emprestimo, salario, qtd_parcelas)