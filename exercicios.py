numero = int(input('digite um número: '))

def dobrar_numero(numero):
    print(numero * 2)

def impar_ou_par(numero):
    print("par" if numero % 2 == 0 else "ímpar")

def aplicar_desconto(preco_produto):
    desconto = preco_produto * 0.05
    preco_final = preco_produto - desconto
    print(f'preço com 5 porcento de desconto: {preco_final}')

aplicar_desconto(numero)