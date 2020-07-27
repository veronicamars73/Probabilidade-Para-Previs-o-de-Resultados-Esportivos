import pandas as pd
import numpy as np


# Abrindo o arquivo com os resultados
"""
o arquivo está formatado da seguinte forma:
gols marcados, gols sofridos
ou seja, se o ajax ganhou fazendo 3 gols e sofrendo 1 - em casa ou fora de casa -
nosso arquivo registrará a rodada como:
3,1
"""
arquivo = open("resultados.txt", "r")

# Inicializando nossa lista de resultados
resultado_rodadas = []

# O for vai percorrer cada linha do arquivo
for linha in arquivo:
    """
    A próxima linha irá adicionar os resultados na nossa lista,
    dentro dos parênteses temos uma 'list comprehension' que
    realiza o mesmo que o seguinte trecho de código:
    list = []
    for x in l.split(","):
        list.append(int(x))
    results.append(list)
    """
    resultado_rodadas.append([int(x) for x in linha.split(",")])

# Agora iremos trabalhar com os dados que obtemos rodada a rodada
# Inicializaremos nossas listas de gols marcados e gols sofridos
gols_marcados = []
gols_sofridos = []

# Também calcularemos nosso número de acertos de resultados
acertos_rodada = 0
acertos_gols_marcados = 0
acertos_gols_sofridos = 0