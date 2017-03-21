#Input index to return what number is in that position of the Fibonacci sequence

def fibonacci(x):
	if x > 1:
		return fibonacci(x-1) + fibonacci(x-2)
	return x
