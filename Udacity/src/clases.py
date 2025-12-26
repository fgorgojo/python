class Example:
    def a_normal_method(self, a, b):
        print(self, a, b)
    @classmethod
    def a_class_method(cls, a, b):
        print(cls, a, b)
    @staticmethod
    def a_static_method(a, b):
        print(a, b)

ex = Example()

ex.a_normal_method(1, 2)      # Example instance, 1, 2
#ex.a_static_method(7, 8)       # 7, 8
#Example.a_class_method(3, 4)   # Example class, 3, 4
Example.a_static_method(5, 6)  # 5, 6                   

# CLASSES WITH CLASSMETHOD FACTORY
class Customer:
    def __init__(self, first_name, last_name, plan_tier='free', plan_cost=0):
        self.name = f"{first_name} {last_name}"
        self.plan_tier = plan_tier
        self.plan_cost = plan_cost

    @classmethod
    def premium(cls, first_name, last_name):
        return cls(first_name, last_name, plan_tier='premium', plan_cost=10)

    def can_access(self, content):
        tiers = {'free': 0, 'premium': 1}
        return tiers[self.plan_tier] >= tiers[content['tier']]

    def bill_for(self, months):
        return self.plan_cost * months
    



marco = Customer('Marco', 'Polo')  # Defaults to the free tier
print(marco.name)  # Marco Polo
print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
print(victoria.name)  

# Polimorphism with Class and magic methods
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return f"Punto en el plano: ({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y  

    def __multiply__(self, other):
        return Point(self,self.x * other.x, self.y * other.y)
    
p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)  # Point(6, 8)
print(p1 == p2)  # False 
p3 = Point(2, 3)
print(p1 == p3)  # True
print(p1.__repr__())  # Point(2, 3)
print("FIN CLASES")

# Exceptions
print("EXCEPCIONES")
print(TypeError.mro())

class InvalidPasswordError(ValueError):
    pass


INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError("Password cannot be the same as your username.")
    if password in INVALID_PASSWORDS:
        raise InvalidPasswordError("Password cannot one of the most common passwords.")


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        validate_password(username, password)
    except InvalidPasswordError as err:
        print(err)
    else:
        account = create_account(username, password)
    finally:
        print("Validated password against username and collection")

main("user1", "password")  # Password cannot one of the most common passwords.
main("user2", "user2")     # Password cannot be the same as your username.
main("user3", "s3cur3p@ss")  # Validated password against username and collection   

#product.py 
class Product:
    def __init__(self, name, description, price, seller, available=True):
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller
        self.available = True
        self.reviews = []

#reuview.py
class Review:
    def __init__(self, content, user, product):
        self.content = content
        self.user = user
        self.product = product      

  #user.py
#from review import Review
#from product import Product
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []

    def write_review(self, content, product):
        review = Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        print(f"{self.name}'s review of {product.name}: {review.content}")
        return review

    def sell_product(self, name, description, price):
        product = Product(name, description, price, self, available=True)
        print(f"{product} is on the market!")
        return product

    def buy_product(self, product):
        if product.available:
            print(f"{self} is buying {product}.")
            product.available = False
        else:
            print(f"{product} is no longer available.")

    def __str__(self):
        return f"User(id={self.id}, name={self.name})" 

brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True

class A:
    def methodA():
        print("Metodo de A")

class B(A):
    def methodB():
        print("Metodo de B")

a = A
a.methodA()
b= B
print(a.__module__)
print(a.__name__)
print(b.mro())
