import unittest
from app.services.orders import calculate_revenue, order_total


class OrdersTests(unittest.TestCase):
    def test_order_total(self):
        self.assertEqual(order_total({"quantity": "2", "price": "10"}), 20)

    def test_revenue(self):
        orders = [{"quantity": "2", "price": "10"}, {"quantity": "1", "price": "5"}]
        self.assertEqual(calculate_revenue(orders), 25)

    def test_empty_revenue(self):
        self.assertEqual(calculate_revenue([]), 0)
