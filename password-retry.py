password = 'a123456'
i = 3 # number of chance left
while i > 0:
	i = i - 1
	pwd = input('Please enter password: ')
	if pwd == password:
		print('Login Success!')
		break # Escape from loop
	else:
		print('Wrong password!')
		if i > 0:
			print('Wrong password!', i , 'more chance')
		else:
			print('No more chance to enter! Locking account!')