import pandas as pd
import tkinter as tk
from tkinter import messagebox


def check_for_duplicates():
    duplicate_ids = data.duplicated(subset=["ID Number"], keep=False)
    duplicate_names = data.duplicated(subset=["Name"], keep=False)
    if duplicate_ids.any() and duplicate_names.any():
        duplicates = data[duplicate_ids | duplicate_names]
        print("Error: The following duplicate entries were found in the XLSX file:")
        print(duplicates)
        return False
    return True


def extract_id_number(input_str):
    if input_str[0] == ";":
        id_number_str = input_str[6:10]
    else:
        id_number_str = input_str
    return int(id_number_str)


def find_name_by_id(id_number):
    return data.loc[data["ID Number"] == id_number]


def mark_as_registered(row_index):
    data.at[row_index, "Registered"] = "Yes"
    data.to_excel(file_name, index=False, engine="openpyxl")


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def display_name_popup(name, id_number, tickets):
    window = tk.Tk()
    window.withdraw()
    center_window(window)
    messagebox.showinfo(
        "ID, Name, Registered Status, and Tickets",
        f"ID: {id_number}\nName: {name}\nRegistered: Yes\nTickets: {tickets}",
        parent=window,
    )
    window.destroy()


def display_already_registered_error(name, id_number):
    window = tk.Tk()
    window.withdraw()
    center_window(window)
    window.bell()
    messagebox.showerror(
        "Error",
        f"ID: {id_number}\nName: {name}\nError: Already registered!",
        parent=window,
    )
    window.destroy()


def display_id_not_found_error(id_number):
    window = tk.Tk()
    window.withdraw()
    center_window(window)
    window.bell()
    messagebox.showerror("Error", f"Cannot find ID number: {id_number}", parent=window)
    window.destroy()


# Parse the XLSX file
file_name = "input.xlsx"
data = pd.read_excel(file_name, engine="openpyxl")

# Continuously take ID number input and display the corresponding name or error popup
if check_for_duplicates():
    while True:
        try:
            input_str = input("Enter an ID number: ")
            id_number = extract_id_number(input_str)
            matching_rows = find_name_by_id(id_number)

            if not matching_rows.empty:
                if len(matching_rows) > 1:
                    # Check if all matching rows are already registered
                    if all(matching_rows["Registered"] == "Yes"):
                        multiple_names = ", ".join(matching_rows["Name"].values)
                        display_already_registered_error(multiple_names, id_number)
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
                    mark_as_registered(row_index)
            else:
                display_id_not_found_error(id_number)
        except ValueError:
            print("Invalid input. Please enter a valid ID.")
        except KeyboardInterrupt:
            print("\nExiting the program...")
            break
else:
    window = tk.Tk()
    window.withdraw()
    center_window(window)
    window.bell()
    messagebox.showerror(
        "Error",
        "Please fix the duplicate entries and restart the program.",
        parent=window,
    )
    window.destroy()
