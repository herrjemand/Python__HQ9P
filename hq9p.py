def hq9p(c):
	"""
	HQ9+
	By Herr Niemand 2014 
	Version 1.0
	Origin: https://github.com/herrniemand/Python__HQ9P

	arguments:
		(string)c - hq9+ code

	help: http://esolangs.org/wiki/HQ9+

	Copyrights Herr Niemand. 
	All right reserved, preserved, precooked and prepared to rage agaings the machines!
	GPLv2
	"""
	for i in c:
		mem = 0
		if i == 'H': print('Hello World!')
		elif i == 'Q': print(c)
		elif i == '9':
			for i in range(98, -1,-1):
				x = str(i + 1) + ' bottles of beer on the wall, ' + str(i + 1) + ' bottles of beer. Take one down, pass it around, '
				if i: print(x + str(i) + ' bottles of beer on the wall.')
				else: print(x + 'No bottles of beer on the wall.')
		elif i == '+': mem += 1 #Jep. No point this line holds.