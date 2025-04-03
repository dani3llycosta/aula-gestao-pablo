numero = int(input('digite um número: '))

def dobrar_numero(numero):
    print(numero * 2)

def impar_ou_par(numero):
    print("par" if numero % 2 == 0 else "ímpar")

def calcula_desconto(preco_produto):
    desconto = preco_produto * 0.05
    return preco_produto - desconto

def aplicar_desconto(desconto):
    print(f'o preço com desconto é R${desconto}')


preco_produto = float(input("preço com 5 porcento de desconto"))
desconto = calcula_desconto(preco_produto)
aplicar_desconto(desconto)