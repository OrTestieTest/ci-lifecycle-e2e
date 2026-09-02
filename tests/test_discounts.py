import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ci_lifecycle_e2e.discounts import discount_percent, total_cents


class DiscountPercentTest(unittest.TestCase):
    def test_below_first_tier(self):
        self.assertEqual(discount_percent(0), 0)
        self.assertEqual(discount_percent(19), 0)

    def test_tier_boundaries_are_inclusive(self):
        self.assertEqual(discount_percent(20), 5)
        self.assertEqual(discount_percent(50), 10)
        self.assertEqual(discount_percent(100), 15)

    def test_inside_tiers(self):
        self.assertEqual(discount_percent(49), 5)
        self.assertEqual(discount_percent(99), 10)
        self.assertEqual(discount_percent(1000), 15)


class TotalCentsTest(unittest.TestCase):
    def test_totals_apply_the_tier_discount(self):
        self.assertEqual(total_cents(10), 1000)
        self.assertEqual(total_cents(20), 1900)
        self.assertEqual(total_cents(50), 4500)
        self.assertEqual(total_cents(100), 8500)


if __name__ == "__main__":
    unittest.main()
