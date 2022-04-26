import zipfile
import os, shutil, pathlib, fnmatch


for i in range(999, 0, -1):
	
	result = os.popen("python3 /home/noa/Desktop/ctf/mocr.py pwd.png").read()
	result = result.replace("\n", "")
		
	file_name = 'flag_{}.zip'.format(i)
	pswd = result
	
	print(i)

	with zipfile.ZipFile(file_name) as file:
		# password you pass must be in the bytes you converted 'str' into 'bytes'
		file.extractall(pwd = bytes(pswd, 'utf-8'))
		
	os.remove("pwd.png")
	os.remove(file_name)
	next_file_name = 'flag_{}.zip'.format(i-1)
	shutil.move("/home/noa/Desktop/ctf/flag/{}".format(next_file_name), "/home/noa/Desktop/ctf/") #moving the new files back to the origin folder
	shutil.move("/home/noa/Desktop/ctf/flag/pwd.png", "/home/noa/Desktop/ctf/")


