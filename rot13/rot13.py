def rot13(text) :
	chk1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	chk2 = 'abcdefghijklmnopqrstuvwxyz'
	res = ''
	for char in text :
		if char in chk1 :
			ind = chk1.index(char)
			ind = (ind + 13) % 26
			res = res + chk1[ind]

		elif char in chk2 :
			ind = chk2.index(char)
			ind = (ind + 13) % 26
			res = res + chk2[ind]

		else :
			res = res + char

	return res