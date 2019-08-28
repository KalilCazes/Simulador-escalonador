#!/usr/bin/env python3.7

from processo import Processo
import fcfs

def main():
    arq = open("entrada", "r").read()
    entrada = arq.split('\n')

    n_processos = int(entrada[0])
    lista_inicio = entrada[1].split(" ")
    lista_fim = entrada[2].split(" ")
    lista_prioridade = entrada[3].split(" ")

    lista_processos = []
    for i in range(n_processos):
        p = Processo()
        p.inicio = lista_inicio[i]
        p.fim = lista_fim[i]
        p.prioridade = lista_prioridade[i]
        lista_processos.append(p)

    fcfs.executa(n_processos, lista_processos)



if __name__ == "__main__":
    main()
