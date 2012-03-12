'''Kind of a creature evolution simulator'''
import random
import sys
if len(sys.argv)>1: count = int(sys.argv[1])
else:   count = int(raw_input())
food = int(250*count*random.random())
bugg=[None]
class bugger:
    '''A living critter'''
    def __init__(self):
        '''Create a bugger'''
        global bugg, bmax
        self.id = len(bugg)
        self.ver = self.id
        bmax = max(bmax, self.id)
        bugg.append(self)
        self.growth = int(random.random()*75) #size of the bugger, critter dies if growth<1
        self.tummy = 0 #Holds food to be used for growth
        self.erate = int(random.random()*10) #Food consumed per turn
        self.grate = int(random.random()*5) #growth per turn
        if self.erate<=self.grate:  self.erate=self.grate+1 #Prevent hibernation
        self.rmax = max(int(random.random()*100), 50) #Threshold of growth for reproduction
        self.rrate = min(int(random.random()*self.rmax), self.growth) #Cost of reproduction
        self.ret = int(random.random()*self.growth*0.5) #Food returned upon death
        self.clrte = max(random.random(), 0.7) #Chances of passing on traits
        if random.random()>=random.random(): self.murd = True #Whether it kills other buggers for food
        else:   self.murd = False
    def eat(self):
        '''Collect food from the world else from a critter; Can eat own growth'''
        global bugg, food
        ok = False
        if (food-self.erate) >= 0:
            food -= self.erate
            ok = True
        lbg = len(bugg)
        i = 0
        while not ok:
            if i>3: bug = self
            else:
                source = int(random.random()*lbg)
                bug = bugg[source]
            if bug:
                if self.murd and bug!=self:
                    self.tummy += int(bug.growth*0.5)-self.erate
                    bug.growth -= bug.growth+5
                else:   bug.growth -= self.erate
                bug.chk()
                break
            i += 1
        self.tummy += self.erate
        return True
    def grow(self):
        '''Convert food to growth & collect food'''
        while self.tummy>0:
            self.tummy -= self.erate
            self.growth += self.grate
        self.eat()
    def get_params(self):
        '''Get the parameters for this bugger'''
        return {"ver":self.ver, "id":self.id, "erate":self.erate, "grate":self.grate, "rrate":self.rrate, "rmax":self.rmax, "clrte":self.clrte, "murd":self.murd, "ret":self.ret}
    def chk(self, gro=False):
        '''Die if growth<1 and reproduce if >rmax'''
        global bugg, food, lstand, repro
        if self.growth < 1:
            bugg[self.id] = None
            food += self.ret
            lstand = self.get_params()
        elif self.growth > self.rmax:
            self.growth -= self.rrate
            bug = bugger()
            if random.random()<self.clrte:
                bug.erate = self.erate
                bug.grate = self.grate
                bug.rmax = self.rmax
                bug.rrate = self.rrate
                bug.ret = self.ret
                bug.ver = self.ver
                #bug.clrte = self.clrte
                bug.murd = self.murd
                bug.growth = self.rrate
            if len(repro)>self.id:   repro[self.id]+=1
            else:   repro.append(1)
        elif gro:
            self.grow()
turns  = 0
mlive = 0
bmax = 0
lstand = 0
grmax = 0
mfood = food
alive = [0]
repro = [0]
while count>0:
    bugger()
    count -= 1
#print([bugg, len(bugg)])
try:
    while filter(None, bugg)!=[]:
        #print("nnnnnnnnnn")
        turns += 1
        mlive = max(len(filter(None, bugg)), mlive)
        for bug in filter(None, bugg):
            if bug:
                bug.chk(True)
                print([bug.id, bug.growth, bug.ver])
                mfood = max(food, mfood)
                grmax = max(grmax, bug.growth)
                if len(alive)>bug.id:   alive[bug.id]+=1
                else:   alive.append(0)
                #print(food)
except: print("EXCEPTION")
finally:
    print(["Turns:", turns])
    print(["Max-Food:", mfood])
    print(["Max-Growth:", grmax])
    print(["Max-Bugs-Alive:", mlive])
    print(["Last-Generation", bmax])
    print(["Last-Standing", lstand])
    print(["Longest-Alive", alive.index(max(alive)), max(alive)])
    print(["Most-Reproduced", repro.index(max(repro)), max(repro)])