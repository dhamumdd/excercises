from cmd import Cmd

class MyExcercise(Cmd):
	prompt = '>'
	dict_test = {}	

	def do_ADD(self, s):
		print(s)
		values = s.split()

		if values[1] in self.dict_test:
			print("ERROR, value already exists")
		else:
			self.dict_test[values[1]] = values[0]
			print("Added")
	

	def do_REMOVE(self, s):
		key = s.split()[0]

		if key in self.dict_test.values():
			del self.dict_test[s.split()[1]]
			print("Removed")
		else:
			print("ERROR, value does not exist")

	def do_KEYS(self, s):
		i=0
		if len(self.dict_test.values()) == 0:
			print("empty set")

		for value in self.dict_test.values():
			i = i+1
			print(str(i) +'){}'.format(value))

	def do_MEMBERS(self, s):
		try:
			for k, v in self.dict_test.items():
				if s == v:
					print(k)
		except ValueError as error:
			print("ERROR, key does on exist")
	
	def do_REMOVEALL(self, s):
		try:
			temp_dict = {}
			for k, v in self.dict_test.items():
				if s != v:
					temp_dict[v] = k
			self.dict_test = temp_dict
			print("Removed")
			temp_dict = {}
		except ValueError as error:
			print("ERROR, key does on exist")

	def do_CLEAR(self, s):
		self.dict_test = {}
		print("Cleared")

	def do_KEYEXISTS(self, s):
		if s in self.dict_test.values():
			print("true")
		else:
			print("false")

	def do_VALUEEXISTS(self, s):
		if s in self.dict_test:
			print("true")
		else:
			print("false")

	def do_ALLMEMBERS(self, s):
		for value in self.dict_test:
			print(value)
	
	def do_ITEMS(self, s):
		i = 0
		for k, v in self.dict_test.items():
			i = i + 1
			print(str(i) + ')'+ v +':'+k)

if __name__ == '__main__':
	MyExcercise().cmdloop()