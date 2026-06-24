import csv
import os
from unittest import TestCase

from src.main import get_dpp

assets = os.path.join(os.path.dirname(__file__), "assets")


class TestGetDpp(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._assets = os.path.join(assets, "test_data.csv")
        with open(cls._assets, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            cls.data = list(reader)

    def test_get_dpp_invalid_ddr_type(self):
        with self.assertRaises(ValueError):
            get_dpp("INVALID_TYPE", 24, 16)

    def test_get_dpp_from_csv(self):
        for row in self.data:
            with self.subTest(isn=row["Isn"], vendor_pn=row["Vendor Pn"]):
                ddr_type = row["Module Type"].strip()
                module_density = float(row["Module Density"].strip())
                die_density = float(row["Die Density"].strip())
                expected_dpp = row["Dpp"].strip()
                result = get_dpp(ddr_type, module_density, die_density)
                self.assertEqual(result, expected_dpp)


if __name__ == "__main__":
    import unittest

    unittest.main()
