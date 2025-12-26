from wordset import english_word_small

print(type(english_word_small))  # True

def find_anagrams(letters, words):
    # Create a dictionary mapping the canonical representation of a word to all anagrams of those letters.
    lookup = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in lookup:
            lookup[key] = set()
        lookup[key].add(word)

    # Search the lookup table for the queried letters.
    search = ''.join((sorted(letters)))
    return lookup.get(search, set())

#letter = input("Press Enter to see anagrams of 'stone': ")
letter = 'stone'
print("SALIDA 1 ")
print(find_anagrams(letter, english_word_small))  # {'notes', 'onset', 'tones', 'stone'}

from collections import defaultdict

def find_anagrams(letters, words):
    lookup = defaultdict(set, {})  # Create a dictionary subclass that adds sets for missing values.
    for word in words:
        lookup[''.join(sorted(word))].add(word)
    return lookup.get(''.join(sorted(letters)), set())

print("SALIDA 2 CON DEFAULTDICT")
print(find_anagrams(letter, english_word_small))  # {'notes', 'onset', 'tones', 'stone'}

def create_profile(given_name, *surnames, **details):
    print(given_name, *surnames)
    for key, value in details.items():
        print(key, value, sep=': ')

create_profile('John', 'Doe', 'Smith', age=30, city='New York')

# hight order functions: map, filter
def reverse(s):
    return s[::-1]

def first_two(s):
    return s[:2]

a = map(len, ["apple", "orange", "pear"])
b = map(str.upper, ["apple", "orange", "pear"])
c = map(reverse, ["apple", "orange", "pear"])  # Could also be with a lambda function.
d = map(first_two, ["apple", "orange", "pear"])  # Could also be with a lambda function.
print(list(a))  # [5, 6, 4]
print(list(b))  # ['APPLE', 'ORANGE', 'PEAR']
print(list(c))  # ['elppa', 'egnaro', 'raep']
print(list(d))  # ['ap', 'or', 'pe']            

# Iterators and generators
def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

g = generate_fibs()
next(g)  # => 1
next(g)  # => 1
next(g)  # => 2
next(g)  # => 3
next(g)  # => 5
#max(g)   # Don't run this line of code. What happens?
print(next(g))


print("FIBONACCI UNDER N")
def fibs_under(n):
    for fib in generate_fibs():  # Loops over 1, 1, 2, ...
        if fib > n:
            break
        print(fib)

print(fibs_under(15))  # 1 1 2 3 5 8 13
print("FIBONACCI AS LIST UNDER N")

def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c

def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    for n in generate_tribonacci_numbers():
        if n < num:
            continue
        return n == num

print(is_tribonacci(4))   # True
print(is_tribonacci(5))   # False   

# DECORATORS
print("DECORATORS:inicio")
def announce(f):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        result = f(*args, **kwargs)
        print("Function finished.")
        return result
    return wrapper

def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n

div_by_3 = make_divisibility_test(3)
tuple(filter(div_by_3, range(10)))  # => (0, 3, 6, 9)
testnum = 10
print(f"El valor {testnum} es divisible por 5?  ",make_divisibility_test(5)(testnum))  # => True

import functools
cacheargs = {}
def memoize2(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        if args in cacheargs:
            print("Usando valor en cache")
        else:
            print("Calculando nuevo valor")
            cacheargs[args] = function(*args,**kwargs)  
        return cacheargs[args]
    return wrapper

def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
            function._cache[key] = function(*args,**kwargs)
        return function._cache[key]
    return wrapper

import time
@memoize
def long_operation(x, y):
    time.sleep(5)   # Or some other suitable long expression.
    return x + y

print(long_operation(3,4))
print(long_operation(3,4)) 
print(long_operation(5,6))

print("DECORATORS:fin")