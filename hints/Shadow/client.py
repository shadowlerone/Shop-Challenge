class Client(object):
	def __init__(self, name, ID=None, wallet=0.0):
		self.name = name
		self.wallet = wallet
		self.cart = Cart()

	def checkout(self):
		if self.cart.total() > self.wallet:
			raise AttributeError

		self.cart.empty()
		return True


class Cart(object):

	def empty(self):
		pass
	def total(self):
		pass