def get(arq, alg, dado):
    return arq[dado+1][alg]

def get_alg(arq, alg):
    dados = []
    for i in range(1,len(arq)):
        dados.append(arq[i][alg])
    return dados

def get_inicio(arq, alg):
    return get(arq, alg, 0)

def get_fim(arq,alg):
    return get(arq, alg, 1)

def get_prioridade(arq, alg):
    return get(arq, alg, 2)
