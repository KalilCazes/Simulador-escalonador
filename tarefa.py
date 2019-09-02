class Tarefa:
    chegada = -1
    tempo_execucao = -1
    prioridade = -1

    tempo_restante = -1
    tempo_total_execucao = 0
    tempo_ultima_interrupcao = 0
    tempo_espera = 0

    prioridade_dinamica = -1

    def __str__(self):
        return "tarefa [ chegada: " + str(self.chegada) \
               + ", tempo de execução: " + str(self.tempo_execucao) \
               + ", prioridade: " + str(self.prioridade) \
               + ", tempo restante: " + str(self.tempo_restante) \
               + ", tempo de espera: " + str(self.tempo_espera) \
               + ", tempo total de execução: " + str(self.tempo_total_execucao) + "]\n "


def print_relatorio_tarefas(tarefas, nome_algoritmo):
    tempo_total_espera = 0
    tempo_total_execucao = 0
    print("\n=====  " + nome_algoritmo + "  =====\n")
    for tarefa in tarefas:
        print(tarefa)
        tempo_total_execucao += tarefa.tempo_total_execucao
        tempo_total_espera += tarefa.tempo_espera
    print("- tempo medio de execução = " + str(tempo_total_execucao / len(tarefas)))
    print("- tempo medio de espera = " + str(tempo_total_espera / len(tarefas)))
    print("\n======================================\n")
