import pandas as pd

# Abrindo o arquivo com os resultados
arquivo = open("resultados.txt", "r")

# Inicializando nossa lista de resultados
results = []

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
    results.append([int(x) for x in l.split(",")])