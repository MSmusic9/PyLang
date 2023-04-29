import os
os.system("pip install numba && pip install termcolor")
from numba import njit
from termcolor import colored as clr


class CompilerLang:
	def __init__(self,filepath):
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
                self.file.close()
		os.system("gcc main.c -o main")
		os.remove("main.c")


class InterplerLang(CompilerLang):
        def __new__(self,filepath):
                self.file = open(self.filepath)
        def run(self):
                self.file.close()
        def execOn(self,linecom,execline):
                if self.line == linecom:
                        exec(execline)
