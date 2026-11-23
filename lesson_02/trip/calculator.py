def calculate_total(expenses):
    """Возвращает общую сумму расходов."""
    return sum(expenses)


def calculate_average(expenses):
    """Возвращает среднюю сумму расхода."""
    if not expenses:
        return 0
    return calculate_total(expenses) / len(expenses)
