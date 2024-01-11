class sugar_can:

    sugar_amount = 0
 
    def sugar_out(self, amount):
        self.sugar_amount -= amount
        print(f'Sugar amount {amount} put out')

    def sugar_in(self, amount):
        self.sugar_amount += amount
        print(f'Sugar amount {amount} put inside')

    def print_amount(self):
        print(f'Inside is {self.sugar_amount} of sugar')

class sugar_can_extended(sugar_can):
    def clean_it(self):
        self.sugar_amount = 0

my_instance = sugar_can_extended()
my_instance.sugar_in(5)
my_instance.print_amount()
my_instance.clean_it()
my_instance.print_amount()
