# -*- coding: utf-8 -*-
name = input ('enter name')
print (type(name))
print('my name is',name)

age = int (input ('enter age'))
print (type(age))
print(type('my age is'))

amount = float (input('enter amount'))
print(type(amount))
print('the amount to be paid is', amount)

#operators
n1 = int (input('enter n1'))
n2 = int (input('enter n2'))
sum=n1+n2
print('sum of the two values',n1,'&',n2,'is',sum)

#difference b/w '/' and '//'
 print(10/3) #prints with decimal, i.e has accuracy
 print(10//3) #prints a single number 
 
 sum=0
 sum=sum+10
 sum +=10
 print(sum)
 
 #relational operators
 n1=10
 n2=20
 n3=30
 print(n1>n2)
 print(n1 != n2)
 print(n1<n2)
 print(n1==n3)
 
 #logical operators
 print(n1>n2 and n1>n3)
 
 #if and else note the syntax
 n1 = 45
 n2 = 18
 if(n1>n2):
    print('n1 is greater')
else:
    print('n2 is greater')
    
#if and elif
std = int(input('enter your std'))

if(std==1):
    print('you are in std 1')
elif(std==2):
    print('you are in std 2')
elif(std==3):
    print('you are in std 3')
else:
    print('you are in other stds than above mentioned')
    
    
#while and for
start = 1
end = 10
while(start<end):
    print(start)
    start = start+1
#prints range taking 0 as default start if start is not mentioned
for i in range(10):
    print(i)    
  
for i in range(10,20):
    print(i)    

for i in range(10,30,2):
    print(i)
    
for i in range(20,10,-1):
    print(i)
    
    
    
    