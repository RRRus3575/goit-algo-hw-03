

def normalize_phone(phone_number):
    if not phone_number.startswith('+38'):
        phone_number = '38' + phone_number