import psutil

try:
	print(psutil.cpu_count())
except:
	pass