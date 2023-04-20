import unittest
import pandas as pd

from main import (
    extract_id_number,
    find_name_by_id,
    check_for_duplicates,
    get_ticket_category,
    validate_ticket_categories,
)


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame(
            {
                "ID Number": [1000, 1001, 1002, 1001],
                "Name": ["John Doe", "Jane Smith", "Alice", "Jane Smith"],
                "Registered": ["No", "Yes", "No", "No"],
                "Tickets": [
                    "2 alcoholic drink tickets",
                    "1 non-alcoholic drink and 1 alcoholic drink",
                    "2 non-alcoholic drink tickets",
                    "1 non-alcoholic drink and 1 alcoholic drink",
                ],
            }
        )

    def test_extract_id_number(self):
        self.assertEqual(extract_id_number(";123809871"), 9871)
        self.assertEqual(extract_id_number("1001"), 1001)

    def test_find_name_by_id(self):
        self.assertEqual(len(find_name_by_id(self.data, 1000)), 1)
        self.assertEqual(len(find_name_by_id(self.data, 1001)), 2)
        self.assertTrue(find_name_by_id(self.data, 9999).empty)

    def test_check_for_duplicates(self):
        self.assertFalse(check_for_duplicates(self.data))

        unique_data = self.data.drop_duplicates(
            subset=["ID Number", "Name"], keep=False
        )
        self.assertTrue(check_for_duplicates(unique_data))

    def test_get_ticket_category(self):
        self.assertEqual(
            get_ticket_category("2 alcoholic drink tickets"), "2 Alcoholic Tickets"
        )
        self.assertEqual(
            get_ticket_category("1 non-alcoholic drink and 1 alcoholic drink"),
            "1 Alcoholic and 1 Non-Alcoholic Tickets",
        )
        self.assertEqual(
            get_ticket_category("2 non-alcoholic drink tickets"),
            "2 Non-Alcoholic Tickets",
        )
        self.assertEqual(get_ticket_category("unknown"), "Unknown Ticket Category")

    def test_validate_ticket_categories(self):
        self.assertEqual(validate_ticket_categories(self.data), -1)

        invalid_data = self.data.copy()
        invalid_data.at[0, "Tickets"] = "invalid_ticket_category"
        self.assertEqual(validate_ticket_categories(invalid_data), 0)


if __name__ == "__main__":
    unittest.main()
