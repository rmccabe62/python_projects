

class Vacation():
    season = "Unknown"
    weather = "Good"
    activity = "Unknown"
    budget = 2500

    def vacaType(self):
        self.season = season
        self.activity = activity

class Summer(Vacation):
    season = 'Summer'
    activity = 'Swimming'
    destination = 'Florida'
    transportation = 'Airplane'

    def vacaType(self):
        
        if (self.season == 'Summer' and self.activity == 'Swimming'):
            print("Have a good time" + self.activity + " on your " + self.season + "vacation")
        else:
            print("Are you enjoying your staycation?")
    

class Winter(Vacation):
   
    season = 'Winter'
    activity = 'Skiing'
    clothing = 'Heavy'
    equipment = 'skis'

    def vacaType(self):
        
        
        if (self.season == 'Winter' and self.activity == 'Skiing'):
            print("Have a good time " + self.activity + " on your " + self.season + " vacation")
            print("Are you going to spend your vacation on  " + self.equipment + " this year?")
        else:
            print("Are you enjoying your staycation?")
vaca = Winter()
vaca.vacaType()
                
    
        
                
        
