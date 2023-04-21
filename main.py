import pandas as pd
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from enum import Enum


class TicketCategory(Enum):
    TWO_ALCOHOLIC = "2 alcoholic drink tickets"
    ONE_ALCOHOLIC_ONE_NON_ALCOHOLIC = "1 non-alcoholic drink and 1 alcoholic drink"
    TWO_NON_ALCOHOLIC = "2 non-alcoholic drink tickets"


class TkinterContext:
    def __init__(self):
        self.window = tk.Tk()
        self.window.withdraw()

    def __enter__(self):
        center_window(self.window)
        return self.window

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.window.destroy()


def check_for_duplicates(data: pd.DataFrame) -> bool:
    duplicate_ids = data.duplicated(subset=["ID Number"], keep=False)
    duplicate_names = data.duplicated(subset=["Name"], keep=False)
    if duplicate_ids.any() and duplicate_names.any():
        duplicates = data[duplicate_ids | duplicate_names]
        print("Error: The following duplicate entries were found in the XLSX file:")
        print(duplicates)
        return False
    return True


def extract_id_number(input_str: str) -> int:
    if input_str[0] == ";":
        id_number_str = input_str[6:10]
    else:
        id_number_str = input_str
    return int(id_number_str)


def find_name_by_id(data: pd.DataFrame, id_number: int) -> pd.DataFrame:
    return data.loc[data["ID Number"] == id_number]


def mark_as_registered(data: pd.DataFrame, file_name: Path, row_index: int) -> None:
    data.at[row_index, "Registered"] = "Yes"
    data.to_excel(file_name, index=False, engine="openpyxl")


def center_window(window: tk.Tk) -> None:
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def get_ticket_category(tickets: str) -> str:
    ticket_categories = {
        TicketCategory.TWO_ALCOHOLIC.value: "2 Alcoholic Tickets",
        TicketCategory.ONE_ALCOHOLIC_ONE_NON_ALCOHOLIC.value: "1 Alcoholic and 1 Non-Alcoholic Tickets",
        TicketCategory.TWO_NON_ALCOHOLIC.value: "2 Non-Alcoholic Tickets",
    }
    return ticket_categories.get(tickets, "Unknown Ticket Category")


def validate_ticket_categories(data: pd.DataFrame) -> int:
    valid_categories = [category.value for category in TicketCategory]
    ticket_enum = enumerate(data["Tickets"])
    for index, category in ticket_enum:
        if category not in valid_categories:
            return index
    return -1


def display_name_popup(name: str, id_number: int, tickets: str) -> None:
    with TkinterContext() as window:
        ticket_category = get_ticket_category(tickets)
        messagebox.showinfo(
            "Info",
            f"ID: {id_number}\nName: {name}\nRegistered: Yes\n{ticket_category}",
            parent=window,
        )


def display_already_registered_error(name: str, id_number: int) -> None:
    with TkinterContext() as window:
        window.bell()
        messagebox.showerror(
            "Error",
            f"ID: {id_number}\nName: {name}\nError: Already registered!",
            parent=window,
        )


def display_id_not_found_error(id_number: int) -> None:
    with TkinterContext() as window:
        window.bell()
        messagebox.showerror(
            "Error",
            f"ID: {id_number}\nError: ID not found!",
            parent=window,
        )


def main():
    file_path = Path("input.xlsx")
    if not file_path.exists():
        print(f"Error: {file_path} not found!")
        return
    try:
        with pd.ExcelFile(file_path, engine="openpyxl") as xls:
            data = pd.read_excel(xls)
    except Exception as e:
        print(f"Error: Unable to read the Excel file. {e}")
        return

    if not check_for_duplicates(data):
        with TkinterContext() as window:
            window.bell()
            messagebox.showerror(
                "Error",
                "Please fix the duplicate entries and restart the program.",
                parent=window,
            )
        return

    invalid_category_index = validate_ticket_categories(data)
    if invalid_category_index != -1:
        print(
            f"Error: Invalid ticket category found at line {invalid_category_index + 2}. Please fix the input file."
        )
        return

    while True:
        try:
            input_str = input("Enter an ID number: ")
            id_number = extract_id_number(input_str)
            matching_rows = find_name_by_id(data, id_number)

            if matching_rows.empty:
                display_id_not_found_error(id_number)
            else:
                if len(matching_rows) > 1:
                    if all(matching_rows["Registered"] == "Yes"):
                        multiple_names = ", ".join(matching_rows["Name"].values)
                        display_already_registered_error(multiple_names, id_number)
                        continue
                    else:
                        print(
                            "Duplicate ID found. Please enter the name for a more accurate search."
                        )
                        name_input = input("Enter the name: ")
                        matching_rows = matching_rows.loc[
                            matching_rows["Name"] == name_input
                        ]

                        if matching_rows.empty:
                            print("No matching name found for the given ID.")
                            continue

                row = matching_rows.iloc[0]
                row_index, name, registered, tickets = (
                    row.name,
                    row["Name"],
                    row["Registered"],
                    row["Tickets"],
                )

                if registered != "Yes":
                    display_name_popup(name, id_number, tickets)
                    mark_as_registered(data, file_path, row_index)
                else:
                    display_already_registered_error(name, id_number)

        except ValueError:
            print("Invalid input. Please enter a valid ID.")
        except KeyboardInterrupt:
            print("\nExiting the program...")
            break


if __name__ == "__main__":
    main()
