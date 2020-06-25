from entity import Entity
from product import Product
class Cart(Entity):
	def __init__(self):
		self.content = {}
	
	def total_price(self) -> float:
		out = 0
		for key, value in self.content:
			out += key*value.price
		return out
	
	def subtotal(self, product):
		if type(product) is not Product:
			raise TypeError("product is not Product Object.")
		return self.content[product] * 