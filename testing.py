from cart import Cart
from client import Client
from product import Product
from shop import Shop

def test_product_creation():
	name = 'banana'
	price = 15.2
	banana = Product(name = name, price = price)
	assert banana.name == 'banana', f"banana.name should be {name}. Got {banana.name}"
	assert banana.price == price, f"banana.price should be {price}. Got {banana.price}"
	print("Success!")
	return True

def test_cart_content():
	c = Cart()
	assert c.content == {}, "Cart Content at initialization should be empty Dict"
	try:
		c.remove(Product(name = 'banana', price = 12.5), 1)
	except ValueError:
		print("Successfully handled remove error.")
	else:
		print("Didn't handle remove Product that doesn't exist.")
		return

def test_shop_ID_conflict():
	shop = Shop()
	banana = Product(name = 'banana', price = 12.5)
	apple = Product(name = 'apple', price = 12.5)
	shop.add_product(banana, 10, ID = '12345')
	try:
		shop.add_product(apple, 10, ID = '12345')
	except ValueError:
		print("Success!")
	else:
		print("ID conflict not handled properly")
		return False



if __name__ == "__main__":
	test_product_creation()
	test_cart_content()