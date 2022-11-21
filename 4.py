a=[]
for i in range(256):
    arr=list(map(int,input().split()))
    a.append(arr)
n=len(a)

for i in range(n):
    
    for j in range(n):
        
        if a[i][j]==0:
            break
        
startLeft=[i,j]

for i in range(n):
    
    for j in range(n-1,0,-1):
        
        if a[i][j]==0:
            break
        

startRight=[i,j]

for i in range(n-1,0,-1):
    
    for j in range(n):
        
        if a[i][j]==0:
            break
        

endLeft=[i,j]

for i in range(n-1,0,-1):
    
    for j in range(n-1,0,-1):
        
        if a[i][j]==0:
            break
        

endRight=[i,j]


print(endLeft,",",endRight,",",startLeft,",",startRight)
