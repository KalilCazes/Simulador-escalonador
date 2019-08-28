#!/usr/bin/env python3.7

import funcoes


def executa(n_processos, lista_processos):

    tempo_atual = 0;
    processos_prontos = []
    processo_executando = -1

    
    for p in range(lista_processos):
        if()
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
