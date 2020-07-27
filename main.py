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

# Também calcularemos nosso número de acertos de resultados para controlarmos quão boa é nossa previsão
acertos_rodada = 0
acertos_gols_marcados = 0
acertos_gols_sofridos = 0

"""
Percorreremos nossa lista de resultados por rodada e calcularemos
o valor esperado de gols marcados e sofridos para cada rodada faremos
uma previsão com esses valores e depois iremos conferir se esses valores 
correspondem ao resultado que ocorreu na rodada
"""
for rodada in range(len(resultado_rodadas)):
    gols_marcados.append(resultado_rodadas[rodada][0])
    gols_sofridos.append(resultado_rodadas[rodada][1])

    # Agora iremos obter a frequência do número de gols registrados até o momento
    num_gols, freq_num_gols = np.unique(gols_marcados, return_counts=True)
    # Por questão de organização transformaremos nossos valores em um dicionário do tipo 'gols':frequencia
    dic_gols_marcados = dict(zip(num_gols, freq_num_gols))

    # Faremos o mesmo com os gols sofridos
    num_gols, freq_num_gols = np.unique(gols_sofridos, return_counts=True)
    # Por questão de organização transformaremos nossos valores em um dicionário do tipo 'gols':frequencia
    dic_gols_sofridos = dict(zip(num_gols, freq_num_gols))

    # Agora calcularemos a esperança dos gols 
    esperanca_marcados=0
    for gol in dic_gols_marcados.keys():
        esperanca_marcados += gol*(dic_gols_marcados[gol]/len(gols_marcados))

    esperanca_sofridos=0 
    for gol in dic_gols_sofridos:
        esperanca_sofridos += gol*(dic_gols_sofridos[gol]/len(gols_sofridos))

    # Depois de calcular nossas esperanças vamos imprimí-las e compará-las com os resultados reais

    # As próximas linhas arredondam nosso resultado para um valor inteiro
    esperanca_marcados = int(np.around(esperanca_marcados))
    esperanca_sofridos = int(np.around(esperanca_sofridos))

    # Se estivermos na última rodada já realizamos nossa previsão
    # na iteração anterior então devemos não devemos imprimir nossa esperança
    if (rodada+1 == len(resultado_rodadas)):
        break
    """
    Agora imprimiremos nosso valor esperado para a rodada que virá
    como listas têm posição inicial no número 0 temos que adicionar
    1 ao valor da rodada para conseguirmos a rodada que está sendo lida atualmente,
    ou seja, temos que adicionar 2 ao numero da `rodada`
    para conseguirmos o valor da proxima rodada.
    """
    print(f'Na {rodada+2} rodada esperamos um resultado de Ajax  {esperanca_marcados} x {esperanca_sofridos} adversário')
    print(f'Na {rodada+2} rodada obtemos um resultado de Ajax  {resultado_rodadas[rodada+1][0]} x {resultado_rodadas[rodada+1][1]} adversário')
    
    # Veremos se acertamos os resultados
    if(esperanca_marcados==resultado_rodadas[rodada+1][0] and esperanca_sofridos==resultado_rodadas[rodada+1][1]):
        acertos_rodada += 1
    if(esperanca_marcados==resultado_rodadas[rodada+1][0]):
        acertos_gols_marcados += 1
    if(esperanca_sofridos==resultado_rodadas[rodada+1][1]):
        acertos_gols_sofridos += 1