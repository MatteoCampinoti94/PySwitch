class switch:
	def __init__(self, key=None, cases={}, default=None):
		if type(cases) != dict:
			raise TypeError
		elif type(default) not in (str, type(None)):
			raise TypeError
		elif any(type(v) != str for v in cases.values()):
			raise TypeError

		self._key = key
		self._cases = cases
		self._default = default

	def run(self):
		if not self._cases and not self._default:
			raise KeyError

		if self._key in self._cases.keys():
				exec(self._cases[self._key])
		elif self._default:
				exec(self._default)
		else:
			raise KeyError

	def key(self, key, run=True):
		self._key = key
		if run:
			self.run()

	def case(self, key, case, run=False):
		if type(case) != str:
			raise TypeError
		self._cases[key] = case
		if run:
			self.run()

	def default(self, default, run=False):
		if type(default) != str:
			raise TypeError
		self._default = default
		if run:
			self.run()

s = switch()
s.case(None, 'print("NoneType as key")')
s.default('print(f"Used key: {self._key}")')
key = input()
s.key(key)
