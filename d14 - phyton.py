A, B, C = input().split()

A = int(A)

B = int(B)

C = int(C)

maior1 = (A + B + abs (A - B)) /2
    
maior = int((maior1 + C + abs (maior1 - C)) /2)

print (f'{maior} eh o maior')