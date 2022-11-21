def valid(koti):
    koti=str(koti)
    for p in koti:
        if int(p) not in dig:
            return False
    return True
dig=(0,1,2,5,6,8,9)
number = int(input())
if number < len(dig):
    print(dig[number])
else:
    cnt=len(dig)
    key=dig[-1]
    while(cnt<=number):
        key+=1
        if valid(key):
            cnt+=1
    print(key)
