def get_mask_card_number(card_number: str) -> str:
    """Эта функция возвращает замаскированный номер карты"""
    mask = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:]
    return mask


card_number = str(input())
print(get_mask_card_number(card_number))


def get_mask_account(account_number: str) -> str:
    """Эта функция возвращает замаскированный номер счета"""
    mask_account = "**" + account_number[-4:]
    return mask_account


account_number = str(input())
print(get_mask_account(account_number))
