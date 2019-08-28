#!/usr/bin/env python3.7

import fcfs
import rr
import funcoes
""" import sjf
import srtf
import prioc
import priop
import priod """




arq = open("entrada", "r").read()
matriz = arq.split('\n')
print(matriz)
for i in range(1,len(matriz)):
    matriz[i] = matriz[i].split(" ")

fcfs.executa(matriz)