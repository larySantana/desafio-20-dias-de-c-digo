cod, npecas, valorpecas = input().split()

cod = int(cod)
npecas = int(npecas)
valorpecas = float(valorpecas)

cod2, npecas2, valorpecas2 = input().split()

cod2 = int(cod2)
npecas2 = int(npecas2)
valorpecas2 = float(valorpecas2)

total = (npecas * valorpecas) + (npecas2 * valorpecas2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
