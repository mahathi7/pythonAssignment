# -*- coding: utf-8 -*-

#12 table in reverse order
n=12
for i in range(10,0,-1):
    r=n*i
    print(n,'*',i,'=',r)
    
    
#simple interest
    
p = float(input('enter principle amount'))
r = float(input('enter the rate'))
t = int(input('enter time in years'))
SI=(p*r*t)/100
print('the simple interest is',SI)

#prime numbern=2
fact = int(input('enter the number'))
fact = fact*1
print('factorial of',n, 'is',fact)

a = int(input('enter the number'))
for a in range(10,20):
    if(a%1)==0:
    
    print(a)
    
    
#factorial

fact = int(input('enter the number'))
fact = fact*i
print('factorial is',fact) 


#square
a = int(input('enter a number'))
square=a*a
print('the square of',a,'is',square)

#ecity bill

a = int(input('Number of units consumed:'))
if(a<=100):
    r=2*a
    print('amount on the bill is',r)
elif(a>100 and a<=200):
    r=3*a
    print('amount on the bill is',r)
elif(a>200 and a<=300):
    r=5*a
    print('amount on the bill is',r)
else:
    r=6*a
    print('total amount on the bill:',r)