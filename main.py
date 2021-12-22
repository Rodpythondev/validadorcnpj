from cnpj import valida, gera, formata

cnpj1 = '04.252.011/0001-10'

if valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')

for i in range(100):
    novo_cnpj = gera()
    formatado = formata(novo_cnpj)
    print(formatado)
