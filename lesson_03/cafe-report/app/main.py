from pathlib import Path

from app.services.orders import load_orders
from app.services.report import build_report

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "orders.csv"


def main() -> None:
    orders = load_orders(DATA_FILE)
    print(build_report(orders))


if __name__ == "__main__":
    main()
