class pet:
    def __init__(self, name, ptype, lvl, inv, energy, state):
        self.name=name
        self.ptype=ptype
        self.lvl=lvl
        self.inv=inv
        self.energy=energy
        self.state=state


    def play(self):
        playable=True
        while playable:
            
            if self.state=="awake":
                print("Choose an option")
                trick=input("Options: fly ")
                if trick == "fly":
                    print(f"{self.name} flew.")
                    self.energy-=1
                    print(f"energy:{self.energy}")
            if self.energy == 0:
                self.state="unconscious"
                print(f"{self.name} is {self.state}, heal them and then feed them in order to play.")
                playable=False
        
        
    
    
    def feed(self):
        print("Choose an option")
        food=input("Options: test ")
        if food == "test" and self.state=="awake":
            print(f"{self.name} ate a {food}.")
            self.energy+=1
            print(f"energy:{self.energy}")
        
        if self.state=="unconscious":
            print(f"{self.name} is unconscious, heal them in order to feed.")
    

    
    
    def heal(self): 
        healing=True     
        while healing:
            
            heal=input(f"do you want to heal {self.name}? y/n ")
            if heal == "y" and self.inv>0:
                self.inv-=1
                self.state="awake"
                print("You have used 1 max potion")
                print(f"{self.name} is {self.state}")
                print(f"inventory: {self.inv} Max potion(s)")
            if heal == "n":
                healing=False
            if self.inv==0:
                print("you dont have any potions left.")
                healing=False
            
    """ def end(self):
         
        fin=input("Would you like to see the stats? y/n")
        if fin == "y":
            print(f"{self.name}: lvl:{self.lvl} type: {self.ptype}")
        if fin=="n":
            print("you didnt catch them all.") """





talonflame=pet("talonflame", "bird", 1, 10, 1, "awake")
print(f"Congrats you have captured a pokemon choose an option to interact with it.") 
playing=True
while playing:
    
    inichoose=input("play feed heal ")
    if inichoose=="play":
        talonflame.play()
    if inichoose=="feed":
        talonflame.feed()
    if inichoose=="heal":
        talonflame.heal()
    contin=input("would you like to continue? y/n ")
    if contin=="y":
        playing=True
    if contin=="n":
        print("Your pokemon has been put in the PC.")
        print("you didnt catch them all.")
        playing=False
    


        
    """ if inichoose=="end":
    talonflame.end() """