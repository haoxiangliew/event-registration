import unittest
import pandas as pd
import tkinter as tk
from tkinter import messagebox

import re


class TkinterContext:
    def __init__(self):
        self.window = tk.Tk()
        self.window.withdraw()

    def __enter__(self):
        return self.window

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.window.destroy()


from main import (
    center_window,
    check_for_duplicates,
    extract_id_number,
    find_name_by_id,
    get_ticket_category,
    mark_as_registered,
    validate_ticket_categories,
    display_already_registered_error,
    display_id_not_found_error,
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

    def test_mark_as_registered(self):
        data_copy = self.data.copy()
        test_file_name = "test_output.xlsx"
        mark_as_registered(data_copy, test_file_name, 0)
        self.assertEqual(data_copy.at[0, "Registered"], "Yes")

    def test_center_window(self):
        window = tk.Tk()
        window.geometry("300x200")
        center_window(window)
        width, height, x, y = [
            int(value) for value in re.findall(r"\d+", window.geometry())
        ]
        self.assertEqual(width, 300)
        self.assertEqual(height, 200)
        self.assertEqual(x, (window.winfo_screenwidth() // 2) - (width // 2))
        self.assertEqual(y, (window.winfo_screenheight() // 2) - (height // 2))
        window.destroy()

    def test_find_name_by_id_multiple_results(self):
        data_with_duplicates = pd.concat(
            [
                self.data,
                pd.DataFrame(
                    {
                        "ID Number": [1001],
                        "Name": ["Jane Smith"],
                        "Registered": ["No"],
                        "Tickets": ["2 alcoholic drink tickets"],
                    }
                ),
            ],
            ignore_index=True,
        )

        matching_rows = find_name_by_id(data_with_duplicates, 1001)
        self.assertEqual(len(matching_rows), 3)

    def test_find_name_by_id_no_results(self):
        data_with_no_matching_id = self.data[self.data["ID Number"] != 1000]
        matching_rows = find_name_by_id(data_with_no_matching_id, 1000)
        self.assertTrue(matching_rows.empty)

    def test_extract_id_number_invalid_input(self):
        self.assertRaises(ValueError, extract_id_number, "abc")

    def test_validate_ticket_categories_invalid_categories(self):
        data_with_invalid_categories = pd.DataFrame(
            {
                "ID Number": [1000, 1001],
                "Name": ["John Doe", "Jane Smith"],
                "Registered": ["No", "Yes"],
                "Tickets": ["invalid category", "3 alcoholic drink tickets"],
            }
        )
        self.assertEqual(validate_ticket_categories(data_with_invalid_categories), 0)

    def test_get_ticket_category_unknown_ticket_category(self):
        self.assertEqual(
            get_ticket_category("invalid ticket category"), "Unknown Ticket Category"
        )

    def test_get_ticket_category_unsupported_ticket_category(self):
        self.assertEqual(
            get_ticket_category("1 alcoholic drink"), "Unknown Ticket Category"
        )

    def test_display_id_not_found_error(self):
        with self.assertRaises(tk.TclError):
            display_id_not_found_error(1234)

    def test_validate_ticket_categories_invalid(self):
        data = pd.DataFrame(
            {
                "ID Number": [1000, 1001, 1002],
                "Name": ["John Doe", "Jane Smith", "Alice"],
                "Registered": ["No", "Yes", "No"],
                "Tickets": [
                    "invalid",
                    "2 alcoholic drink tickets",
                    "2 non-alcoholic drink tickets",
                ],
            }
        )
        self.assertEqual(validate_ticket_categories(data), 0)

    def test_get_ticket_category_unknown(self):
        self.assertEqual(get_ticket_category("unknown"), "Unknown Ticket Category")

    def display_already_registered_error(self, name, id_number):
        window = tk.Tk()
        try:
            center_window(window)
            window.bell()
            messagebox.showerror(
                "Error",
                f"ID: {id_number}\nName: {name}\nError: Already registered!",
                parent=window,
            )
        finally:
            window.destroy()

    def test_extract_id_number_no_input(self):
        with self.assertRaises(IndexError):
            extract_id_number("")

    def test_extract_id_number_5_digits(self):
        self.assertEqual(extract_id_number("12345"), 12345)


if __name__ == "__main__":
    unittest.main()
