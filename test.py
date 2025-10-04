# test.py
from lib import count_common_elements


def test_count_common_elements():
    # Тест 1: Общие элементы в трёх списках
    assert count_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]) == 1  # только 3

    # Тест 2: Нет общих элементов
    assert count_common_elements([1, 2], [3, 4], [5, 6]) == 0



if __name__ == "__main__":
    test_count_common_elements()