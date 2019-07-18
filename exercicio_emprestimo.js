let idade = prompt('qual a sua idade');

function emprestimo(idade, valorEmprestimo, salario, qtdParcelas){
    if(idade < 22 || idade > 55|| valorEmprestimo < 1000 || valorEmprestimo > salario * 15 || qtdParcelas < 3 || qtdParcelas > 20){
        console.log('Não aceito');
    }
    else{
        console.log('Aceito');
        let montante;
        montante = valorEmprestimo * (1 + 0.08) ** qtdParcelas;
        montante = montante.toFixed(2);
        let parcela = montante/qtdParcelas;
        parcela = parcela.toFixed(2);
        console.log(`O valor total do empréstimo é de ${montante} e o valor da parcela é de ${parcela}`);
    }
}