# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:34:45 2016

@author: segarcia15
"""
import matplotlib
import matplotlib.pyplot as plt
import random
import time

'''lower_bust = 31.235
higher_profit = 63.208'''

sampleSize = 100

startingFunds = 10000
wagerSize = 100
wagerCount = 10000

def rollDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif roll <=50:
        return False
    elif 100> roll > 50:
        return True
        
def multiple_bettor(funds, initial_wager, wager_count):
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
    wX=[]
    vY=[]

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager
    
    while currentWager <= wager_count:
        if previousWager == 'win':
            #print ('we won last wager')
            if rollDice():
                value+=wager
                #print (value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                #print (value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print ('we went broke after'.currentWager, 'bets')
                    multiple_busts += 1
                    break
                    
        elif previousWager == 'loss':
            #print ('We lost last one so time to double')
            if rollDice():
                wager = previousWagerAmount* random_multiple
                if (value-wager) < 0:
                    wager = value
                #print ('we won', wager)
                value += wager
                #print (value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            
            else:
                wager = previousWagerAmount* random_multiple
                if (value-wager) < 0:
                    wager = value
                #print ('we lost', wager)
                value -= wager
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print ('we went broke after', currentWager, 'bets')
                    multiple_busts += 1
                    break
                    
                #print (value)
                previousWager = 'loss'
                
                
        currentWager += 1
    #print(value)
    #plt.plot(wX,vY,color)
    if value > funds:
        multiple_profits += 1            

        
def doubler_bettor(funds, initial_wager, wager_count, color): 
    value = funds
    wager = initial_wager

    global doubler_busts
    global doubler_profits   
    
    wX= []    
    vY= []
    
    currentWager = 1
    previousWager = 'win' 
    previousWagerAmount = initial_wager
    
    while currentWager <= wager_count:
        if previousWager == 'win':
            #print ('we won last wager')
            if rollDice():
                value+=wager
                #print (value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                #print (value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print ('we went broke after'.currentWager, 'bets')
                    doubler_busts += 1
                    break
                    
        elif previousWager == 'loss':
            #print ('We lost last one so time to double')
            if rollDice():
                wager = previousWagerAmount*2
                if (value-wager) < 0:
                    wager = value
                #print ('we won', wager)
                value += wager
                #print (value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            
            else:
                wager = previousWagerAmount*2
                if (value-wager) < 0:
                    wager = value
                #print ('we lost', wager)
                value -= wager
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print ('we went broke after', currentWager, 'bets')
                    doubler_busts += 1
                    break
                    
                #print (value)
                previousWager = 'loss'
                
                
        currentWager += 1
    #print(value)
    plt.plot(wX,vY,color)
    if value > funds:
        doubler_profits += 1

def simple_bettor(funds, initial_wager, wager_count, color):
    global simple_busts
    global simple_profits  
    value = funds
    wager = initial_wager
    
    wX = []
    vY = []
    
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value-= wager
            wX.append(currentWager)
            vY.append(value)
            
        currentWager += 1
    if value <= 0:
        simple_busts +=1
    #print ('Funds: ', value)
    plt.plot(wX, vY, color)
    if value > funds:
        simple_profits += 1

doubler_busts = 0
doubler_profits = 0
simple_busts = 0
simple_profits = 0

for i in range(sampleSize):
    simple_bettor(10000, 100, 100000, 'red')
    doubler_bettor(10000, 100, 100000, 'blue')
'''
x = 0
while True:
    multiple_profits = 0.0
    multiple_busts = 0.0
    
    multipleSampSize = 10000
    currentSample = 1
    
    random_multiple = random.uniform(0.1, 5.0)

    while currentSample <= multipleSampSize:
        multiple_bettor(startingFunds, wagerSize, wagerCount)
        currentSample += 1
        
    if (multiple_busts/multipleSampSize*100.00 < lower_bust) and (multiple_profits/multipleSampSize*100.00 > higher_profit):
        print('#########################################')
        print('Found winner! The multiple was: ', random_multiple)
        print('Lower bust to beat', lower_bust)
        print('higher profit rate to beat', higher_profit)
        print('bust rate: ', multiple_busts/multipleSampSize*100.00)
        print('profit rate: ', multiple_profits/multipleSampSize*100.00)
        print ('#########################################')
        
    else:
        pass
    
        print('#########################################')
        print('Found loser! The multiple was: ', random_multiple)
        print('Lower bust to beat', lower_bust)
        print('higher profit rate to beat', higher_profit)
        print('bust rate: ', multiple_busts/multipleSampSize*100.00)
        print('profit rate: ', multiple_profits/multipleSampSize*100.00)
        print ('#########################################')'''

