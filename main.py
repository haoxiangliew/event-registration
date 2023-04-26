import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
from pathlib import Path
from enum import Enum
from typing import Union


# Ticket Categories
class TicketCategory(Enum):
    TWO_ALCOHOLIC = "2 alcoholic drink tickets"
    ONE_ALCOHOLIC_ONE_NON_ALCOHOLIC = "1 non-alcoholic drink and 1 alcoholic drink"
    TWO_NON_ALCOHOLIC = "2 non-alcoholic drink tickets"


TICKET_CATEGORIES = {
    TicketCategory.TWO_ALCOHOLIC.value: "2 Alcoholic Tickets",
    TicketCategory.ONE_ALCOHOLIC_ONE_NON_ALCOHOLIC.value: "1 Alcoholic and 1 Non-Alcoholic Tickets",
    TicketCategory.TWO_NON_ALCOHOLIC.value: "2 Non-Alcoholic Tickets",
}


# Tkinter Context Manager
class TkinterContext:
    def __init__(self):
        self.window = tk.Tk()
        self.window.withdraw()

    def __enter__(self):
        center_window(self.window)
        return self.window

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.window.destroy()


# check for duplicate entries on boot
def check_for_duplicates(data: pd.DataFrame) -> bool:
    duplicate_ids = data.duplicated(subset=["ID Number"], keep=False)
    duplicate_names = data.duplicated(subset=["Name"], keep=False)
    if duplicate_ids.any() and duplicate_names.any():
        duplicates = data[duplicate_ids | duplicate_names]
        print("Error: The following duplicate entries were found in the XLSX file:")
        print(duplicates)
        return False
    return True


# extract id number from input string
def extract_id_number(input_str: str) -> int:
    if input_str.startswith(";90") and input_str.endswith("=0249?"):
        id_number_str = input_str[6:10]
    else:
        id_number_str = input_str
    return int(id_number_str)


# find name by id number
def find_name_by_id(data: pd.DataFrame, id_number: int) -> pd.DataFrame:
    return data.loc[data["ID Number"] == id_number]


# find row index by id number and mark as registered
def mark_as_registered(data: pd.DataFrame, file_name: Path, row_index: int) -> None:
    data.at[row_index, "Registered"] = "Yes"
    data.to_excel(file_name, index=False, engine="openpyxl")


# center tkinter window
def center_window(window: Union[tk.Tk, tk.Toplevel]) -> None:
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


# get ticket category
def get_ticket_category(tickets: str) -> str:
    return TICKET_CATEGORIES.get(tickets, "Unknown Ticket Category")


# make sure ticket categories are valid
def validate_ticket_categories(data: pd.DataFrame) -> int:
    valid_categories = [category.value for category in TicketCategory]
    invalid_categories = [
        index
        for index, category in enumerate(data["Tickets"])
        if category not in valid_categories
    ]
    return invalid_categories[0] if invalid_categories else -1


# custom tkinter message box
def show_message(title, message, parent, font_size=14, font_weight="bold"):
    top = tk.Toplevel(parent)
    top.title(title)

    top.attributes("-topmost", True)

    msg = ttk.Label(top, text=message, font=("TkDefaultFont", font_size, font_weight))
    msg.pack(padx=20, pady=20)

    button = ttk.Button(top, text="OK", command=top.destroy)
    button.pack(pady=10)

    center_window(top)

    top.bind("<Return>", lambda event: top.destroy())

    parent.wait_window(top)


# display name popup
def display_name_popup(name: str, id_number: int, tickets: str) -> None:
    with TkinterContext() as window:
        ticket_category = get_ticket_category(tickets)
        show_message(
            "Info",
            f"ID: {id_number}\nName: {name}\nRegistered: Yes\n{ticket_category}",
            window,
        )


# display already registered error
def display_already_registered_error(name: str, id_number: int) -> None:
    with TkinterContext() as window:
        window.bell()
        show_message(
            "Error",
            f"ID: {id_number}\nName: {name}\nError: Already registered!",
            window,
        )


# display id not found error
def display_id_not_found_error(id_number: int) -> None:
    with TkinterContext() as window:
        window.bell()
        show_message(
            "Error",
            f"ID: {id_number}\nError: ID not found!",
            window,
        )


# main function
def main():
    # check for input file
    file_path = Path("input.xlsx")
    if not file_path.exists():
        print(f"Error: {file_path} not found!")
        return
    # read input file
    try:
        with pd.ExcelFile(file_path, engine="openpyxl") as xls:
            data = pd.read_excel(xls)
    except Exception as e:
        print(f"Error: Unable to read the Excel file. {e}")
        return

    # check for duplicate entries
    if not check_for_duplicates(data):
        with TkinterContext() as window:
            window.bell()
            messagebox.showerror(
                "Error",
                "Please fix the duplicate entries and restart the program.",
                parent=window,
            )
        return

    # check for invalid ticket categories
    invalid_category_index = validate_ticket_categories(data)
    if invalid_category_index != -1:
        print(
            f"Error: Invalid ticket category found at line {invalid_category_index + 2}. Please fix the input file."
        )
        return

    # then we can start the main loop
    while True:
        try:
            # get input
            input_str = input("Enter an ID number: ")
            id_number = extract_id_number(input_str)
            matching_rows = find_name_by_id(data, id_number)

            # check if id number is valid
            if matching_rows.empty:
                display_id_not_found_error(id_number)
            else:
                # check if id number is already registered
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

                # lookup name and display popup
                row = matching_rows.iloc[0]
                row_index, name, registered, tickets = (
                    row.name,
                    row["Name"],
                    row["Registered"],
                    row["Tickets"],
                )

                # check if already registered, if not then register
                if registered != "Yes":
                    display_name_popup(name, id_number, tickets)
                    mark_as_registered(data, file_path, row_index)
                else:
                    display_already_registered_error(name, id_number)

        # exception handling
        except ValueError:
            print("Invalid input. Please enter a valid ID.")
        except KeyboardInterrupt:
            print("\nExiting the program...")
            break


if __name__ == "__main__":
    main()
