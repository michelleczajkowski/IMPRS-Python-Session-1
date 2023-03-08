import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Create root window
root = tk.Tk()

# Hide the main window
root.withdraw()

# Show file dialog to choose file
file_path = filedialog.askopenfilename(initialdir="C:/", title="Select a file", filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])

# Print the selected file path
print("Selected file:", file_path)

# Read file using Pandas
if file_path.endswith('.csv'):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

# Print file structure
print("\nFile Structure:")
print(df.head())
