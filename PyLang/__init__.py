import os
from numba import njit
from termcolor import colored as clr


class CompileLang:
	def __init__(self,langname:str,filepath,langtype,compilepath):
		self.langtype = langtype
		self.compilepath = compilepath
		self.filepath = filepath
		self.file = open(self.filepath)
		self.langname = langname
	def onEveryLine(self,line:str,command):
		self.line = line
		for self.line in self.file.readlines():
			command()
	def interrupt(self,i1:int,i2:int):
		return self.line[i1:i2]
	def execOn(self,linecom:str,execline:str):
		if self.line == linecom:
			self.compiler.write(execline)
	def showMessage(self,deco:str,color:str,effect:str,msgtype:str):
		if msgtype == 'info':
			print(clr(deco,color,attrs=[effect]))
		if msgtype == 'error':
			print(clr(deco,color,attrs=[effect]))
			exit(0)
	def run(self,command):
		self.compiler = open(
			f"PyLang/run/{self.compilepath}.{self.langtype}",
			"w"
		)
		self.compiler = open(
			f"PyLang/run/{self.compilepath}.{self.langtype}",
			"a"
		)
		self.compiler.close()
		os.system(
			command.format(
				lang_name
				=
				"PyLang/run/"
				+
				self.compilepath
				+
				"."
				+
				self.langtype
			)
		)
		os.remove(
			f"PyLang/run/{self.compilepath}.{self.langtype}"
		)
	def writeJSONfile(self,version,pattern,path,license_,author,description):
		f = open(f"{path}{self.filepath}.json","w")
		f.write("{"+"""
  "language_name": "{lang}",
  "version": "{ver}",
	"description": "{des}",
  "compiler": "GCC",
  "lisense": "{lis}",
  "author": "{auth}",
  "pattern": "{pat}"
""".format(des=description,lang=self.langname,ver=version,lis=license_,auth=author,pat=pattern)+"}"
		)
		f.close()
