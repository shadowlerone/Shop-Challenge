# Shop Challenge

Welcome to the shop challenge.
Your goal is to make a shopping system.

## Requirements

You will need to make the following classes:

-   `Product`
    : Defines a product sold by the shop
-   `Cart`
    : Defines a shopping cart
-   `Shop`
    : Defines the shop
-   `Client`
    : Defines someone shopping in your store

### Product

Here are the methods and attributes your `Product` class should contain:

-   `#name`
    : The Name of the product.  
    -> `String`
-   `#description`
    : A description of the product.  
    -> `String`
-   `#ID`
    : A Unique ID that for each `Product` item.  
    -> `String` or `Integer`. Your choice.
-   `#price`
    : How much the product costs.  
    -> `Float` or `Double`

### Cart

-   `#content`
    : What is in the cart.  
    -> `{Product => Quantity(Integer)}`

-   `#total_price()`
    : The total checkout price of the cart.  
    -> `Float` or `Double`

-   `#subtotal(Product)`
    : The calculated price of the `Product` parameter.  
    -> `Float` or `Double`
-   `#add(Product, Quantity)`
    : Adds `Quantity` of `Product` to the `Cart`.  
    -> `nil`
-   `#remove(Product, Quantity)`
    : Removes `Quantity` of `Product` from the `Cart`.
    -> `True` if succesful.
    -> `ValueError` if cannot remove product. (ei: Not enough `Product` in `Cart`)
-   `#empty`
    : Clears the cart  
    -> `True`

### Client

Here are the methods and attributes your `Client` class should contain:

-   `#name`
    : Client Name.  
    -> `String`
-   `#ID`
    : Unique ID.  
    -> `String`
-   `#wallet`
    : The Money the client has.  
    -> `Float` or `Double`
-   `#cart`
    : Their shopping cart.  
    -> `Cart`
-   `#checkout()`
    : Buys everything in their cart if they have enough money for it.  
    -> `True` or `ValueError`

### Shop

Here are the methods and attributes your `Shop` class should contain:

-   `#stock`
    : The Shop's stock.  
    -> `{Product => Quantity(Integer)}`
-   `#clients`
    : The people in the shop.  
    -> `{CliendID => Client}`
-   `#add_client(Name, ID = None)`
    : Creates and adds a `Client` to the shop.  
    If no `ID` is provided, generate one.  
    If provided `ID` is already used by another `Client`, throw `ValueError`.  
    -> `ID` (`String` or `Integer`)
-   `#client_join(Client)`
    : Adds an existing `Client` to the shop.  
     If `Client`'s `ID` is already used in the shop, throw `ValueError`.  
     -> `ID` (`String` or `Integer`)

-   `#add_to_cart(ClientID, Product, Quantity)`
    : Adds `Quantity` of `Product` to the `Client`'s `Cart`.  
    -> `True` on success.  
    -> `ValueError` if `Shop` doesn't have enough `Product` in stock.
