#!/usr/bin/env python3

from tarefa import Tarefa
import fcfs
import rr
import sjf
import srtf
import prioc
import priop
import priod


def main():
    print_header_tabela()

    lista_tarefas = tarefas_de_entrada()
    fcfs.executa(lista_tarefas)
    print_linha_tabela()

    lista_tarefas = tarefas_de_entrada()
    rr.executa(lista_tarefas)
    print_linha_tabela()

    lista_tarefas = tarefas_de_entrada()
    sjf.executa(lista_tarefas)
    print_linha_tabela()

    lista_tarefas = tarefas_de_entrada()
    srtf.executa(lista_tarefas)
    print_linha_tabela()

    lista_tarefas = tarefas_de_entrada()
    prioc.executa(lista_tarefas)
    print_linha_tabela()

    lista_tarefas = tarefas_de_entrada()
    priop.executa(lista_tarefas)
    print_linha_tabela()

    lista_tarefas = tarefas_de_entrada()
    priod.executa(lista_tarefas)

    print_footer_tabela()


def print_header_tabela():
    print("=" * 99)
    print("|{:^31}|{:^21}|{:^21}|{:^21}|"
          .format("Algoritmo", "Tempo total medio", "Tempo de espera medio", "Trocas de contexto"))
    print("=" * 99)


def print_linha_tabela():
    print("." * 99)


def print_footer_tabela():
    print("=" * 99)


def tarefas_de_entrada():
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
        t.tempo_ultima_interrupcao = t.chegada
        t.prioridade_dinamica = t.prioridade
        lista_tarefas.append(t)

    return lista_tarefas


if __name__ == "__main__":
    main()
