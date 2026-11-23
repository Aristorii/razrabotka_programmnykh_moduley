"""Примеры корректных вызовов для проверки типов."""

from app.utils.formatter import format_kopeks, format_title
from app.utils.text import normalize_name

title = format_title(" Итог ")
price = format_kopeks(125000)
waiter = normalize_name("Иван")
print(title)
print(price)
print(waiter)
