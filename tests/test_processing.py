import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.mark.parametrize(
    "my_list, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state(my_list, result):
    assert filter_by_state(my_list) == result


@pytest.mark.parametrize(
    "my_list, state, result",
    [
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "CANCELED", []),
        (
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            "CANCELED",
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
        ),
    ],
)
def test_filter_by_different_state(my_list, state, result):
    assert filter_by_state(my_list, state) == result


# sort_by_date
@pytest.mark.parametrize(
    "my_list, is_reverse, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(my_list, is_reverse, result):
    assert sort_by_date(my_list, is_reverse) == result


@pytest.mark.parametrize(
    "my_list, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_same_date(my_list, result):
    assert sort_by_date(my_list) == result


@pytest.mark.parametrize(
    "my_list, result",
    [
        (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T08:58.425572"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-раарпарап30T02:08:58.425572"},
            ],
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-раарпарап30T02:08:58.425572"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T08:58.425572"},
            ],
        )
    ],
)
def test_sort_error_date(my_list, result):
    assert sort_by_date(my_list) == result


def test_process_bank_search():
    # фиктивные данные
    transactions = [
        {
            "id": 1,
            "description": "Оплата продуктов",
            "state": "EXECUTED",
            "date": "2026-01-16T12:00:00",
            "operationAmount": {"amount": "100", "currency": {"name": "рубль", "code": "RUB"}},
        },
        {
            "id": 2,
            "description": "Покупка одежды",
            "state": "EXECUTED",
            "date": "2026-01-15T12:00:00",
            "operationAmount": {"amount": "200", "currency": {"name": "рубль", "code": "RUB"}},
        },
        {
            "id": 3,
            "description": "Оплата такси",
            "state": "EXECUTED",
            "date": "2026-01-14T12:00:00",
            "operationAmount": {"amount": "150", "currency": {"name": "рубль", "code": "RUB"}},
        },
    ]

    # ищем транзакции, где есть слово "Оплата"
    result = process_bank_search(transactions, "Оплата")

    # проверяем, что вернулись только нужные транзакции
    assert len(result) == 2
    assert all("Оплата" in t["description"] for t in result)
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

    # ищем слово, которого нет
    empty_result = process_bank_search(transactions, "Кафе")
    assert empty_result == []

    # проверяем, что функция не падает на некорректные данные
    bad_result = process_bank_search("не список", "Оплата")
    assert bad_result == []


def test_process_bank_operations():
    # фиктивные данные
    transactions = [
        {"id": 1, "description": "food"},
        {"id": 2, "description": "taxi"},
        {"id": 3, "description": "food"},
        {"id": 4, "description": "shopping"},
        {"id": 5, "description": "food"},
    ]

    categories = ["food", "taxi", "shopping", "entertainment"]

    result = process_bank_operations(transactions, categories)

    assert isinstance(result, dict)
    assert result["food"] == 3
    assert result["taxi"] == 1
    assert result["shopping"] == 1
    # категория, которой нет в данных, должна быть 0
    assert result["entertainment"] == 0

    bad_result = process_bank_operations("не список", categories)
    assert bad_result == {}
