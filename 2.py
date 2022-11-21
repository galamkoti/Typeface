str1=input()
str2=input()
c=str2[-1]
count=0
for i in str1:
    if i==c:
        count+=1
print(count)
