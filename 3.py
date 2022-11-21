def valid(koti):
    koti=str(koti)
    for p in koti:
        if int(p) not in digits:
            return False
    return True
  
  
digits=[0,1,2,5,6,8,9]

number = int(input())
if number < len(digits):
    print(digits[number-1])
else:
    count=len(digits)
    k=digits[-1]
    while(count<=number):
        k+=1
        if valid(k):
            count+=1
    print(k)
