class Product(object):
	def __init__(self, name, description, ID, price):
		#assign the different values to a self variable
		self.product_name = name
		self.product_description = description
		self.product_ID = ID
		self.product_price = price

	#if these functions are called without any parameter, they simply return the value already in place
	#if they're called with a parameter, they modify the value and return it
	def name(self, name = None):
		if name != None:
			self.product_name = name
		return self.product_name

	def description(self, description = None):
		if description != None:
			self.product_description = description
		return self.product_description

	def ID(self):
		#ID cannot be modified, so you can only check its value
		return self.product_ID
		
	def price(self, price = None):
		if price != None:
			self.product_price = price
		return self.product_price