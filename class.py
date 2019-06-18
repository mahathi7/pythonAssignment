# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:48:41 2019

@author: Mahathi Surampudi
"""

class stud():
    def register(self,USN,Name,Std,Section):
        self.USN = USN
        self.Name = Name
        self.Std = Std
        self.Section = Section
    
    def information(self):
        print('USN',self.USN,'Name',self.Name,'Std',self.Std,'Section',self.Section)
        
John = stud()
John.register(129,'John','10','B')
John.information()
Tom = stud()
Tom.register(77,'Tom','8','A')
Tom.information



class calculator():
    def add(self,a,b):
        self.a = a
        self.b = b
        return a+b
        
    def sub(self,a,b):
         self.a = a
         self.b = b
         return a-b
        
    def mul(self,a,b):
         self.a = a
         self.b = b
         return a*b
        
    def div(self,a,b):
         self.a = a
         self.b = b
         return a/b
        
        
calc = calculator()
print(calc.add(4,5))
print(calc.sub(10,4))
print(calc.mul(3,2))
print(calc.div(4,2)) 


