import re


class InterpretLang:
	def __init__(self, **tokens):
		self.init_tokens(tokens)

	def init_tokens(self, **tokens):
		self.tokens = tokens

	def tokenize(self, code: str, err = lambda l: pass):
		toks = []
		pos = 0
		nowchr = lambda: code[pos, pos]
		futchr = lambda: code[pos + 1, pos + 1]
		for key in self.tokens.items():
			if re.match(nowchr(), self.tokens[key]):
				text = nowchr()
				while re.match(futchr(), self.tokens[key]):
					pos += 1
					text += nowchr()
				toks.append([key, text])
			else:
				err(nowchr())
				return
		return toks

	def construct(toks: list, fn = lambda: pass):
		
