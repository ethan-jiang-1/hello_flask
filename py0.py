"""
Module Documentation
Words Go Here
"""

spam = 40

def square(x):
	""" Function Documentation: Can we have you liver then ? """
	return x**2

class Employee:
	"""Class Documentation """
	pass

def f1(x):
    x = 88
    print(x+1)
    def f2(x):
    	print(x+2)
    f2(x)
f1(1)

def gensquares(n):
	for i in range(n):
		yield i**2


print(square(4))
print(square.__doc__)
