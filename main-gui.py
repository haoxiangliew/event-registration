import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from ttkthemes import ThemedTk
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

    # Check if the extracted ID number is a valid integer
    try:
        id_number = int(id_number_str)
    except ValueError:
        raise ValueError(f"Invalid ID number format: {id_number_str}")

    return id_number


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

    # always on top
    top.attributes("-topmost", True)
    top.grab_set()
    top.focus_force()

    # message
    msg = ttk.Label(top, text=message, font=("TkDefaultFont", font_size, font_weight))
    msg.pack(padx=20, pady=20)

    # ok button
    button = ttk.Button(top, text="OK", command=top.destroy)
    button.pack(pady=10)

    # center window
    center_window(top)

    # return should dismiss
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


# GUI class
class TicketScannerApp(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_theme("yaru")

        self.title("Ticket Scanner")
        self.geometry("600x300")

        self.style = ttk.Style()
        bg_color = self.style.lookup("TFrame", "background")
        self.configure(bg=bg_color)

        self.create_widgets()

    # create widgets
    def create_widgets(self):
        # input frame
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(side=tk.TOP, pady=20, padx=40)

        # input label
        self.input_label = ttk.Label(
            self.input_frame, text="Enter an ID number:", font=("TkDefaultFont", 18)
        )
        self.input_label.pack(side=tk.TOP)

        # input entry
        self.input_entry = ttk.Entry(
            self.input_frame, font=("TkDefaultFont", 18), width=20
        )
        self.input_entry.pack(side=tk.TOP, pady=10)
        self.input_entry.focus_set()
        self.input_entry.bind("<Return>", self.process_input)  # bind enter key
        self.input_entry.bind("<Control-a>", self.select_all_input)  # bind ctrl+a

        # button frame
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(side=tk.TOP, pady=20)

        # submit button
        self.submit_button = ttk.Button(
            self.button_frame,
            text="Submit",
            command=self.process_input,
            style="TButton",
        )
        self.submit_button.pack(side=tk.LEFT, padx=10)

        # exit button
        self.exit_button = ttk.Button(
            self.button_frame,
            text="Exit",
            command=self.exit_app,
            style="TButton",
        )
        self.exit_button.pack(side=tk.LEFT, padx=10)

        # handle WM_DELETE_WINDOW
        self.protocol("WM_DELETE_WINDOW", self.exit_app)

        # style
        self.style = ttk.Style()
        self.style.configure("TButton", font=("TkDefaultFont", 18))

    # select all handler
    def select_all_input(self, event):
        self.input_entry.select_range(0, tk.END)
        self.input_entry.icursor(tk.END)
        return "break"

    # enter / submission handler
    def process_input(self, event=None):
        input_str = self.input_entry.get()
        id_number = extract_id_number(input_str)
        matching_rows = find_name_by_id(data, id_number)

        if matching_rows.empty:
            display_id_not_found_error(id_number)
        else:
            if len(matching_rows) > 1:
                if all(matching_rows["Registered"] == "Yes"):
                    multiple_names = ", ".join(matching_rows["Name"].values)
                    display_already_registered_error(multiple_names, id_number)
                else:
                    name_input = self.ask_name()
                    if name_input:
                        matching_rows = matching_rows.loc[
                            matching_rows["Name"] == name_input
                        ]

                        if matching_rows.empty:
                            messagebox.showerror(
                                "Error",
                                "No matching name found for the given ID.",
                                parent=self,
                            )
                        else:
                            self.process_row(matching_rows.iloc[0], id_number)
                    else:
                        return
            else:
                self.process_row(matching_rows.iloc[0], id_number)

        self.input_entry.delete(0, tk.END)
        self.input_entry.focus_set()

    # process row
    def process_row(self, row, id_number):
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

    # ask name
    def ask_name(self):
        name_input = simpledialog.askstring(
            "Enter Name", "Enter the name for a more accurate search", parent=self
        )
        return name_input

    # exit app
    def exit_app(self):
        if messagebox.askyesno(
            "Exit", "Do you want to exit the application?", parent=self
        ):
            self.destroy()


# main function
def main():
    global data
    global file_path

    # check if input file exists
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

    # check for duplicates
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

    # then we can run the app
    app = TicketScannerApp()
    app.mainloop()


if __name__ == "__main__":
    main()
