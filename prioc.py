#!/usr/bin/env python3.7
from tarefa import print_relatorio_tarefas


def executa(lista_tarefas):

    tempo_atual = 0
    tarefas_prontas = [tarefa for tarefa in lista_tarefas if tarefa.chegada == tempo_atual]
    tarefas_futuras = [tarefa for tarefa in lista_tarefas if tarefa.chegada > tempo_atual]
    tarefas_terminadas = []
    total_troca_contexto = -1

    while len(tarefas_terminadas) != len(lista_tarefas):
        if len(tarefas_prontas) == 0:
            tempo_atual += 1

            checa_novas_tarefas_prontas(tarefas_futuras, tarefas_prontas, tempo_atual)

        else:
            tarefa_executando = tarefas_prontas[0]

            for t in tarefas_prontas:
                if t.prioridade > tarefa_executando.prioridade:
                    tarefa_executando = t

            tarefas_prontas.remove(tarefa_executando)
            tarefa_executando.tempo_espera += tempo_atual - tarefa_executando.tempo_ultima_interrupcao

            while tarefa_executando.tempo_restante > 0:
                tarefa_executando.tempo_restante -= 1
                tempo_atual += 1

                # tarefa em execução ...

                checa_novas_tarefas_prontas(tarefas_futuras, tarefas_prontas, tempo_atual)

            tarefa_executando.tempo_total_execucao = tempo_atual - tarefa_executando.chegada
            tarefas_terminadas.append(tarefa_executando)
            total_troca_contexto += 1

    print_relatorio_tarefas(lista_tarefas, total_troca_contexto, "Prioridade Cooperativo")


def checa_novas_tarefas_prontas(tarefas_futuras, tarefas_prontas, tempo_atual):
    for tarefa_futura in tarefas_futuras:
        if tarefa_futura.chegada == tempo_atual:
            tarefas_prontas.append(tarefa_futura)

