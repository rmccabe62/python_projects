

from abc import ABC, abstractmethod
class student(ABC):
    def tuition(self,amount):
        print("Your total tuition is: ",amount)
# this function is telling us to pass in an arguement, but we don't reveal how
# or what kind of data it is.
    @abstractmethod
    def pay_amount(self,amount):
        pass

class CreditCardPayment(student):
# Here we dine how to implement the payment method function from the parent class.
    def pay_amount(self,amount):
        print('Your tuition amount of {} exceeds your credit card balance limit of $2000'.format(amount))

obj = CreditCardPayment()
obj.tuition("$5000")
obj.pay_amount("$5000")

        
