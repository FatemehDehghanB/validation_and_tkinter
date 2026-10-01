from persian_tools.bank import card_number
from persian_tools import phone_number , national_id , plate

def card_validator(card_num):
    if not card_number.validate(card_num):
        raise ValueError("شماره کارت معتبر نیست")
    else:
        return card_number.bank_data(card_num)

def phone_validator(phone_num):
    if not phone_number.validate(phone_num):
        raise ValueError("شماره همراه نامعتبر است")
    else:
        return phone_number.operator_data(phone_num)

def nationalid_validator(id_num):
    if not national_id.validate(id_num):
        raise ValueError("شماره ملی نامعتبر است")
    else:
        return national_id.find_place(id_num)

def plate_validator(plate_num):
    if not plate.is_valid(plate_num):
        raise ValueError("شماره پلاک نامعتبر است")
    else:
        return plate.get_info(plate_num)


