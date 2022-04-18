password = 'a123456'
i = 3 # number of chance left
while i > 0:
	pwd = input('Please enter password: ')
	if pwd == password:
		print('Login Success!')
		break # Escape from loop
	else:
		i = i - 1
		print('Wrong password!', i , 'more chance')