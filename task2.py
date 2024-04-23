
import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max - min < quantity or not isinstance(min, (int, float)) or not isinstance(min, (int, float)) or not isinstance(max, (int, float)) or not isinstance(quantity, (int, float)):
        return ''
    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))

    return result



print(get_numbers_ticket(10, 20, 3))
print(get_numbers_ticket(30, 20, 3))