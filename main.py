# -*- coding: utf-8 -*-
from classDiagnostico import *
from classPerguntas import *

#Inferência
se = Diagnostico()
pergunta = Pergunta()
print('================')
print('HEATH DIAGNOSTIC')
print('================')

while se.probabilidade() != 100:
	string = pergunta.texto()
	se.pergunta(string[0],string[1])
	print('---')
	# print('Probability: %d' %(se.probabilidade()), "%")
	print(se.resultado)
	print('---')
	if se.probabilidade() == 100:
		print('===')
		print('The patient has: ',se.resultado[0])
		print('===')
		