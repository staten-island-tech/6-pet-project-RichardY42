class pet:
    def __init__(self, name, ptype, age, toyinv, energy, state):
        self.name=name
        self.ptype=ptype
        self.age=age
        self.toyinv=toyinv
        self.energy=energy
        self.state=state
    def play(self,trick):
        if trick == "fly" and self.energy >0:
            print(f"{self.name} flew.")
            self.energy-=1
            print(f"energy lvl:{self.energy}")
        if self.energy == 0:
            self.state = "unconscious"
        if self.state=="unconscious":
            
talonflame=pet("Dude", "bird", (f"{2} years old"), ["squeaky toy"], 15, "awake")
print("Congrats you have captured a talonflame choose an option to interact with it.") 
talonawake= True
while talonawake:
    playinput=input("Play or Feed ")
    if playinput == "fly":
        talonflame.play("fly")

