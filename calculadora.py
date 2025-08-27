try:
    n1 = float(input('Digite o primeiro número: '))
    operacao = input('Digite a operação (+, -, *, /): ')
    n2 = float(input('Digite o segundo número: '))

    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            print('Erro: Divisão por zero!')
            resultado = None
        else:
            resultado = n1 / n2
    else:
        print('Operação inválida!')
        resultado = None

    if resultado is not None:
        # Verifica o tipo do resultado
        tipe = type(resultado)
        if tipe == float:
            print(f'Resultado: {resultado:.3f}')  # Exibe com 3 casas decimais
        elif tipe == int:
            print(f'Resultado: {resultado:.1f}')  # Exibe com 1 casa decimal
        else:
            print(f'Resultado: {resultado}')  # Exibe o resultado sem formatação específica
except ValueError:
    print('Erro: Digite apenas números válidos!')