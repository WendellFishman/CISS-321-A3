#CISS 321 - Assignment3 solution code (Strong Password Validator) 

import re

file1 = open('passwords.txt', 'r')
passwords = file1.readlines()
for password in passwords:
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d_$!]{8,}$"
	match = re.search(re.compile(reg), password)
	if match:
		print("Strong Password")
	else:
		print("Weak Password")