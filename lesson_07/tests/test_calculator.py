"""Проверки расчётов по оценкам."""

import pytest

from app.services.calculator import calculate_average, grade_bounds


def test_average_rounds_to_two_digits() -> None:
    assert calculate_average([5, 4, 5, 3, 5]) == 4.4


def test_average_empty_raises() -> None:
    with pytest.raises(ValueError):
        calculate_average([])


def test_bounds_returns_min_then_max() -> None:
    assert grade_bounds([5, 3, 4]) == (3, 5)


def test_bounds_empty_raises() -> None:
    with pytest.raises(ValueError):
        grade_bounds([])
