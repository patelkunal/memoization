memoization
===========
memoization is an optimization technique used primarily to speed up computer programs by having function calls avoid repeating the calculation of results for previously processed inputs.

python implementation for http://en.wikipedia.org/wiki/Memoization


usage

	from memoization import memo
	@memo
	def func(arg1, arg2):
    	# do_some_processing
		# do_some_other_processing
		# return output
