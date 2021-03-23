# -*- coding: utf-8 -*-
from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Is adult? ','adult'],
		# ['Does the chest hurt? ','chest'],
		['Does the head hurt? ','head'],
		['Do any member fall asleep? ','asleep'],
	]

	def texto(self):
		print('self', self)
		if(len(self.level[0]) > 0):
			string = self.level[0]
			del self.level[0]
			print('string', string)
			return string
		else: return ['', '']

