import random

def password():
	password = ""
	length = int(input("How long do you want your password to be: "))

	for i in range(length):
		password += chr(random.randint(48, 122))

	print(password)

password()
