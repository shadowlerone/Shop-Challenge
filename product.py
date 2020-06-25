import warnings as w
from entity import Entity
class Product(Entity):
	def __init__(self, name = '', price = 0.0, ID = None):
		if price < 0:
			raise ValueError("Price is negative.")
		if name == None or name == '':
			w.warn('Name is empty')
		if price == 0.0 or price == None:
			w.warn(f'Price is {price}.')
		self.name = name
		self.price = price
		if ID == None:
			w.warn("Generating ID")
			self.ID = self.generate_ID()
		else:
			self.ID = ID