#Calculadora
numero1 = 0
numero2 = 0
resultado = 0
operacao = ' '

while True:
    numero1 = int(input('Digite o primeiro número: '))
    operacao = input('Digite a operação : ')
    numero2 = int(input('Digite o segundo número : '))
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    else:
        resultado = 'Operação inválida'

    print(str(numero1) + ' ' + str(operacao) + ' ' + str(numero2) + ' = ' + str(resultado))
