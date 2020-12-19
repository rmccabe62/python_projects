
# create parent class
class Vacation():
    season = "Unknown"
    weather = "Good"
    activity = "Unknown"
    budget = 2500

    # define function for parent class
    def vacaType(self):
        self.season = season
        self.activity = activity

# create child class
class Summer(Vacation):
    season = 'Summer'
    activity = 'Swimming'
    destination = 'Florida'
    transportation = 'Airplane'

    # use polymorphism to add to the function from parent class
    def vacaType(self):
        
        if (self.season == 'Summer' and self.activity == 'Swimming'):
            print("Have a good time" + self.activity + " on your " + self.season + "vacation")
        else:
            print("Are you enjoying your staycation?")
    
# create another child class
class Winter(Vacation):
   
    season = 'Winter'
    activity = 'Skiing'
    clothing = 'Heavy'
    equipment = 'skis'

    # use polymorphism to add to the function from parent class to update second child class
    def vacaType(self):
        
        
        if (self.season == 'Winter' and self.activity == 'Skiing'):
            print("Have a good time " + self.activity + " on your " + self.season + " vacation")
            print("Are you going to spend your vacation on  " + self.equipment + " this year?")
        else:
            print("Are you enjoying your staycation?")

# create variable object to access and call function for desired output
vaca = Winter()
vaca.vacaType()
                
    
        
                
        
