import tkinter as tk
from tkinter import messagebox

def calculate_frequency():
    try:
        L = float(entry_length.get())
        CNT_ratio = float(entry_cnt.get())
        rho = float(entry_rho.get())
        E = float(entry_E.get())

        # equation for the first frequency
        freq = (3.14 / L)**2 * ((E * (1 + CNT_ratio)) / rho)**0.5
        result_label.config(text=f"natural frequency ≈ {freq:.2f} Hz")
    except:
        messagebox.showerror("error", "please enter corect values")

root = tk.Tk()
root.title("natural frequuency simulator - FG-CNTRC")

tk.Label(root, text="ray length (m):").pack()
entry_length = tk.Entry(root)
entry_length.pack()

tk.Label(root, text="ratio CNT:").pack()
entry_cnt = tk.Entry(root)
entry_cnt.pack()

tk.Label(root, text="density (kg/m³):").pack()
entry_rho = tk.Entry(root)
entry_rho.pack()

tk.Label(root, text="modulus of elasticity (Pa):").pack()
entry_E = tk.Entry(root)
entry_E.pack()

tk.Button(root, text="calculate the frequency", command=calculate_frequency).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

