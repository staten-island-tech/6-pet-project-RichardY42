consumables=[
    {
        "name": "Leppa Berry",
        "amount": 10,
        "effect": "A Berry that can be fed to a Pokémon to restore 1 energy",
    },
    {
        "name": "Max Potion",
        "amount": 10,
        "effect": "Fully restores Pokémon HP"
    }
]



class pet:
    def __init__(self, name, lvl, exp, inv, energy, state):
        self.name=name
        self.lvl=lvl
        self.exp=exp
        self.inv=inv
        self.energy=energy
        self.state=state
        
    
    
    def start(self):
        
        playing=True
        while playing:
            print("choose an option")
            inichooseCAP=input("play feed heal ")
            inichoose=inichooseCAP.lower()
            
            if inichoose=="play":
                talonflame.play()
            if inichoose=="feed":
                talonflame.feed()
            if inichoose=="heal":
                talonflame.heal()
            if inichoose!="play" or "feed" or "heal":
                print("invalid option")
                playing=True
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
        playable=True
        while playable:
            if self.energy == 0:
                self.state="unconscious"
                print(f"{self.name} is {self.state}, heal them and then feed them in order to play.")
                playable=False

            if self.energy>0:
                print("Choose an option")
                trick=input("Option: fly ")
                if trick == "fly":
                    self.exp+=10
                    print(f"{self.name} flew.")
                    self.energy-=1
                    print(f"energy:{self.energy}")
                    print(f"exp:{self.exp}")
                if self.exp == 30:
                    self.lvl+=1
                    print(f"{named} has leveled up to level {self.lvl}")
                #talonflame.start()

            
        
    
    
    def feed(self):
        print("Choose an option")
        food=input("Option: Leppa Berry ")
        if food == "Leppa Berry" and self.state=="awake":
            print(f"{self.name} ate a {consumables[0]['name']}.")
            self.energy+=1
            consumables[0]['amount']-=1
            print(f"energy:{self.energy}")
        
        if self.state=="unconscious":
            print(f"{self.name} is unconscious, heal them in order to feed.")
    

    
    
    def heal(self): 
        healing=True     
        while healing:
            
            heal=input(f"do you want to heal {self.name}? y/n ")
            if heal == "y" and consumables[1]['amount']>0:
                consumables[1]['amount']-=1
                self.state="awake"
                
                print(f"{self.name} is {self.state}")
                print(f"You have used 1 {consumables[1]['name']}")
                print(f"inventory: {consumables[1]['amount']} Max potion(s)")
            if heal == "n":
                healing=False
            if self.inv==0:
                print("you dont have any potions left.")
                healing=False



print(f"Congrats you have captured a pokemon choose an option to interact with it.")
named=input("whats talonflames name? ")
# def __init__(self, name, lvl, exp, inv, energy, state):
talonflame=pet(named, 1, 0, consumables, 1, "awake")
talonflame.start()






            
""" def end(self):
        
    fin=input("Would you like to see the stats? y/n")
    if fin == "y":
        print(f"{self.name}: lvl:{self.lvl} type: {self.ptype}")
    if fin=="n":
        print("you didnt catch them all.") """





#talonflame=pet("talonflame", "bird", 1, 10, 30, "awake")

    


        
""" if inichoose=="end":
talonflame.end() """