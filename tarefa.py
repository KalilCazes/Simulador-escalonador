class Tarefa:
    chegada = -1
    tempo_execucao = -1
    prioridade = -1

    tempo_restante = -1
    tempo_total_execucao = 0
    tempo_ultima_interrupcao = 0
    tempo_espera = 0

    prioridade_dinamica = -1


def print_relatorio_tarefas(tarefas, total_troca_contexto, nome_algoritmo):
    tempo_total_espera = 0
    tempo_total_execucao = 0

    for tarefa in tarefas:
        tempo_total_execucao += tarefa.tempo_total_execucao
        tempo_total_espera += tarefa.tempo_espera

    print("|{:<31}|{:^21.1f}|{:^21.1f}|{:^21d}|"
          .format(nome_algoritmo, tempo_total_execucao / len(tarefas), tempo_total_espera / len(tarefas),
                  total_troca_contexto))

