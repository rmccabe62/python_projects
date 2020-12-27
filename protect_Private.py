
# create a protected and private class and define them
class Protected:
    def __init__(self):
        self._protectedStudent= ''
        self.__privateCourse = 'Math'
    def getPrivate(self):
        print(self.__privateCourse)
    def setPrivate(self,private):
        self.__privateCourse = private
        
# get and display the values for the protected and private class
obj = Protected()
obj._protectedStudent = 'John Smith'
print(obj._protectedStudent)
obj.getPrivate()
obj.setPrivate('Math')
obj.getPrivate()


