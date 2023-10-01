n= int(input())
cnt=1
si = 1
ei = 1
sm=1
answer=0
while ei <=n:
    if sm<n:
        ei+=1 
        sm+=ei
    elif sm==n:
        answer+=1
        #왜?
        ei+=1
        sm+=ei
    else:
        sm-=si
        si+=1
        
print(answer)