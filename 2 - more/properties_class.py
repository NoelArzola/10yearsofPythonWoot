class Presenter():
	def __init__(self, name):
		# Constructor
		self.name = name #Property

	@property
	def name(self):
		print('Retrieving name...')
		return self.__name
	@name.setter
	def name(self, value):
		# cool validation here
		print('Validating name...')
		self.__name = value

presenter = Presenter('Noel')
presenter.name = 'Noel Arzola'
print(presenter.name)