from sys import stdin,stdout
input,print = stdin.readline,stdout.write
def prime(nb):
	for div in range(2,nb):
		if nb % div == 0:
			return False
	return True
i, count = 2, 0
while count < 10001:
	if prime(i): count += 1
	i += 1
print(str(i - 1))