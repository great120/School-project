import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
from tkinter import Label
import requests

def basic_calculation():
    for widget in root.winfo_children():
        widget.pack_forget()

    # Create the calculator frame
    calc_frame = tk.Frame(background="grey")
    calc_frame.pack(expand=True)
     # Remove home page

    # Display a title label for the calculator
    title_label = tk.Label(calc_frame, text="Basic Calculator", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=4, pady=10)

    # Entry widget to display calculations
    calc_entry = ttk.Entry(calc_frame, justify="right", font=("Arial", 18))
    calc_entry.grid(row=1, column=0, columnspan=4, ipadx=5, ipady=10, padx=10, pady=10, sticky="ew")

    # Function to update the entry widget with button text
    def click(event):
        current = calc_entry.get()
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(current)
                calc_entry.delete(0, tk.END)
                calc_entry.insert(tk.END, str(result))
            except Exception as e:
                calc_entry.delete(0, tk.END)
                calc_entry.insert(tk.END, "Error")
        elif text == "C":
            calc_entry.delete(0, tk.END)
        else:
            calc_entry.insert(tk.END, text)

    # Keypad layout in grid form
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "C", "0", "=", "+"
    ]

    # Create keypad buttons using grid layout
    row, col = 2, 0  # Starting row index is 2 to leave space for title and entry
    for button in buttons:
        btn = ttk.Button(calc_frame, text=button, style="TButton")
        btn.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", click)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Make the grid layout responsive
    for i in range(4):
        calc_frame.columnconfigure(i, weight=1)
    for i in range(5):
        calc_frame.rowconfigure(i, weight=1)

def calculate_area(shape):
    # Dictionary to store formulas and required dimensions for each shape
    if shape == "Circle":
        radius = float(simpledialog.askstring("Input", "Enter the radius of the circle:"))
        area = 3.14159 * (radius ** 2)
        messagebox.showinfo("Area Calculation", f"The area of the circle is: {area:.2f}")
    
    elif shape == "Rectangle":
        length = float(simpledialog.askstring("Input", "Enter the length of the rectangle:"))
        width = float(simpledialog.askstring("Input", "Enter the width of the rectangle:"))
        area = length * width
        messagebox.showinfo("Area Calculation", f"The area of the rectangle is: {area:.2f}")
    
    elif shape == "Triangle":
        base = float(simpledialog.askstring("Input", "Enter the base of the triangle:"))
        height = float(simpledialog.askstring("Input", "Enter the height of the triangle:"))
        area = 0.5 * base * height
        messagebox.showinfo("Area Calculation", f"The area of the triangle is: {area:.2f}")
    
    elif shape == "Square":
        side = float(simpledialog.askstring("Input", "Enter the side length of the square:"))
        area = side ** 2
        messagebox.showinfo("Area Calculation", f"The area of the square is: {area:.2f}")
    
    elif shape == "Trapezium":
        base1 = float(simpledialog.askstring("Input", "Enter the first base of the trapezium:"))
        base2 = float(simpledialog.askstring("Input", "Enter the second base of the trapezium:"))
        height = float(simpledialog.askstring("Input", "Enter the height of the trapezium:"))
        area = 0.5 * (base1 + base2) * height
        messagebox.showinfo("Area Calculation", f"The area of the trapezium is: {area:.2f}")
    
    elif shape == "Parallelogram":
        base = float(simpledialog.askstring("Input", "Enter the base of the parallelogram:"))
        height = float(simpledialog.askstring("Input", "Enter the height of the parallelogram:"))
        area = base * height
        messagebox.showinfo("Area Calculation", f"The area of the parallelogram is: {area:.2f}")
    
    elif shape == "Semi-Circle":
        radius = float(simpledialog.askstring("Input", "Enter the radius of the semi-circle:"))
        area = (3.14159 * (radius ** 2)) / 2
        messagebox.showinfo("Area Calculation", f"The area of the semi-circle is: {area:.2f}")

    else:
        messagebox.showinfo("Error", "Invalid shape selected!")

def calculate_perimeter(shape):
    if shape == "Circle":
        radius = float(simpledialog.askstring("Input", "Enter the radius of the circle:"))
        perimeter = 2 * 3.14159 * radius
        messagebox.showinfo("Perimeter Calculation", f"The perimeter (circumference) of the circle is: {perimeter:.2f}")

    elif shape == "Rectangle":
        length = float(simpledialog.askstring("Input", "Enter the length of the rectangle:"))
        width = float(simpledialog.askstring("Input", "Enter the width of the rectangle:"))
        perimeter = 2 * (length + width)
        messagebox.showinfo("Perimeter Calculation", f"The perimeter of the rectangle is: {perimeter:.2f}")

    elif shape == "Triangle":
        side1 = float(simpledialog.askstring("Input", "Enter the length of the first side of the triangle:"))
        side2 = float(simpledialog.askstring("Input", "Enter the length of the second side of the triangle:"))
        side3 = float(simpledialog.askstring("Input", "Enter the length of the third side of the triangle:"))
        perimeter = side1 + side2 + side3
        messagebox.showinfo("Perimeter Calculation", f"The perimeter of the triangle is: {perimeter:.2f}")

    elif shape == "Square":
        side = float(simpledialog.askstring("Input", "Enter the side length of the square:"))
        perimeter = 4 * side
        messagebox.showinfo("Perimeter Calculation", f"The perimeter of the square is: {perimeter:.2f}")

    elif shape == "Trapezium":
        side1 = float(simpledialog.askstring("Input", "Enter the length of the first base of the trapezium:"))
        side2 = float(simpledialog.askstring("Input", "Enter the length of the second base of the trapezium:"))
        side3 = float(simpledialog.askstring("Input", "Enter the length of the first side of the trapezium:"))
        side4 = float(simpledialog.askstring("Input", "Enter the length of the second side of the trapezium:"))
        perimeter = side1 + side2 + side3 + side4
        messagebox.showinfo("Perimeter Calculation", f"The perimeter of the trapezium is: {perimeter:.2f}")

    elif shape == "Parallelogram":
        base = float(simpledialog.askstring("Input", "Enter the base of the parallelogram:"))
        side = float(simpledialog.askstring("Input", "Enter the side length of the parallelogram:"))
        perimeter = 2 * (base + side)
        messagebox.showinfo("Perimeter Calculation", f"The perimeter of the parallelogram is: {perimeter:.2f}")

    elif shape == "Semi-Circle":
        radius = float(simpledialog.askstring("Input", "Enter the radius of the semi-circle:"))
        perimeter = (3.14159 * radius) + (2 * radius)
        messagebox.showinfo("Perimeter Calculation", f"The perimeter of the semi-circle is: {perimeter:.2f}")

    else:
        messagebox.showinfo("Error", "Invalid shape selected!")

def calculate_3d(feature, shape):
    try:
        if shape == "Cylinder":
            radius = float(simpledialog.askstring("Input", "Enter the radius of the cylinder:"))
            height = float(simpledialog.askstring("Input", "Enter the height of the cylinder:"))
            if feature == "Volume":
                result = 3.14159 * radius**2 * height
            elif feature == "Surface Area":
                result = 2 * 3.14159 * radius * (radius + height)
            elif feature == "Curved Surface Area":
                result = 2 * 3.14159 * radius * height

        elif shape == "Cube":
            side = float(simpledialog.askstring("Input", "Enter the side length of the cube:"))
            if feature == "Volume":
                result = side**3
            elif feature == "Surface Area":
                result = 6 * side**2
            elif feature == "Curved Surface Area":
                result = 4 * side**2

        elif shape == "Cuboid":
            length = float(simpledialog.askstring("Input", "Enter the length of the cuboid:"))
            width = float(simpledialog.askstring("Input", "Enter the width of the cuboid:"))
            height = float(simpledialog.askstring("Input", "Enter the height of the cuboid:"))
            if feature == "Volume":
                result = length * width * height
            elif feature == "Surface Area":
                result = 2 * (length * width + width * height + height * length)
            elif feature == "Curved Surface Area":
                result = 2 * height * (length + width)

        elif shape == "Sphere":
            radius = float(simpledialog.askstring("Input", "Enter the radius of the sphere:"))
            if feature == "Volume":
                result = (4 / 3) * 3.14159 * radius**3
            elif feature == "Surface Area":
                result = 4 * 3.14159 * radius**2
            elif feature == "Curved Surface Area":
                result = 4 * 3.14159 * radius**2  # Same as total surface area for a sphere

        elif shape == "Hemisphere":
            radius = float(simpledialog.askstring("Input", "Enter the radius of the hemisphere:"))
            if feature == "Volume":
                result = (2 / 3) * 3.14159 * radius**3
            elif feature == "Surface Area":
                result = 3 * 3.14159 * radius**2
            elif feature == "Curved Surface Area":
                result = 2 * 3.14159 * radius**2

        elif shape == "Cone":
            radius = float(simpledialog.askstring("Input", "Enter the radius of the cone:"))
            height = float(simpledialog.askstring("Input", "Enter the height of the cone:"))
            slant_height = (radius**2 + height**2)**0.5  # Calculate slant height
            if feature == "Volume":
                result = (1 / 3) * 3.14159 * radius**2 * height
            elif feature == "Surface Area":
                result = 3.14159 * radius * (radius + slant_height)
            elif feature == "Curved Surface Area":
                result = 3.14159 * radius * slant_height

        else:
            messagebox.showinfo("Error", "Invalid shape selected!")
            return

        # Display the result
        messagebox.showinfo(f"{feature} Calculation", f"The {feature.lower()} of the {shape.lower()} is: {result:.2f}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def convert_length(length_input, length_option, length_result):
    if length_option.get() == "Meters to Kilometers":
        result = float(length_input.get()) / 1000
    elif length_option.get() == "Kilometers to Meters":
        result = float(length_input.get()) * 1000
    elif length_option.get() == "Inches to Centimeters":
        result = float(length_input.get()) * 2.54
    elif length_option.get() == "Centimeters to Inches":
        result = float(length_input.get()) / 2.54
    length_result.set(f"{result:.2f}")

def convert_weight(weight_input, weight_option, weight_result): 
    if weight_option.get() == "Grams to Kilograms":
        result = float(weight_input.get()) / 1000
    elif weight_option.get() == "Kilograms to Grams":
        result = float(weight_input.get()) * 1000
    elif weight_option.get() == "Pounds to Ounces":
        result = float(weight_input.get()) * 16
    elif weight_option.get() == "Ounces to Pounds":
        result = float(weight_input.get()) / 16
        weight_result.set(f"{result:.2f}")
        weight_result.set("Invalid Input")

def convert_temperature(temp_input, temp_option, temp_result):
    temp = float(temp_input.get())
    if temp_option.get() == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
    elif temp_option.get() == "Fahrenheit to Celsius":
        result = (temp - 32) * 5/9
    elif temp_option.get() == "Celsius to Kelvin":
        result = temp + 273.15
    elif temp_option.get() == "Kelvin to Celsius":
        result = temp - 273.15
    elif temp_option.get() == "Fahrenheit to Kelvin":
        result = (temp - 32) * 5/9 + 273.15
    elif temp_option.get() == "Kelvin to Fahrenheit":
        result = (temp - 273.15) * 9/5 + 32
    temp_result.set(f"{result:.2f}")

def convert_time(time_input, time_option, time_result):
    time = float(time_input.get())
    if time_option.get() == "Seconds to Minutes":
        result = time / 60
    elif time_option.get() == "Minutes to Seconds":
        result = time * 60
    elif time_option.get() == "Minutes to Hours":
        result = time / 60
    elif time_option.get() == "Hours to Minutes":
        result = time * 60
    elif time_option.get() == "Seconds to Hours":
        result = time / 3600
    elif time_option.get() == "Hours to Seconds":
        result = time * 3600
    time_result.set(f"{result:.2f}")

def unit_conversion():
    for widget in root.winfo_children():
        widget.pack_forget()
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)
    notebook.pack(expand=True)  # Show conversion page

    # Tabs
    length_tab = ttk.Frame(notebook)
    weight_tab = ttk.Frame(notebook)
    temp_tab = ttk.Frame(notebook)
    time_tab = ttk.Frame(notebook)
    
    style = ttk.Style()
    style.configure("TNotebook.Tab", font=("Arial", 22))

    notebook.add(length_tab, text="Length")
    notebook.add(weight_tab, text="Weight")
    notebook.add(temp_tab, text="Temperature")
    notebook.add(time_tab, text="Time")

    # Length Conversion
    ttk.Label(length_tab, text="Input Value:", font=("Arial", 20)).grid(row=0, column=0, padx=10, pady=5)
    length_input = ttk.Entry(length_tab)
    length_input.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(length_tab, text="Convert:", font=("Arial", 17)).grid(row=1, column=0, padx=10, pady=5)
    length_option = ttk.Combobox(length_tab, values=["Meters to Kilometers", "Kilometers to Meters", "Inches to Centimeters", "Centimeters to Inches"])
    length_option.grid(row=1, column=1, padx=10, pady=5)

    ttk.Button(length_tab, text="Convert", command=lambda: convert_length(length_input, length_option, length_result)).grid(row=2, column=0, columnspan=2, pady=10)
    length_result = tk.StringVar()
    ttk.Label(length_tab, text="Result:", font=("Arial", 17)).grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(length_tab, textvariable=length_result, state="readonly").grid(row=3, column=1, padx=10, pady=5)

    # Weight Conversion
    ttk.Label(weight_tab, text="Input Value:", font=("Arial", 17)).grid(row=0, column=0, padx=10, pady=5)
    weight_input = ttk.Entry(weight_tab)
    weight_input.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(weight_tab, text="Convert:", font=("Arial", 17)).grid(row=1, column=0, padx=10, pady=5)
    weight_option = ttk.Combobox(weight_tab, values=["Grams to Kilograms", "Kilograms to Grams", "Pounds to Ounces", "Ounces to Pounds"])
    weight_option.grid(row=1, column=1, padx=10, pady=5)

    ttk.Button(weight_tab, text="Convert", command=lambda: convert_weight(weight_input, weight_option, weight_result)).grid(row=2, column=0, columnspan=2, pady=10)
    weight_result = tk.StringVar()
    ttk.Label(weight_tab, text="Result:", font=("Arial", 17)).grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(weight_tab, textvariable=weight_result, state="readonly").grid(row=3, column=1, padx=10, pady=5)

    # Temperature Conversion
    ttk.Label(temp_tab, text="Input Value:", font=("Arial", 17)).grid(row=0, column=0, padx=10, pady=5)
    temp_input = ttk.Entry(temp_tab)
    temp_input.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(temp_tab, text="Convert:", font=("Arial", 17)).grid(row=1, column=0, padx=10, pady=5)
    temp_option = ttk.Combobox(temp_tab, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius", "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])
    temp_option.grid(row=1, column=1, padx=10, pady=5)

    ttk.Button(temp_tab, text="Convert", command=lambda: convert_temperature(temp_input, temp_option, temp_result)).grid(row=2, column=0, columnspan=2, pady=10)
    temp_result = tk.StringVar()
    ttk.Label(temp_tab, text="Result:", font=("Arial", 17)).grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(temp_tab, textvariable=temp_result, state="readonly").grid(row=3, column=1, padx=10, pady=5)

    # Time Conversion
    ttk.Label(time_tab, text="Input Value:", font=("Arial", 17)).grid(row=0, column=0, padx=10, pady=5)
    time_input = ttk.Entry(time_tab)
    time_input.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(time_tab, text="Convert:", font=("Arial", 17)).grid(row=1, column=0, padx=10, pady=5)
    time_option = ttk.Combobox(time_tab, values=["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Seconds to Hours", "Hours to Seconds"])
    time_option.grid(row=1, column=1, padx=10, pady=5)

    ttk.Button(time_tab, text="Convert", command=lambda: convert_time(time_input, time_option, time_result)).grid(row=2, column=0, columnspan=2, pady=10)
    time_result = tk.StringVar()
    ttk.Label(time_tab, text="Result:", font=("Arial", 17)).grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(time_tab, textvariable=time_result, state="readonly").grid(row=3, column=1, padx=10, pady=5)

def about():
    messagebox.showinfo("About", "PyGenExpert Calculator v1.0\nDeveloped by Somesh Kumar Satpathy\n\nDeveloped under the supervision of \nAcademic Session: 2024-25")

def contact():
    messagebox.showinfo("Contact", "For queries, contact: someshkumarsatapathy2009@gmail.com")

def convert_currency():
    from_currency = from_currency_entry.get()
    to_currency = to_currency_entry.get()
    amount = amount_entry.get()

    # Check if the amount entered is valid
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for amount.")
        return

    # API URL and Key
    url = "https://api.apilayer.com/currency_data/live"
    api_key = "EwAvmex2Fx3DMUFMNX7TW7wZor4zaIm6"  # Replace with your actual API key

    # Construct the API request
    query_params = {
        "source": from_currency,
        "currencies": to_currency
    }
    headers = {
        "apikey": api_key
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=query_params)

    if response.status_code == 200:
        data = response.json()
        if 'success' in data and data['success']:
            conversion_rate = data['quotes'][f"{from_currency}{to_currency}"]
            converted_amount = amount * conversion_rate
            result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
        else:
            messagebox.showerror("Error", "Failed to retrieve conversion data.")
    else:
        messagebox.showerror("API Error", "Error fetching data from API. Please try again later.")
def show_currency_converter():
    # Clear any existing widgets in the frame
    for widget in root.winfo_children():
        widget.destroy()
    frame = ttk.Frame(root)

    frame.pack(expand=True)  # Show conversion page
    # Add labels and entry fields for currency converter
    tk.Label(frame, text="From Currency (e.g., USD)").grid(row=0, column=0, padx=10, pady=10)
    global from_currency_entry
    from_currency_entry = ttk.Entry(frame)
    from_currency_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="To Currency (e.g., EUR)").grid(row=1, column=0, padx=10, pady=10)
    global to_currency_entry
    to_currency_entry = ttk.Entry(frame)
    to_currency_entry.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(frame, text="Amount").grid(row=2, column=0, padx=10, pady=10)
    global amount_entry
    amount_entry = ttk.Entry(frame)
    amount_entry.grid(row=2, column=1, padx=10, pady=10)

    # Add a button to trigger the conversion
    convert_button = tk.Button(frame, text="Convert", command=convert_currency)
    convert_button.grid(row=3, column=0, columnspan=2, pady=20)

    # Label to display the conversion result
    global result_label
    result_label = tk.Label(frame, text="Converted Amount: ")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)
# Create the main application window
root = tk.Tk()
root.title("PyGenExpert Calculator v1.0")
root.geometry("600x800")
root.resizable(False, False)
root.wm_iconbitmap("logo.ico")
root.config(background="grey")

# Create a container frame to switch views
container_frame = tk.Frame(root)
container_frame.pack(expand=True)
# Add content
content = """
Developed By
Somesh Kumar Satpathy
Class: 10 A | Roll No.: 34

Subject: Artificial Intelligence (417)

School: Kendriya Vidyalaya Gajapati

Guided By:
Mr. Love Khandelwal
AI Teacher

Academic Session: 2024-25

Note:
This project is a proud result of creativity, collaboration, \nand the power of artificial intelligence! 
"""

label = tk.Label(root, text=content, font=("Arial", 17), justify="left")
label.pack(pady=(20, 100))
# Create a menu bar
menu_bar = Menu(root)

# Basic Calculation menu
menu_bar.add_command(label="Basic Calculation", command=basic_calculation)

# Area menu
area_menu = Menu(menu_bar, tearoff=0)
shapes = ["Circle", "Rectangle", "Triangle", "Square", "Trapezium", "Parallelogram", "Semi-Circle"]
for shape in shapes:
    area_menu.add_command(label=shape, command=lambda s=shape: calculate_area(s))
menu_bar.add_cascade(label="Area", menu=area_menu)

# Perimeter menu
perimeter_menu = Menu(menu_bar, tearoff=0)
for shape in shapes:
    perimeter_menu.add_command(label=shape, command=lambda s=shape: calculate_perimeter(s))
menu_bar.add_cascade(label="Perimeter", menu=perimeter_menu)

# 3-D Shapes menu
shapes_3d_menu = Menu(menu_bar, tearoff=0)

# Submenu for Surface Area
surface_area_menu = Menu(shapes_3d_menu, tearoff=0)
three_d_shapes = ["Cylinder", "Cube", "Cuboid", "Sphere", "Hemisphere", "Cone"]
for shape in three_d_shapes:
    surface_area_menu.add_command(label=shape, command=lambda s=shape: calculate_3d("Surface Area", s))
shapes_3d_menu.add_cascade(label="Surface Area", menu=surface_area_menu)

# Submenu for Curved Surface Area
curved_surface_area_menu = Menu(shapes_3d_menu, tearoff=0)
for shape in three_d_shapes:
    curved_surface_area_menu.add_command(label=shape, command=lambda s=shape: calculate_3d("Curved Surface Area", s))
shapes_3d_menu.add_cascade(label="Curved Surface Area", menu=curved_surface_area_menu)

# Submenu for Volume
volume_menu = Menu(shapes_3d_menu, tearoff=0)
for shape in three_d_shapes:
    volume_menu.add_command(label=shape, command=lambda s=shape: calculate_3d("Volume", s))
shapes_3d_menu.add_cascade(label="Volume", menu=volume_menu)

menu_bar.add_cascade(label="3-D Shapes", menu=shapes_3d_menu)

menu_bar.add_command(label="Unit Conversion", command=unit_conversion)

menu_bar.add_command(label="Currency Converter", command=show_currency_converter)

# About menu
menu_bar.add_command(label="About", command=about)

# Contact menu
menu_bar.add_command(label="Contact", command=contact)

# menu_bar.add_cascade(label="Unit Conversion", menu=unit_menu)
menu_bar.add_command(label="Exit", command=root.destroy)
# Configure the menu bar in the root window
root.config(menu=menu_bar)

# Run the application
root.mainloop()
