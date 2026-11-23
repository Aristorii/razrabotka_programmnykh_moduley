"""Чтение строк заказов из CSV-файлов."""

import csv
from collections.abc import Iterator
from pathlib import Path


def read_rows(path: Path) -> Iterator[dict[str, str]]:
    """Последовательно читает строки CSV-файла.

    Args:
        path: Путь к CSV-файлу.

    Yields:
        Словари, где ключи соответствуют заголовкам столбцов.
    """
    with open(path, encoding="utf-8", newline="") as file:
        yield from csv.DictReader(file)
