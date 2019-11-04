"""

Created by aditya on 25/12/18 at 1:53 PM

"""


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        f_list = []
        for i in self.ingredients:
            for j in self.toppings:
                f_list_mini = []
                f_list_mini = [i,j]
                f_list.append(f_list_mini)

        return f_list


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]