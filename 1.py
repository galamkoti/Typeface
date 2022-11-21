number=int(input())
koti=""
while(number>0):
	koti+=str(number%3)
	number=int(number/3)
print(koti)
