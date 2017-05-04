import os

def run(**args):
	print"[*] W modlule dirlister"
	files= os.listdir(".")
	
	return str(files)
	
	