def my_range(*args):
	if len(args) == 0:
		raise TypeError
	if len(args) == 1:
		i = 0
		while i < args[0]:
			yield i
			i += 1
	elif len(args) == 2:
		i = args[0]
		while i < args[1]:
			yield i
			i += 1
	elif len(args) == 3:
		if args[0] > args[1] and args[2] < 0:
			i = args[0]
			while i > args[1]:
				yield i
				i += args[2]
		elif args[0] < args[1] and args[2] > 0:
			i = args[0]
			while i < args[1]:
				yield i
				i += args[2]
				
for i in my_range(5):
	print(i, end= ' ')
print()
	
for i in my_range(5, 10):
	print(i, end= ' ')
print()

for i in my_range(15, 1, -2):
	print(i, end= ' ')
print()	

for i in my_range(5, 25, 3):
	print(i, end= ' ')
print()

for i in my_range(5, 5, 3):
	print(i, end= ' ')
print()

for i in my_range():
	print(i, end= ' ')