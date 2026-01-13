class ThemeParkPass:
    def __init__(self, guestname, passtype, ridesused, ridelimit,isvalid):
        self.guestname = guestname
        self.passtype = passtype
        self.ridesused = ridesused
        self.ridelimit = ridelimit
        self.isvalid = isvalid
    def canride(self, ridename):
        if not self.isvalid:
            return False
        elif len(self.ridesused) >= self.ridelimit:
            return False
        self.ridesused.append(ridename)
        return print(f"you have riden {ridename}")
    
    
    
guest0=ThemeParkPass("John","Basic", [], 5, True) 
guest1=ThemeParkPass("Jane", "Premium", [], 10, True)
guest2=ThemeParkPass("Jim", "Premium", [], 10, True)
passes=[guest0,guest1,guest2]
#guest0.canride("ride 1")

def countpremiumpasses(passes):
        count=0
        for i in passes:
            if i == "Premium" and i == True:
                count +=1
        return count

countpremiumpasses(passes)
