# -*- coding: utf-8 -*-
from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		# ['Is adult?','adult'],
		['Does the chest hurt? ','chest'],
		['Does the head hurt? ','head'],
		['Do any member fall asleep? ','asleep'],
		# ['Hurt on head? ','head'],
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
