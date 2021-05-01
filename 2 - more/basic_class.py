class Presenter():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(self.name)

presenter = Presenter('Noel')
presenter.name = 'Noel Arzola'
presenter.say_hello()