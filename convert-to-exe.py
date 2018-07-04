import os, shutil

if os.path.exists('dist'):
	shutil.rmtree("dist")
if os.path.exists('build'):
	shutil.rmtree("build")
if os.path.exists('__pycache__'):
	shutil.rmtree("__pycache__")

os.system("pyinstaller -F -i images/voice.ico control-pc-via-voice.py")
shutil.copyfile("dist/control-pc-via-voice.exe", "./control-pc-via-voice.exe")
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")