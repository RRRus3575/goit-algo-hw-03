import re

def normalize_phone(phone_number):
    
    correct_phone = re.sub(r'\D', '', phone_number)

    if not correct_phone.startswith('+'):
        correct_phone = '+38' + correct_phone

    return correct_phone