import unittest
from app.services.report import build_report


class ReportTests(unittest.TestCase):
    def test_report_contains_count(self):
        report = build_report([{"quantity": "1", "price": "10"}])
        self.assertIn("Заказов: 1", report)

    def test_report_contains_revenue(self):
        report = build_report([{"quantity": "2", "price": "10"}])
        self.assertIn("Выручка: 20,00 ₽", report)

    def test_empty_report(self):
        report = build_report([])
        self.assertIn("Заказов: 0", report)
