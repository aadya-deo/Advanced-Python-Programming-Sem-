# Payment Strategy
class PaymentStrategy:

    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card")


# PayPal Payment
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print("Paid Rs.", amount, "using PayPal")


# Bitcoin Payment
class BitcoinPayment(PaymentStrategy):

    def pay(self, amount):
        print("Paid Rs.", amount, "using Bitcoin")


# Payment Processor
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    # Switch strategy at runtime
    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Take amount from user
amount = float(input("Enter amount in Rs: "))

# Select payment method
print("\nChoose payment method:")
print("1. Credit Card")
print("2. PayPal")
print("3. Bitcoin")

choice = int(input("Enter your choice: "))


# Decide which strategy to use
if choice == 1:
    strategy = CreditCardPayment()

elif choice == 2:
    strategy = PayPalPayment()

elif choice == 3:
    strategy = BitcoinPayment()

else:
    print("Invalid choice")
    exit()


# Create processor and process payment
processor = PaymentProcessor(strategy)
processor.process_payment(amount)