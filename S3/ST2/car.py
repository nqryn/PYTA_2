
class Car:
    def __init__(self, vin, make, model, price, color='BLUE', state='NEW'):
        self.vin = vin  # vehicle identification number
        self.make = make
        self.model = model
        self.color = color
        self.state = state
        self.price = price
        self.is_available = True
        self.selling_price = 0

    def describe(self):
        print('=' * 20, f'{self.make} {self.model}', '=' * 20)
        print(f'Color: {self.color}')
        if self.is_available:
            print(f'Price:  {self.price}')
        else:
            print(f'Selling price: {self.selling_price}')

    def sell(self, discount=0):
        self.is_available = False
        self.selling_price = self.price * (100 - discount) // 100

