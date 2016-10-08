#We need a class for heroes and evil dudes
#we need a random generator for the evil dudes
#level up system
from random import *
from time import *

def initWarrior():
    #sets user to Warrior class
    return Warrior(300, 10, 25, 10, 20, 1, ['Strike', 'Heave', 'Balls'], [])
    
def initMage():
    return Mage(150, 50, 10, 25, 15, 1, ['Staffswing'], ['Fireball', 'Bolt', 'Icewind'])
    
def initRogue():
    return Rogue(200, 20, 15, 15, 35, 1, ['Stab', 'Sneak', 'Whirlkick'], [])
#superclass
class Hero:
    '''hp is an int, hit points
    mp is an int, magic points
    strength is in, determings physical attack
    magic is int, determines magic attack
    dext is an int, determines ability to dodge attacks
    attacks is a list of physical attacks
    mattacks is a list of magic attacks'''
    
    def __init__(self, hp, mp, strength, magic, dext, level):
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.magic = magic
        self.dext = dext
        self.level = level
    
    def __str__(self):
        return ('A Hero with {} hp, {} mp, {} strength, {} magic, {} dexterity').format(self.hp, self.mp, self.strength, self.magic, self.dext)
    
    #to get list of attacks
    def getattacks(self):
        return self.attacks
    
    #to get list of magic attacks
    def getmattacks(self):
        return self.getmattacks
        
    #to get level
    def getlevel(self):
        return self.level
        
    def reducemp(self,cost):
        self.mp = self.mp - cost
    
    def reducehp(self, damage):
        self.hp = self.hp - damage
    
    def dealdamage(self, other):
        damage = round(self.chooseattack())
        other.hp = other.hp - damage
        print ('The attack deals {} damage!').format(damage)

    def getstats(self):
        print (str(self) + ' has {} hp, {} mp, {} strength, {} magic, and {} dexterity').format(self.hp, self.mp, self.strength, self. magic, self.dext)
        
    def afterbattle(self):
        print (str(self) + ' has {} hp and {} mp left').format(self.hp, self.mp)
        

#NOW FOR THE FUN PART!

class Warrior(Hero):
    def __init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks):
        Hero.__init__(self, hp, mp, strength, magic, dext, level)
        self.attacks = ['Strike', 'Heave', 'Balls']
        self.mattacks = []
    def __str__(self):
        return ('Warrior') # with {} hp, {} mp, {} strength, {} magic, {} dexterity').format(self.hp, self.mp, self.strength, self.magic, self.dext)
    def Strike(self):
        return self.strength*uniform(.75, 1) 
    def Heave(self):
        if random() <.5:
            return self.strength* uniform(1.25, 2)
        else:
            print 'Attack missed!'
            return 0
            
    def Balls(self):
        if random() <.1:
            return self.strength*10*uniform(1,1.5)
        else:
            print 'Your ballsy attacked missed! You deal damage to yourself'
            self.hp -= self.hp*.25
            return 0
    def chooseattack(self):
        #return attack from a list
        n = 0
        print 'Choose from the following attacks: '
        for i in self.attacks + self.mattacks:
            print str(n+1) + ': ' + i
            n += 1
        self.attack = raw_input('>>>')
        if self.attack == '1':
            return self.Strike()
        elif self.attack == '2':
            return self.Heave()
        elif self.attack == '3':
            return self.Balls()
        else:
            print 'Your hero stumbles!'
                
class Mage(Hero):
    def __init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks):
        Hero.__init__(self, hp, mp, strength, magic, dext, level)
        self.attacks = ['Staffswing']
        self.mattacks = ['Fireball', 'Bolt', 'Icewind']
    def __str__(self):
        return ('Mage')  
        
    def Staffswing(self):
        return self.strength*uniform(.25,.5)
        
    def Fireball(self):
        self.mp -= 5
        return self.magic*uniform(1.25,1.75)
        
    def Bolt(self):
        self.mp -=6
        total = 0
        print ('Bolt attacked {} times!').format(self.magic/10)
        #maybe write code for a method to grab a special descriptor?
        for i in range(self.magic/10):
            total += self.magic*2*random()
        return total
        print ('Bolt attacked {} times!').format(self.magic/10)
        
    def Icewind(self):
        self.reducemp(7)
        return self.magic*uniform(.6,1)
        #write code here to skip opponent's next turn
    
    def chooseattack(self):
        #return attack from a list
        print 'Choose from the following attacks: '
        n = 0
        for i in self.attacks + self.mattacks:
            print str(n+1) + ':' + i
            n += 1
        self.attack = raw_input('>>>')
        if self.attack == '1':
            return self.Staffswing()
        elif self.attack == '2':
            return self.Fireball()
        elif self.attack == '3':
            return self.Bolt()
        elif self.attack == '4':
            return self.Icewind()
        else:
            print 'Your hero stumbles!'    
          
class Rogue(Hero):
    def __init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks):
        Hero.__init__(self, hp, mp, strength, magic, dext, level)
        self.attacks = ['Stab', 'Sneak', 'Whirlkick']
        self.mattacks = []
    def __str__(self):
        return ('Rogue')   
    def Stab(self):
        return self.dext*uniform(.5,.75)+self.strength*uniform(0,.25)
    def Sneak(self):
        #write code for high dodge ability next turn
        if random() < .3:
            return self.dext * uniform(1,1.25)
        else:
            return self.dext * uniform(.1,.5)
    def Whirlkick(self):
        self.reducehp(random()*50)
        return self.strength * uniform(.75,1)+ self.dext*random()
 
    def chooseattack(self):
        #return attack from a list
        print 'Choose from the following attacks: '
        n = 0
        for i in self.attacks + self.mattacks:
            print str(n+1) + ':' + i
            n += 1
        self.attack = raw_input('>>>')
        if self.attack == '1':
            return self.Stab()
        elif self.attack == '2':
            return self.Sneak()
        elif self.attack == '3':
            return self.Whirlkick()
        else:
            print 'Your hero stumbles!'    
            
               
#enemy classes
def initCaterpillar():
    return Caterpillar(10,0,5,0,5,1,['Stringshot', 'Wiggle'], []) 
    
def initCharizard():
    return Charizard(1000,100,45,40,45,20,['Slash', 'Fly'], ['Firespin', 'Flamethrower']) 
    
def initGod():
    return God(1000000,100000, 1000, 1000, 1000, 1000, ['God Punch', 'Mercy'], ['God Light', 'Goku Spirit Bomb'])

class Enemy(Hero):
    def __init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks):
        Hero.__init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks)  
          
class Caterpillar(Hero):
    def __init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks):
        Hero.__init__(self, hp, mp, strength, magic, dext, level)
        self.attacks = ['Stringshot', 'Wiggle']
        self.mattacks = []  
          
    def __str__(self):
        return ('Caterpillar')
            
    def Stringshot(self):
        return self.strength* uniform (.1, .25)
        
    def Wiggle(self):
        print 'Enemy Caterpillar wiggles!'
        return 0
        
    def chooseattack(self):
        print 'Enemy Caterpillar is thinking!'
        self.choice = random()
        if self.choice > .5:
            print 'Enemy Caterpillar uses Stringshot!'
            return round(self.Stringshot())
        else:
            print 'Enemy Caterpillar uses Wiggle!'
            return round(self.Wiggle())
            
class Charizard(Hero):
    def __init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks):
        Hero.__init__(self, hp, mp, strength, magic, dext, level)
        self.attacks = ['Slash', 'Fly']
        self.mattacks = ['Firespin', 'Flamethrower']  
          
    def __str__(self):
        return ('Charizard')
            
    def Slash(self):
        return self.strength* uniform (.75, 1.25)
        
    def Fly(self):
        #dodge increase next turn
        return (self.strength*.5 + self.dext*.5) * uniform (.25, .75)
    
    def Firespin(self):
        self.reducemp(25)
        return (self.magic+self.strength)* uniform (1.25, 2)
        
    def Flamethrower(self):
        self.reducemp(10)
        return self.magic * uniform (1, 1.5)
        
    def chooseattack(self):
        #maybe move attack descriptors to method
        print 'Enemy Charizard is thinking!'
        self.choice = random()
        if self.mp >= 50:
            if self.choice < .3:
                print 'Enemy Charizard uses Firespin! You are probably dead'
                return self.Firespin()
            else:
                print 'Enemy Charizard uses Flamethrower! You are lucky it was not Firespin this time'
                return self.Flamethrower()
        elif 10 < self.mp < 50:
            if self.choice <.5:
                print 'Enemy Charizard uses Firespin! You are probably dead'
                return self.Firespin()
            else:
                print 'Enemy Charizard slashes your fucking face!'
                return self.Slash()
        elif self.hp < 500 and self.choice <.75:
            print 'Enemy Charizard uses Fly! Try and catch him now!'
            return self.Fly()
        else:
            print 'Enemy Charizard slashes your fucking face'
            return self.Slash()
            
            
class God(Hero):
    def __init__(self, hp, mp, strength, magic, dext, level, attacks, mattacks):
        Hero.__init__(self, hp, mp, strength, magic, dext, level)
        self.attacks = ['Stringshot', 'Wiggle']
        self.mattacks = []  
          
    def __str__(self):
        return ('God')
            
    def Godpunch(self):
        print 'God punched your balls'
        return self.strength * random()
        
    def Mercy(self):
        print 'God has shown mercy!'
        return 0
    
    def Light(self):
        print 'God is healing himself by like a million HP'
        self.reducehp(-self.magic*uniform(5,10))
        return 0

    def SpiritBomb(self):
        print 'God calls Goku to throw a spirit bomb on your ass'
        return self.strength*self.magic*self.dext*uniform(1,10)
        
    def chooseattack(self):
        print 'God is thinking!'
        self.choice = random()
        if self.choice < .4:
            return self.Godpunch()
        elif self.choice < .7:
            return self.Mercy()
        elif self.choice < .9:
            return self.Light()
        else:
            return self.SpiritBomb()
#stat tracker
   
#choose class
def chooseclass():
    print 'Welcome! Choose your class: Warrior, Mage, or Rogue'
    choice = raw_input('> ')
    while choice.lower() not in ['warrior', 'mage', 'rogue']:
        choice = raw_input('Please choose one of the classes: ')
    if choice.lower() == 'warrior':
        return initWarrior()
    elif choice.lower() == 'mage':
        return initMage()
    else:
        return initRogue()

player = chooseclass()
print ('You are a {}.').format(player),
print 'Your ', 
player.getstats()

#random encounter
def randomenemy():
    choice = random()
    if choice < .4:
        return initCaterpillar()
    elif choice <.8:
        return initCharizard()
    else:
        return initGod()

enemy = randomenemy()
print 'Your enemy is: '
print enemy

def battle():
    while player.hp > 0: #while someone still has health
        player.dealdamage(enemy) #player chooses attack, add critical hit modifier or dodge modifier
        if enemy.hp <= 0:
            print 'You win!'
            break
        enemy.dealdamage(player)
        if player.hp <=0:
            print 'You lose!'
            break
        player.getstats()
        enemy.getstats()
        #print stats

        #print attack used
        #print if successful
        '''print damage done to everyone
        print mp used, if any
        print hp and mp left # all of these can be done in one method
        enemy_attack #same process'''
                

'''warrior = initWarrior()
print warrior

mage = initMage()
print mage

rogue = initRogue()
print rogue'''

'''opponent = initGod()
player = initMage()'''
battle()