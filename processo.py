class Processo:
    inicio = -1;
    fim = -1;
    prioridade = -1;

    def __str__(self):
        return "[ inicio: " + self.inicio + ", fim: " + self.fim + ", prioridade: " + self.prioridade + "]\n"
