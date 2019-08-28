#!/usr/bin/env python3.7

import funcoes


def executa(matriz):
    #inicio, fim, prioridade = []
    processos = []
    for i in range(int(matriz[0])):
        fila(matriz, processos)
    print(processos)

def fila(matriz, processos, i):
    processos.append({})
    processos[i]["inicio"] = funcoes.get_inicio(matriz, i)
    processos[i]["fim"] = funcoes.get_fim(matriz, i)
    processos[i]["prioridade"] = funcoes.get_prioridade(matriz, i)

    processos.sort(key=lambda processo: processo["inicio"])

""" def foo (matriz):
    programasnafila = 0
    tempoatual = 0
    processos = []
    while programasnafila < int(matriz[0]):
        for i in range(int[matriz[0]]):
            if(funcoes.get_inicio(matriz, i) == tempoatual):
                fila(matriz, processos, i)
                programasnafila += 1
        tempoatual += 1 """
