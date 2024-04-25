import random
print('Welcome\nLet\'s play Rock Paper and Scissor')
print('note: R->Rock ,P->Paper ,S->scissor')
n=1
us=0
ss=0
while(n!=0):
    u=input("Enter your choice(R/P/S):")
    s=random.randint(0,2)
    dic={0:'R',1:'P',2:'S'}
    print('System choice:',dic[s])
    if(u!='R' and u!='P' and u!='s'and u!='S' and u!='r' and u!='p'):
        print('Invalid input...Try Again!')
    else:
        dic1={'R':0,'P':1,'S':2,'r':0,'p':1,'s':2}
        user=dic1[u]
        if(user==s):
            print('Draw')
            flag=0
        elif(user==0 and s==1):
            print('You lose')
            flag=2
        elif(user==1 and s==2):
            print('You lose')
            flag=2
        elif(user==2 and s==0):
            print('You lose')
            flag=2
        else:
            print('You Win')
            flag=1
        if(flag==1):
            us+=1
        elif(flag==2):
            ss+=1
        print('Your score:',us,'\nSystem Score:',ss)
    n=int(input('Do want to continue(enter 0 to end):'))
        
        

