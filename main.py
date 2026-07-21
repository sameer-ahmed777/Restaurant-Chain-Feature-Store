import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load Excel File
df = pd.read_excel(
    "Restaurant_Chain_Feature_Store.xlsx"
)

# Create Main Window
root = tk.Tk()

root.title("Restaurant Dashboard")
root.geometry("1200x700")

# Heading
heading = tk.Label(
    root,
    text="Restaurant Feature Explorer Dashboard",
    font=("Arial", 20, "bold")
)

heading.pack(pady=10)

# Create Frame for Table
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Scrollbar
scroll_y = ttk.Scrollbar(frame)
scroll_y.pack(side="right", fill="y")

# Table
tree = ttk.Treeview(
    frame,
    yscrollcommand=scroll_y.set
)

scroll_y.config(command=tree.yview)

tree["columns"] = list(df.columns)
tree["show"] = "headings"

# Column Headings
for col in df.columns:

    tree.heading(col, text=col)

    tree.column(
        col,
        width=120
    )

# Insert Data
for _, row in df.head(100).iterrows():

    tree.insert(
        "",
        "end",
        values=list(row)
    )

tree.pack(
    fill="both",
    expand=True
)

root.mainloop()