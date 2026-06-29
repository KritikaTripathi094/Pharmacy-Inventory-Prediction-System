import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os


# =====================================================
# Color Palette (Professional Slate/Teal theme)
# =====================================================
BG_MAIN = "#F4F6F7"        # app background - soft neutral grey
BG_CARD = "#FFFFFF"        # card/panel background
HEADER_BG = "#0F4C5C"      # deep slate teal header
TEXT_DARK = "#1B2B34"      # near-black for body text
TEXT_MUTED = "#5E6B6E"     # muted grey for secondary text
ACCENT_COLOR = "#0F9B8E"   # teal accent for primary actions
ACCENT_HOVER = "#0C7C72"   # darker teal for hover/active
BORDER_COLOR = "#D6DEE0"
print("=== RUNNING THE UPDATED SCRIPT ===")

# Ensuring the 'src' directory is in the system path so we can import predict.py
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from predict import predict_demand, medicine_map, weekday_map

# =====================================================
# Core Prediction Trigger
# =====================================================
def on_predict():
    try:
        med = med_var.get()
        year = int(year_var.get())
        month = int(month_var.get())
        day = day_var.get()

        if year < 2000 or year > 2100:
            raise ValueError("Please enter a realistic year (e.g., 2026).")

        result = predict_demand(med, year, month, day)

        if "High" in result:
            result_label.config(text=f"Prediction: {result}", foreground="red")
        elif "Low" in result:
            result_label.config(text=f"Prediction: {result}", foreground="blue")
        else:
            result_label.config(text=f"Prediction: {result}", foreground="green")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# =====================================================
# Fullscreen Toggle
# =====================================================
is_fullscreen = False

def toggle_fullscreen():
    global is_fullscreen
    if not is_fullscreen:
        root.state("zoomed")
    else:
        root.state("normal")
    is_fullscreen = not is_fullscreen

# =====================================================
# Window Setup
# =====================================================
root = tk.Tk()
root.title("Pharmacy Inventory AI - Demand Predictor")

# START SMALL - no zoomed call here
root.geometry("500x450")
root.configure(bg=BG_MAIN)

# Escape key only exits fullscreen if currently fullscreen
root.bind("<Escape>", lambda e: toggle_fullscreen() if is_fullscreen else None)

# Styling layout
style = ttk.Style()
style.theme_use('clam')

style.theme_use('clam')

# Applying custom color scheme to all ttk widgets
style.configure("TFrame", background=BG_MAIN)
style.configure("TLabel", background=BG_MAIN, foreground=TEXT_DARK)
style.configure("TButton", background=ACCENT_COLOR, foreground="white", padding=6)
style.map("TButton", background=[("active", TEXT_DARK)])
style.configure("TCombobox", fieldbackground="white", background=BG_CARD)
style.configure("TEntry", fieldbackground="white")

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Title Label
title_label = ttk.Label(main_frame, text="Medicine Demand Forecaster", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# =====================================================
# Input Fields
# =====================================================
ttk.Label(main_frame, text="Select Medicine Class:", font=("Arial", 11)).grid(row=1, column=0, sticky=tk.W, pady=10)
med_var = tk.StringVar()
med_dropdown = ttk.Combobox(main_frame, textvariable=med_var, values=list(medicine_map.keys()), state="readonly", width=25)
med_dropdown.grid(row=1, column=1, pady=10)
med_dropdown.current(0)

ttk.Label(main_frame, text="Enter Year (YYYY):", font=("Arial", 11)).grid(row=2, column=0, sticky=tk.W, pady=10)
year_var = tk.StringVar(value="2026")
year_entry = ttk.Entry(main_frame, textvariable=year_var, width=27)
year_entry.grid(row=2, column=1, pady=10)

ttk.Label(main_frame, text="Select Month:", font=("Arial", 11)).grid(row=3, column=0, sticky=tk.W, pady=10)
month_var = tk.StringVar()
month_dropdown = ttk.Combobox(main_frame, textvariable=month_var, values=[str(i) for i in range(1, 13)], state="readonly", width=25)
month_dropdown.grid(row=3, column=1, pady=10)
month_dropdown.current(0)

ttk.Label(main_frame, text="Select Day of Week:", font=("Arial", 11)).grid(row=4, column=0, sticky=tk.W, pady=10)
day_var = tk.StringVar()
day_dropdown = ttk.Combobox(main_frame, textvariable=day_var, values=list(weekday_map.keys()), state="readonly", width=25)
day_dropdown.grid(row=4, column=1, pady=10)
day_dropdown.current(0)

# =====================================================
# Execution & Output Elements
# =====================================================
predict_btn = ttk.Button(main_frame, text="Predict Demand", command=on_predict)
predict_btn.grid(row=5, column=0, columnspan=2, pady=20)




result_label = ttk.Label(main_frame, text="Prediction: Waiting for input...", font=("Arial", 13, "bold"), foreground="gray")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()