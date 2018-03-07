# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:22:31 2018

@author: sadhja02
"""

#******************************Dice Rolling Simulator*************************
#The Objective is to create a dice

# Option 1

import random

def dice():
    print (random.randint(1,6))
    
dice()

#******************************************************************************

#Option 2
ls = [1, 2, 3, 4, 5, 6]  
print (random.choice(ls))

def dice_roll():
    print (random.choice(ls))
    
dice_roll()    

#*****************************************************************************


    
    
    
    