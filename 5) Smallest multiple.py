from sys import stdin,stdout
input,print = stdin.readline,stdout.write
def fromto(n):
	check = True
	for div in range(1,20):
		if n % div != 0: check = False
	return check
nb,working = 0,True
while working:
	nb += 1
	if fromto(nb):
		print(str(nb))
		working = False