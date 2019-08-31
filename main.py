#!/usr/bin/env python3

from tarefa import Tarefa
import fcfs


def main():
    arq = open("entrada", "r").read()
    entrada = arq.split('\n')

    n_tarefas = int(entrada[0])
    lista_chegada = entrada[1].split(" ")
    lista_execucao = entrada[2].split(" ")
    lista_prioridade = entrada[3].split(" ")

    lista_tarefas = []
    for i in range(n_tarefas):
        t = Tarefa()
        t.chegada = int(lista_chegada[i])
        t.tempo_execucao = int(lista_execucao[i])
        t.prioridade = int(lista_prioridade[i])
        t.tempo_restante = t.tempo_execucao
        lista_tarefas.append(t)

    fcfs.executa(lista_tarefas)

if __name__ == "__main__":
    main()
