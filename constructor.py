# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:23:30 2019

@author: Mahathi Surampudi
"""

class bike():
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.speed = 0
    
    def start(self):
        if(self.speed==0):
            print('the vehicle is just started')
            return self.speed
    
    def move(self):
        if(self.speed>=0):
            self.speed = self.speed+5
            print('the speed is increasing by 5 units')
            return self.speed
            
    def stop(self):
        if(self.speed==0):
            print('the vehicle has stopped')
            return self.speed
            
    def info(self):
        print('make',self.make,'model',self.model,'color',self.color,'price',self.price)
        
tw = bike('RE','classic350','black','150000')
initialspeed=tw.start()
print('Initial speed',initialspeed)
tw.start()
speed=tw.move()
tw.move()
print('Speed',speed)
tw.stop()
tw.info()




        
        
        
            
    
        
        
        