# PyLang
A small framework to make languages using Python.

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



# Classes, methods and examples
And now, we can start.

### CompilerLang(filepath: str)
The Python class that builds-up your file and compiler.
#### run()
Use it at the end of program. It runs compiler.
#### onEveryLine(var: str,command)
That loop which do 'command' every iteration.
#### interrupt(from: int,to: int)
Line-iterator trimming.
####

### InterplerLang() # Extends CompilerLang
The Python class that builds-up your file, but <b>NOT</b>
compiler.
#### 
