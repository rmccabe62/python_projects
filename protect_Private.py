

class Protected:
    def __init__(self):
        self._protectedStudent= ''
        self.__privateCourse = 'Math'
    def getPrivate(self):
        print(self.__privateCourse)
    def setPrivate(self,private):
        self.__privateCourse = private
        

obj = Protected()
obj._protectedStudent = 'John Smith'
print(obj._protectedStudent)
obj.getPrivate()
obj.setPrivate('Math')
obj.getPrivate()


