#!/usr/bin/python

class User(object):
	def __init__(self, name):
		self.name = name

def set_password(self, password):
    self.password = password

print 'Classe original:', dir(User)

User.set_password = set_password
print 'Classe modificada: ', dir(User)
user = User('guest')
user.set_password('guest')
print 'Objeto:',dir(user)
print 'Senha:', user.password		
