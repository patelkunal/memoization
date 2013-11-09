import collections
import functools


class memo(object):
	"""
	memoization optimization
	
	usage
	from memoization import memo

	@memo
	def func(arg1, arg2):
		...
		...
		return ...
	"""

	def __init__(self, func):
		self.func = func
		self.cache = {}

	def __call__(self, *args):
		if not isinstance(args, collections.Hashable):
			return self.func(*args)

		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value

	def __repr__(self):
		"""
		Return the function's docstring.
		"""
		return self.func.__doc__

	def __get__(self, obj, objtype):
		"""
		Support instance methods.
		"""
		return functools.partial(self.__call__, obj)
