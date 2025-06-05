def filter_by_state(list_bank_dictionary: list, state: str="EXECUTED")->list:
    """Эта функция предназначена для фильтрации словаря"""
    filtered_list = []
    for i in list_bank_dictionary:
        if i["state"] == state:
            filtered_list.append(i)

    return filtered_list


def sort_by_date(list_bank_dictionary:list, reverse:bool=True)-> list:
    """Эта функция предназначена для сортировки словаря"""
    sorted_bank_dictionary = sorted(list_bank_dictionary, key=lambda i: i["date"], reverse=reverse)
    return sorted_bank_dictionary


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="CANCELED",
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
