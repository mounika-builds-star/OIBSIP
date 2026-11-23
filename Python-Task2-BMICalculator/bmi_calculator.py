# ============================================================
# HealthMate - BMI Calculator (Clean Version - No Emojis)
# Project: Oasis Infobyte | Python Internship - Task 2
# Developed By: Mounika
# This version has NO emojis, so it works perfectly in Pydroid
# ============================================================

import tkinter as tk
from tkinter import messagebox

# ------------------------------------------------------------
# 1. MAIN WINDOW SETUP
# -----------------------------------------------------------
app = tk.Tk()
app.title("HealthMate - BMI Calculator | By Mounika")
app.geometry("420x730")
app.config(bg="#F8F9FF")
app.resizable(False, False)

# ------------------------------------------------------------
# 2. TOP HEADER SECTION (Purple)
# ------------------------------------------------------------
header = tk.Frame(app, bg="#7C3AED", height=130)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(header, text="HealthMate", font=("Arial", 26, "bold"), bg="#7C3AED", fg="white").pack(pady=(15, 0))
tk.Label(header, text="Know Your Body - Stay Healthy", font=("Arial", 11), bg="#7C3AED", fg="#DDD6FE").pack()
tk.Label(header, text="By Mounika | OIBSIP", font=("Arial", 9, "bold"), bg="#7C3AED", fg="white").pack(pady=(4, 0))


# 3. MAIN WHITE CARD

card = tk.Frame(app, bg="white", padx=22, pady=15)
card.pack(padx=20, pady=15, fill="x")

# Helper function to create labels
def create_label(text):
    return tk.Label(card, text=text, font=("Arial", 11, "bold"), bg="white", fg="#1F2937", anchor="w")

# Helper function to create entry boxes
def create_entry():
    entry = tk.Entry(card, font=("Arial", 14), bg="#EDE9FE", relief="flat", justify="center", fg="#111827")
    entry.pack(fill="x", ipady=9, pady=(2, 8))
    return entry

# 4. INPUT FIELDS - NAME, WEIGHT, HEIGHT

create_label("YOUR NAME").pack(fill="x")
name_entry = create_entry()

create_label("WEIGHT (in kg)").pack(fill="x")
weight_entry = create_entry()

create_label("HEIGHT (in cm)").pack(fill="x")
height_entry = create_entry()

# ------------------------------------------------------------
# 5. GENDER SELECTION - BOY / GIRL OPTION
# ------------------------------------------------------------
create_label("SELECT GENDER").pack(fill="x", pady=(2, 5))

gender_var = tk.StringVar(value="Girl")

gender_frame = tk.Frame(card, bg="white")
gender_frame.pack(fill="x", pady=(0, 5))

# Boy Button - Blue Style
boy_radio = tk.Radiobutton(
    gender_frame, text="BOY", variable=gender_var, value="Boy",
    font=("Arial", 12, "bold"), bg="#DBEAFE", fg="#1D4ED8",
    selectcolor="#BFDBFE", indicatoron=False, width=12, pady=8, cursor="hand2"
)
boy_radio.pack(side="left", padx=(0, 10), fill="x", expand=True)

# Girl Button - Pink Style
girl_radio = tk.Radiobutton(
    gender_frame, text="GIRL", variable=gender_var, value="Girl",
    font=("Arial", 12, "bold"), bg="#FCE7F3", fg="#BE185D",
    selectcolor="#FBCFE8", indicatoron=False, width=12, pady=8, cursor="hand2"
)
girl_radio.pack(side="left", fill="x", expand=True)

# ------------------------------------------------------------
# 6. BMI METER BAR
# ------------------------------------------------------------
tk.Label(card, text="YOUR BMI METER", font=("Arial", 10, "bold"), bg="white", fg="#9CA3AF").pack(pady=(8, 5))

meter_bg = tk.Frame(card, bg="#E5E7EB", height=16)
meter_bg.pack(fill="x")
meter_bg.pack_propagate(False)

meter_fill = tk.Frame(meter_bg, bg="#7C3AED", width=10)
meter_fill.pack(side="left", fill="y")

# ------------------------------------------------------------
# 7. RESULT DISPLAY AREA
# ------------------------------------------------------------
result_big = tk.Label(card, text="--", font=("Arial", 36, "bold"), bg="white", fg="#7C3AED")
result_big.pack(pady=(8, 0))

result_category = tk.Label(card, text="Enter details to see magic", font=("Arial", 13, "bold"), bg="white", fg="#6B7280", wraplength=320)
result_category.pack()

result_tip = tk.Label(card, text="", font=("Arial", 11), bg="white", fg="#4B5563", wraplength=320, justify="center")
result_tip.pack(pady=(5, 0))

result_ideal = tk.Label(card, text="", font=("Arial", 11, "bold"), bg="white", fg="#7C3AED")
result_ideal.pack(pady=(5, 0))

# ------------------------------------------------------------
# 8. CALCULATE FUNCTION - MAIN LOGIC
# ------------------------------------------------------------
def calculate_bmi():
    try:
        # Get user inputs
        name = name_entry.get().strip().title() or "Friend"
        gender = gender_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Validation for positive numbers
        if weight <= 0 or height <= 0:
            messagebox.showwarning("Oops!", "Please enter positive numbers!")
            return

        # BMI Formula: Weight / (Height in meters)^2
        height_m = height / 100
        bmi = round(weight / (height_m * height_m), 2)

        # Ideal weight range calculation
        min_weight = round(18.5 * height_m * height_m, 1)
        max_weight = round(24.9 * height_m * height_m, 1)

        # Gender based greeting
        title_word = "Handsome Boy" if gender == "Boy" else "Beautiful Girl"

        # Decide category, color and health tip based on BMI
        if bmi < 18.5:
            category = "Underweight"
            color = "#3B82F6"
            tip = "You are a little weak. Eat more protein, milk, eggs and dry fruits. You can do it!"
        elif bmi < 24.9:
            category = "Perfectly Healthy"
            color = "#10B981"
            tip = f"Wow {name}! You are a {title_word} and in perfect shape. Keep it up, proud of you!"
        elif bmi < 29.9:
            category = "Little Overweight"
            color = "#F59E0B"
            tip = "Need little workout. Daily 30 mins walking / dance and avoid junk food."
        else:
            category = "Need Care"
            color = "#EF4444"
            tip = "Please focus on health. Start daily walking and consult a doctor. You can do it!"

        # Update UI with results and colors
        result_big.config(text=f"{bmi}", fg=color)
        result_category.config(text=f"{name}, You are {category}", fg=color)
        result_tip.config(text=tip)
        result_ideal.config(text=f"Ideal Weight: {min_weight} kg - {max_weight} kg | Gender: {gender}")

        # Update BMI Meter width (Scale 15 to 40)
        meter_width = int(((bmi - 15) / (40 - 15)) * 340)
        meter_width = max(10, min(340, meter_width))
        meter_fill.config(bg=color, width=meter_width)

    except ValueError:
        # If user enters letters instead of numbers
        messagebox.showerror("Error", "Please enter numbers only!")

# ------------------------------------------------------------
# 9. BUTTONS - CALCULATE AND CLEAR
# ------------------------------------------------------------
button_frame = tk.Frame(app, bg="#F8F9FF")
button_frame.pack(fill="x", padx=20)

# Calculate Button
calc_button = tk.Button(
    button_frame, text="CHECK MY BMI",
    font=("Arial", 15, "bold"), bg="#7C3AED", fg="white",
    relief="flat", cursor="hand2", command=calculate_bmi
)
calc_button.pack(fill="x", ipady=12)

# Clear Function to reset all fields
def clear_all():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    gender_var.set("Girl")
    result_big.config(text="--", fg="#7C3AED")
    result_category.config(text="Enter details to see magic", fg="#6B7280")
    result_tip.config(text="")
    result_ideal.config(text="")
    meter_fill.config(bg="#7C3AED", width=10)

# Clear Button
clear_button = tk.Button(
    button_frame, text="Clear & Try Again",
    font=("Arial", 11), bg="white", fg="#7C3AED",
    relief="flat", cursor="hand2", command=clear_all
)
clear_button.pack(pady=10)

# Footer
tk.Label(app, text="Made by Mounika", font=("Arial", 10), bg="#F8F9FF", fg="#9CA3AF").pack(pady=5)

# ------------------------------------------------------------
# 10. RUN THE APP
# ------------------------------------------------------------
app.mainloop()
