from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_account_card: str) -> str:
    """Эта функция для счета и карты и названия"""
    if "Счет" in type_account_card:
        return get_mask_account(type_account_card)
    else:
        return get_mask_card_number(type_account_card)


print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))


def get_date(data_str: str) -> str:
    """Эта функция вазвращает дату в заданном формате"""
    modified_data = data_str[8:10] + "." + data_str[5:7] + "." + data_str[0:4]
    return modified_data


print(get_date("2024-03-11T02:26:18.671407"))

if __name__ == "__main__":
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))