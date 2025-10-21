import tkinter as tk

def calculate_miles_to_km():
    pass

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(400, 200)
window.config(padx=20, pady=20)

#Labels
miles = tk.Label(text="Miles")
km = tk.Label(text="Km")
is_equal_to = tk.Label(text="Is equal to")
result_value = tk.Label(text=0)

#Button
calculate = tk.Button(text="Calculate", command=calculate_miles_to_km)

window.mainloop()