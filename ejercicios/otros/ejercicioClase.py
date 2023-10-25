def foo(a):
	print('ID de la variable a en función: {}'.format(id(a)))
	a+=1
	print('ID de la variable a en función 2: {}'.format(id(a)))
	print('Variable a incrementada en función: {}, ID: {}'.format(a, id(a)))
	
a = 2
print('ID de la varibale a: {}'.format(id(a)))
foo(a)
print('Variable después de función: {}'.format(a))
