[![PyLang](https://github.com/MSmusic9/PyLang/actions/workflows/python-publish.yml/badge.svg?branch=main&event=workflow_run)](https://github.com/MSmusic9/PyLang/actions/workflows/python-publish.yml)


# PyLang
PyLang is a small framework to make languages using Python.

### How to use
To start using PyLang, first choose, 
how you do want to make language: compile it with C or 
interpler it with Python. If you prefer compile it,
scroll down to paragraph `CompileLang`, else scroll
down to `InterplerLang`.



# A bit theory: How PyLang creates your language
PyLang works very simply: it just creates a loop, 
and with each iteration, it assigns "i" the value of 
each line in your file.  Then, it checks each line for 
a match with the correct one according to the syntax of 
your language, which is done by the `execOn` and `interrupt` 
methods of both classes.



# Classes and methods
And now, we can start.

### CompilerLang(filepath: str)
The Python class that builds-up your file and compiler.
#### run()
Use it at the end of program. It runs compiler.
#### onEveryLine(var: str,command)
That loop which do 'command' every iteration.
#### interrupt(from: int,to: int)
Line-iterator trimming.
#### execOn(compareline: str,execline: str)
If line-iterator equals 'compareline', it exectues 
'execline'.
#### showMessage(msg: str,color: str,effect: str)
Prints colored line with some 'effect' like bold.

### InterplerLang(filepath: str) # Extends CompilerLang
The Python class that builds-up your file, but <b>NOT</b>
compiler.


# Examples
Example: Math language(only a bit of code, after i'll upload
completed language):
```Python
# Import class
from PyLang import InterplerLang as inter

# Build-up the file
lang = inter("main.math")
lines = ""

# Parse function
def parse():
  # print line on concident of lines of file and 'print whattoprint'
  lang.execOn("print {l}\n".format(l=lang.interrupt(6,-3)),"print({l})".format(l=lang.interrupt(6,-3)))
  # I'm lazy to continue the code

lang.onEveryLine(lines,parse)
lang.run()
```
