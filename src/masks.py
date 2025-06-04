def get_mask_card_number(card_number: str) -> str:
    """Эта функция возвращает замаскированный номер карты"""
    mask = (
        card_number[:-17]
        + " "
        + card_number[-17:-12]
        + " "
        + card_number[-12:-10]
        + "**"
        + " "
        + "****"
        + " "
        + card_number[-4:]
    )
    return mask


def get_mask_account(account_number: str) -> str:
    """Эта функция возвращает замаскированный номер счета"""
    mask_account = "Счет" + " " + "**" + account_number[-4:]
    return mask_account


if __name__ == "__main__":
    card_number = str("Visa Classic 6831982476737658")
    print(get_mask_card_number(card_number))
    account_number = "Счет 73654108430135874305"
    print(get_mask_account(account_number))


