# -*- coding: utf-8 -*-
class Diagnostico():
	# metodo construtor
	def __init__(self):
		self.resultado = [
			'asma',
			'pneumonia',
			'tuberculose',
			'enxaqueca',
			'acidente_vascular_cerebral',
		]
		self.pessoa = []
		self.db = []
		# abre o arquivo db.txt em modo leitura e passa os dados para
		# uma lista de listas de str
		arquivo = open('db.py','r')
		for linha in arquivo:
			if linha[0] != '#' and linha[len(linha) - 1] == '\n':
				linha = linha.replace("\n", "")
				(self.db).append(linha.split('-'))
		arquivo.close()

	# imprime a quantidade de possibilidades cadastradas
	def tamanho(self):
		print(len(self.resultado))

	# imprime a probabilidade do diagnótico
	def probabilidade(self):
		return (int(100/len(self.resultado)))


	# verifica se diagnóstico pensado tem a caracteristica passada por parametro
	def busca(self, familiar, caract):	
		for i in range(len(self.db)):
			if familiar == self.db[i][1]:
				if self.db[i][0] == caract:
					return True
		return False				

	# remove os diagnósticos que não possuem o atributo passado por parametro
	def excluiquemnaoe(self, atributo):
		lista = []
		count = 0
		for i in range(len(self.resultado)):
			if not self.busca(self.resultado[i], atributo):
				lista.append(self.resultado[i])
				count = count + 1
		for i in range(count):
			self.resultado.remove(lista[i])
	
	# remove os diagnosticos que possuem o atributo passado por parametro
	def excluiqueme(self, atributo):
		lista = []
		count = 0
		for i in range(len(self.resultado)):
			if self.busca(self.resultado[i], atributo):
				lista.append(self.resultado[i])
				count = count + 1
		for i in range(count):
			self.resultado.remove(lista[i])
		
	def pergunta(self,pergunta,caract):
		# print(self,pergunta,caract)
		resp = input(pergunta)
		if resp == 's' or resp == 'S' or resp == 'yes' or resp == 1:
			self.excluiquemnaoe(caract)
		elif resp == 'n' or resp == 'N' or resp == 'no' or resp == 0:
			self.excluiqueme(caract)