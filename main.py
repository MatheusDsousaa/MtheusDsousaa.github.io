def contarSubmatrizes(mat):
    linhas, colunas = len(mat), len(mat[0])
    alturas = [0] * colunas
    total_submatrizes = 0
    
    for i in range(linhas):
       
        for j in range(colunas):
            if mat[i][j] == 1:
                alturas[j] += 1
            else:
                alturas[j] = 0
        
        total_submatrizes += contarSubmatrizesNaLinha(alturas)
    
    return total_submatrizes

def contarSubmatrizesNaLinha(alturas):
    pilha = []
    submatrizes = 0
    soma_submatrizes = 0
    
    for i in range(len(alturas)):
        contagem = 0
        while pilha and pilha[-1][0] >= alturas[i]:
            altura, qtd = pilha.pop()
            soma_submatrizes -= altura * qtd
            contagem += qtd
        
        soma_submatrizes += alturas[i] * (contagem + 1)
        submatrizes += soma_submatrizes
        pilha.append((alturas[i], contagem + 1))
    
    return submatrizes


matriz1 = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]

matriz2 = [
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 0]
]


resultado1 = contarSubmatrizes(matriz1)
resultado2 = contarSubmatrizes(matriz2)


print(f"Total de submatrizes com todos 1's na primeira matriz: {resultado1}")
print(f"Total de submatrizes com todos 1's na segunda matriz: {resultado2}")
