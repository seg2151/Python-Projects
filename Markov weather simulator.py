# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:06:58 2016

@author: segarcia15
"""

import random
import matplotlib
import matplotlib.pyplot as plt
import time

#function to return either sunny, cloudy, rainy
def weather():
    #given yesterday's weather
    chance = random.random()
    global yest_weather
    if yest_weather == 'sunny':
        if chance < .8:
            yest_weather = 'sunny'
            return 'sunny'
        elif chance <.95:
            yest_weather = 'cloudy'
            return 'cloudy'
        else:
            yest_weather = 'rainy'
            return 'rainy'
    elif yest_weather == 'rainy':
        if chance < .8:
            yest_weather = 'rainy'
            return 'rainy'
        elif chance < .95:
            yest_weather = 'cloudy'
            return 'cloudy'
        else:
            yest_weather = 'sunny'
            return 'sunny'
    else:
        if chance < .5:
            yest_weather = 'cloudy'
            return 'cloudy'
        elif chance < .75:
            yest_weather = 'sunny'
            return 'sunny'
        else:
            yest_weather = 'rainy'
            return 'rainy'

yest_weather = 'rainy'
#print (weather())
suns = 0
rains = 0
clouds = 0
days = 0
wS = []
wR = []
wC = []
wD = []
for i in range(10000):
    day = weather()
    if day == 'sunny':
        suns +=1
        wS.append(suns)
        wR.append(rains)
        wC.append(clouds)
    elif day == 'cloudy':
        clouds +=1
        wS.append(suns)
        wR.append(rains)
        wC.append(clouds)
    else:
        rains +=1
        wS.append(suns)
        wR.append(rains)
        wC.append(clouds)
    days += 1
    wD.append(days)
print('Number of sunny days: ', suns)
print('Number of rainy days: ', rains)
print('Number of cloudy days: ', clouds)

plt.plot(wD, wS, 'r', wD, wR, 'g', wD, wC, 'b')
plt.show()
        
    
    

