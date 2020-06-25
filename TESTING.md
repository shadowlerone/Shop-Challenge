# Testing

Add these to the end of your file.
Alternatively, download `/testing/tests.py` 
## Testing Product

### Basic `Product` creation
```py
from product import Product
name = 'banana'
price = 15.2
banana = Product(name = name, price = price)
assert banana.name == 'banana', f"banana.name should be {name}. Got {banana.name}"
assert banana.price == price, f"banana.price should be {price}. Got {banana.price}"
print("Success!")
```


## Testing Cart
### Cart Contents
```py
from cart import Cart
from product import Product
c = Cart()
assert c.content == {}, "Cart Content at initialization should be empty Dict"
try:
	c.remove(Product(name = 'banana', price = 12.5), 1)
except ValueError:
	print("Successfully handled remove error.")
else:
	print("Didn't handle remove Product that doesn't exist.")
```


## Testing Shop
### Product ID conflicts
```py
from product import Product
from shop import Shop
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
```
### Client ID conflicts
```py
from client import Client
from shop import Shop

shop = Shop()
shop.add_client()
try:
	shop.add_client()
except ValueError:
	print('Success!')
else:
	print("ID conflict not handled properly")
```