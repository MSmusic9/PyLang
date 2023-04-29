import os
from numba import njit
from termcolor import colored as clr


class CompileLang:
	def __init__(self):
		self.file = open(self.filepath)
		self.compiler = open("main.c","a")
	def onEveryLine(self,line:str,command):
		self.line = line
		for self.line in self.file.readlines():
			command()
	def interrupt(self,i1:int,i2:int):
		return self.line[i1:i2]
	def execOn(self,linecom:str,execline:str):
		if self.line == linecom:
			self.compiler.write(execline)
	def showMessage(self,deco:str,color:str,effect:str):
		print(clr(deco,color,attrs=[effect]))
	def run(self):
		self.compiler.close()
		os.system("gcc main.c -o main")
		os.remove("main.c")
