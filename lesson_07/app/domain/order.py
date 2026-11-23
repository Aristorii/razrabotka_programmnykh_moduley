"""Модель заказа кафе."""

from dataclasses import dataclass

from app.utils.text import normalize_name


@dataclass(frozen=True)
class Order:
    """Заказ одного официанта с суммой в копейках.

    Attributes:
        waiter: Нормализованное имя официанта.
        kopeks: Сумма заказа в копейках.
    """

    waiter: str
    kopeks: int

    def __post_init__(self) -> None:
        """Проверяет сумму и нормализует имя официанта.

        Raises:
            ValueError: Если сумма заказа отрицательная.
        """
        if self.kopeks < 0:
            raise ValueError("Сумма заказа не может быть отрицательной")
        object.__setattr__(self, "waiter", normalize_name(self.waiter))
