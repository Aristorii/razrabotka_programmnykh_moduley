from app.services.orders import calculate_revenue
from app.utils.money import format_money


def build_report(orders: list[dict[str, str]]) -> str:
    count = len(orders)
    revenue = calculate_revenue(orders)
    average = revenue / count if count else 0
    return (
        "ОТЧЁТ ПО ЗАКАЗАМ\n"
        "----------------------------------\n"
        f"Заказов: {count}\n"
        f"Выручка: {format_money(revenue)}\n"
        f"Средний чек: {format_money(average)}"
    )
