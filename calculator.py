print('********CALCULATOR********')
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
print("1.Addition \t2.Subtraction \n3.Division \t4.Multiplication\n5.Modulus  \t6.Power of")
c=int(input("Enter which operation to be performed:"))
if(c==1):
      r=a+b
      print('The result is:',r)
elif(c==2):
     r=a-b
     print('The result is:',r)
elif(c==3):
     r=a*b
     print('The result is:',r)
elif(c==4):
     r=a/b
     print('The result is:',r)
elif(c==5):
     r=a%b
     print('The result is:',r)
elif(c==6):
     r=a**b
     print('The result is:',r)
else:
    print('Invalid input!')   
