num =11
flag = 0

for a in range(2,num-1):
		if (num%a) == 0:
			flag=1
			break

if flag:
	print("素数でない")
else:
	print("素数です")