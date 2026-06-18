from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass



class CreditCardPayment(Payment):

    def process_payment(self, amount):

        print(f"Credit Card payment of ₹{amount} successful.")



class UPIPayment(Payment):

    def process_payment(self, amount):

        print(f"UPI payment of ₹{amount} successful.")




credit_card = CreditCardPayment()

upi = UPIPayment()



credit_card.process_payment(5000)

upi.process_payment(1500)