user=['saksham','yuvank','lovesh','manav']
pin=['1234','abcd','7890','hello']
bal=['5675','9876','12345','6753']
while(1):
    count=0
    count2=0
    ind=0
    ind1=0
    x=input('enter your name')
    for i in range (len(user)):
        if (x==user[i]):
            count=count+1
            ind=i
    if (count==1):
        y=input ('please enter pin')
        if (y==pin[ind]):
            z=input('press 1 for check balance\npress 2 for withdraw\npress 3 for deposit\npress 4 for transfer')
             
            if (z=='1'):
                print('your balance is :',bal[ind])
            elif(z=='2'):
                amt =int(input('enter amout'))
                if(amt<=int(bal[ind])):
                    print('thank you')
                    bal[ind]=str(int(bal[ind])-amt)
            elif(z=='3'):
                amt=int(input('enter amount'))
                print('thank you')
                bal[ind]=str(int(bal[ind])+amt)
            elif(z=='4'):
                u1=input('enter user name per transfer')
                for i in range (len (user)):
                    if (u1==user[i]):
                        count2+=1
                        ind2=i
                if (count2==1):
                    amt=int(input('enter amount'))
                    if(amt<=int(bal[ind])):
                        bal[ind]=str(int(bal[ind])-amt)
                        bal[ind2]=str(int(bal[ind2])+amt)
                        print('thank you for transfering amount')
        else:
            print('wrong user name')

        
