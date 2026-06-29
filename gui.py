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
            result_label.config(text=f"Prediction: {result}", foreground="#C0392B")
        elif "Low" in result:
            result_label.config(text=f"Prediction: {result}", foreground="#2471A3")
        else:
            result_label.config(text=f"Prediction: {result}", foreground="#1E8449")

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
root.geometry("520x560")
root.configure(bg=BG_MAIN)
root.bind("<Escape>", lambda e: toggle_fullscreen() if is_fullscreen else None)

# =====================================================
# Style Configuration
# =====================================================
style = ttk.Style()
style.theme_use('clam')

style.configure("TFrame", background=BG_MAIN)
style.configure("Card.TFrame", background=BG_CARD)
style.configure("Header.TFrame", background=HEADER_BG)

style.configure("TLabel", background=BG_CARD, foreground=TEXT_DARK, font=("Segoe UI", 10))
style.configure("Header.TLabel", background=HEADER_BG, foreground="white", font=("Segoe UI", 15, "bold"))
style.configure("Sub.TLabel", background=HEADER_BG, foreground="#B9D6D2", font=("Segoe UI", 9))
style.configure("Muted.TLabel", background=BG_CARD, foreground=TEXT_MUTED, font=("Segoe UI", 11, "bold"))

style.configure("TButton", background=ACCENT_COLOR, foreground="white",
                font=("Segoe UI", 10, "bold"), padding=10, borderwidth=0)
style.map("TButton", background=[("active", ACCENT_HOVER)])

style.configure("Secondary.TButton", background=BG_CARD, foreground=ACCENT_COLOR,
                font=("Segoe UI", 9), padding=6, borderwidth=1)
style.map("Secondary.TButton", background=[("active", "#E8F3F1")])

style.configure("TCombobox", fieldbackground="white", background="white",
                arrowsize=14, padding=4)
style.configure("TEntry", fieldbackground="white", padding=4)

# =====================================================
# Header
# =====================================================
header = ttk.Frame(root, style="Header.TFrame")
header.pack(fill="x")

ttk.Label(header, text="Medicine Demand Forecaster", style="Header.TLabel").pack(
    anchor="w", padx=20, pady=(18, 2))
ttk.Label(header, text="AI-powered pharmacy inventory predictions", style="Sub.TLabel").pack(
    anchor="w", padx=20, pady=(0, 16))

# =====================================================
# Main Card
# =====================================================
card = ttk.Frame(root, style="Card.TFrame", padding=25)
card.pack(fill="both", expand=True, padx=20, pady=20)

card.columnconfigure(1, weight=1)

# --- Input Fields ---
ttk.Label(card, text="Medicine Class").grid(row=0, column=0, sticky="w", pady=(0, 6))
med_var = tk.StringVar()
med_dropdown = ttk.Combobox(card, textvariable=med_var, values=list(medicine_map.keys()),
                             state="readonly")
med_dropdown.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 16))
med_dropdown.current(0)

ttk.Label(card, text="Year (YYYY)").grid(row=2, column=0, sticky="w", pady=(0, 6))
year_var = tk.StringVar(value="2026")
year_entry = ttk.Entry(card, textvariable=year_var)
year_entry.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 16))

ttk.Label(card, text="Month").grid(row=4, column=0, sticky="w", pady=(0, 6))
month_var = tk.StringVar()
month_dropdown = ttk.Combobox(card, textvariable=month_var,
                               values=[str(i) for i in range(1, 13)], state="readonly")
month_dropdown.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, 16))
month_dropdown.current(0)

ttk.Label(card, text="Day of Week").grid(row=6, column=0, sticky="w", pady=(0, 6))
day_var = tk.StringVar()
day_dropdown = ttk.Combobox(card, textvariable=day_var, values=list(weekday_map.keys()),
                             state="readonly")
day_dropdown.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(0, 20))
day_dropdown.current(0)

# --- Separator ---
ttk.Separator(card, orient="horizontal").grid(row=8, column=0, columnspan=2, sticky="ew", pady=(0, 20))

# --- Predict Button ---
predict_btn = ttk.Button(card, text="Predict Demand", command=on_predict)
predict_btn.grid(row=9, column=0, columnspan=2, sticky="ew", ipady=4)

# --- Result Display ---
result_label = ttk.Label(card, text="Prediction: Waiting for input...", style="Muted.TLabel")
result_label.grid(row=10, column=0, columnspan=2, pady=(20, 0))


root.mainloop()