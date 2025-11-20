consumables=[
    {
        "name": "Leppa Berry",
        "amount": 100,
        "effect": "A Berry that can be fed to a Pokémon to restore 1 energy",
    },
    {
        "name": "Max Potion",
        "amount": 10,
        "effect": "Fully restores Pokémon HP"
    }
]

lvlsys=[3,8,15,24,35,48,63,80]

class pet:
    def __init__(self, name, lvl, exp, inv, energy, state, day):
        self.name=name
        self.lvl=lvl
        self.exp=exp
        self.inv=inv
        self.energy=energy
        self.state=state
        self.day=day
    
    
    def start(self):

        playing=True
        while playing:
            print("choose an option")
            initchooseCAP=input("play feed heal stats ")
            initchoose=initchooseCAP.lower()
            print(initchoose)
            if initchoose=="play":
                talonflame.play()
            elif initchoose=="feed":
                talonflame.feed()
            elif initchoose=="heal":
                talonflame.heal()
            elif initchoose=="stats":
                talonflame.stats()
            elif initchoose!="play" or initchoose != "feed" or initchoose!= "heal" or initchoose!="stats":
                print("invalid option")
            if self.state=="dead":
                playing == False
                deathinterCAP=input("choose an option: death ")
                deathinter=deathinterCAP.lower()
                if deathinter=="death":
                    talonflame.stats()
                    print(f"you didnt catch them all. Days: {self.day}")
                elif deathinter!="death":
                    print ("invalid option")
                
                #playing=True
            """ continCAP=input("would you like to continue? y/n ")
            contin=continCAP.lower()
            if contin=="y":
                playing=True
            if contin=="n":
                print("Your pokemon has been put in the PC.")
                print("you didnt catch them all.")
                playing=False
            if contin!="y"or"n":
                print("invalid option")
                continCAP
 """

    
    def play(self):
        #playable=True
        #while playable:
        
        if self.state=="dead":
            return "hes dead, let go"
            
        if self.energy == 0:
            self.state="unconscious"
            print(f"{self.name} is {self.state}, heal them and then feed them in order to play.")
            #playable=False

        if self.energy>0:
            print("Choose an option")
            trickCAP=input("Option: fly ")
            trick=trickCAP.lower()
            
                #talonflame.start()
            if trick == "fly":
                self.exp+=1
                print(f"{self.name} flew.")
                self.energy-=1
                print(f"energy:{self.energy}")
                print(f"exp:{self.exp}")
                for i in range(len(lvlsys)):
                    if self.exp == i in lvlsys:
                        self.lvl+=1
                        print(f"{named} has leveled up to level {self.lvl}")
                
                talonflame.start()
            elif trick != "fly":
                print("invalid option")
                talonflame.play()
        

            
        
    
    
    def feed(self):
        #eating=True
        #while eating:
        if self.state=="dead":
            return "hes dead, let go"
        if self.state=="unconscious":
            print(f"{self.name} is unconscious, heal them in order to feed.")
            return
        print("Choose an option")
        foodCAP=input("Option: leppa berry ")
        food=foodCAP.lower()
        if consumables[0]['amount']<=0:
            print("you dont have any leppa berry left.")
            #eating=False
        if food == "leppa berry" and self.state=="awake":
            print(f"{self.name} ate a {consumables[0]['name']}.")
            self.energy+=1
            consumables[0]['amount']-=1
            print(f"You have: {consumables[0]['amount']} leppa berry(s) left")
            print(f"energy:{self.energy}")
            talonflame.start()
        elif food!="leppa berry":
            print("invalid option")
        
        

    
    
    def heal(self): 
        #healing=True     
        #while healing:
        if self.state=="dead":
            return "hes dead, let go"
        healCAP=input(f"do you want to heal {self.name}? y/n ")
        heal=healCAP.lower()
        if consumables[1]['amount']<=0 and self.state=="unconscious":
            print("you dont have any potions left.")
            nochoiceCAP=input(f"would you like to put down {named}? y/n ")
            nochoice=nochoiceCAP.lower()
            if nochoice=="y":
                self.state="dead"
            elif nochoice!="y":
                print("invalid option")
        elif consumables[1]['amount']<=0 and self.state!="unconscious":
            print("your broke out of potion")
            talonflame.start()
        elif heal == "y" and consumables[1]['amount']>0:
            consumables[1]['amount']-=1
            self.state="awake"
            print ("it will take a day")
            self.day+=1
            print(f"{self.name} is {self.state}")
            print(f"You have used 1 {consumables[1]['name']}")
            print(f"inventory: {consumables[1]['amount']} Max potion(s)")
        elif heal == "n":
            talonflame.start()
        elif heal!="y" or heal!="n":
            print("invalid option")

    def stats(self):
        print(f"Name: {self.name}, lvl: {self.lvl}, exp: {self.exp}, inv: {self.inv}, energy: {self.energy}, state: {self.state}")

    
        
        
print(f"Congrats you have captured a pokemon choose an option to interact with it.")
named=input("whats talonflames name? ")
# def __init__(self, name, lvl, exp, inv, energy, state):
talonflame=pet(named, 1, 0, consumables, 5, "awake",0)
talonflame.start()


""" spiralCAP=input("y/n ")
        spiral=spiralCAP.lower()
        if spiral=="y":
            print(f"Name: {self.name}, lvl: {self.lvl}, exp: {self.exp}, inv: {self.inv}, energy: {self.energy}, state: {self.state}")
        if spiral=="n":
            input("you have to let go ") """



            
""" def end(self):
        
    fin=input("Would you like to see the stats? y/n")
    if fin == "y":
        print(f"{self.name}: lvl:{self.lvl} type: {self.ptype}")
    if fin=="n":
        print("you didnt catch them all.") """





#talonflame=pet("talonflame", "bird", 1, 10, 30, "awake")

    


        
""" if inichoose=="end":
talonflame.end() """