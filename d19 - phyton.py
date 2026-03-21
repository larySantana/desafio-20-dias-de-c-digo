N = int(input())
print(N)
notas = [100, 50, 20, 10, 5, 2, 1]

for ni in notas:
    valor = int(N / ni)
    N -= valor * ni
    print(f"{valor} nota(s) de R$ {ni},00")
