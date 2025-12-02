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

lvlsys=[3,8,17,24,35,48,63,80]

class pet:
    def __init__(self, name, lvl, exp, inv, energy, state, day):
        self.name=name
        self.lvl=lvl
        self.exp=exp
        self.inv=inv
        self.energy=energy
        self.state=state
        self.day=day
    
    def lvlingsys(self):
        self.lvl=1
        for i in range(len(lvlsys)):
            if self.exp not in lvlsys and not self.exp > lvlsys[i]:
                print(f"{self.name} is at level {self.lvl}")
                return 
            if self.exp >= lvlsys[i]:
                self.lvl+=1
        print(f"{self.name} is at lvl {self.lvl}")
        return
                            
    def play(self):    
        if self.state=="dead":
            return "hes dead, let go"
        if self.energy <= 0:
            self.state="unconscious"
            print(f"{self.name} is {self.state}, heal them and then feed them in order to play.")
            
        if self.energy>0:
            print(f"Choose a move, 1,2,3, or 4, for {self.name} to use:"),
            print("Options:",
                  "1. aerial ace",
                  "2. flare blitz",
                  "3. brave bird",
                  "4. steel wing" )
            tricknotint=input("choice: ")
            
            if not tricknotint.isdigit():
                print("invalid option: not a number")
                self.play()
            
            trick=int(tricknotint)
            if trick not in (1,2,3,4):
                print("invalid option: not a valid number")
                self.play()
        
            if trick == 1:
                self.exp+=2
                print(f"{self.name} used aerial ace.")
                self.energy-=2
                
            elif trick == 2:
                self.exp+=1
                print(f"{self.name} used flare blitz.")
                self.energy-=1
               
            elif trick == 3:
                self.exp+=4
                print(f"{self.name} used brave bird.")
                self.energy-=4
                
            elif trick == 4:
                self.exp+=3
                print(f"{self.name} used steel wing.")
                self.energy-=3
            if self.energy <0:
                self.energy=0
            print(f"energy:{self.energy}")
            print(f"exp:{self.exp}")
            self.lvlingsys()
            
    
    def feed(self):
        #eating=True
        #while eating:
        if self.state=="dead":
            return "hes dead, let go"
        if self.state=="unconscious":
            print(f"{self.name} is unconscious, heal them in order to feed.")
            return
        print("Choose an option")
        food=input("Option: leppa berry ").lower()
        if food!="leppa berry":
            print("invalid option")
            self.feed()
        if consumables[0]['amount']<=0:
            print("you dont have any leppa berry left.")
            return
        if food == "leppa berry" and self.state=="awake":
            print(f"{self.name} ate a {consumables[0]['name']}.")
            self.energy+=1
            consumables[0]['amount']-=1
            print(f"You have: {consumables[0]['amount']} leppa berry(s) left")
            print(f"energy:{self.energy}")
            
        
        
    def heal(self): 
        #healing=True    
        #while healing:
        if self.state=="dead":
            return "hes dead, let go"
        heal=input(f"do you want to heal {self.name}? y/n ").lower()
        
        if consumables[1]['amount']<=0 and self.state=="unconscious":
            print("you dont have any potions left.")
            nochoiceCAP=input(f"would you like to put down {named}? y/n ")
            nochoice=nochoiceCAP.lower()
            if nochoice=="y":
                self.state="dead"
            elif nochoice!="y":
                print("invalid option")
        elif consumables[1]['amount']<=0 and self.state!="unconscious":
            print("your out of potion")
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
            #talonflame.start()
            return
        elif heal!="y" or heal!="n":
            print("invalid option")

    def stats(self):
        print(
            f"Name: {self.name}, "
            f"lvl: {self.lvl}, " 
            f"exp: {self.exp}, "
            f"inv: {self.inv}, " 
            f"energy: {self.energy}, "
            f"state: {self.state}, "
            f"Days: {self.day}"
        )

    def start(self):
            playing=True
            while playing:
                print("choose an interaction option")
                initchoose=input("play feed heal stats ").lower()
                print(initchoose)
                if initchoose=="play":
                    self.play()
                elif initchoose=="feed":
                    self.feed()
                elif initchoose=="heal":
                    self.heal()
                elif initchoose=="stats":
                    self.stats()
                elif initchoose!="play" or initchoose != "feed" or initchoose!= "heal" or initchoose!="stats":
                    print("invalid option")
                if self.state=="dead":
                    print(f"you didnt catch them all. Days survived: {self.day}")
                    break
                    
        
print(f"Congrats you have captured a pokemon.")
named=input("whats talonflames name? ")
# def __init__(self, name, lvl, exp, inv, energy, state):
talonflame=pet(named, 1, 0, consumables, 5, "awake",0)
talonflame.start()
