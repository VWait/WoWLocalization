from django.test import TestCase


class A:
	x = 0


a = A()

setattr(a, 'x', None)

print(a.x)