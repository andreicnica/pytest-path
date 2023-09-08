from .americano import americano
from .latte import latte
import random

def main(coffee_type):
    coffee = ""
    if coffee_type == 'latte':
        coffee = latte.make()
    else:
        coffee = americano.make()
    return f"I created {coffee}"
