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
            tarefa_executando = tarefas_prontas.pop(0)
            tarefa_executando.tempo_espera += tempo_atual - tarefa_executando.tempo_ultima_interrupcao
            quantum_restante = 2

            while tarefa_executando.tempo_restante > 0 and quantum_restante > 0:
                tarefa_executando.tempo_restante -= 1
                tempo_atual += 1
                quantum_restante -= 1

                # tarefa em execução ...

                checa_novas_tarefas_prontas(tarefas_futuras, tarefas_prontas, tempo_atual)

            total_troca_contexto += 1

            if tarefa_executando.tempo_restante > 0:
                tarefa_executando.tempo_ultima_interrupcao = tempo_atual
                tarefas_prontas.append(tarefa_executando)

            else:
                tarefa_executando.tempo_total_execucao = tempo_atual - tarefa_executando.chegada
                tarefas_terminadas.append(tarefa_executando)

    print_relatorio_tarefas(lista_tarefas, total_troca_contexto, "Round-Robin")


def checa_novas_tarefas_prontas(tarefas_futuras, tarefas_prontas, tempo_atual):
    for tarefa_futura in tarefas_futuras:
        if tarefa_futura.chegada == tempo_atual:
            tarefas_prontas.append(tarefa_futura)
