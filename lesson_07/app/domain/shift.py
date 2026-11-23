"""Модель рабочей смены."""

from datetime import date

from app.domain.order import Order


class Shift:
    """Хранит дату смены и список заказов."""

    def __init__(self, day: date) -> None:
        """Создаёт смену на указанную дату.

        Args:
            day: Дата рабочей смены.
        """
        self.day = day
        self.orders: list[Order] = []

    def add(self, order: Order) -> None:
        """Добавляет заказ в смену.

        Args:
            order: Заказ, который нужно добавить.
        """
        self.orders.append(order)

    def total_kopeks(self) -> int:
        """Возвращает общую сумму заказов в копейках.

        Returns:
            Сумма всех заказов в копейках.
        """
        return sum(order.kopeks for order in self.orders)
