import tkinter as tk


class GUICalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(
            self.master,
            textvariable=self.result_var,
            font=('Arial', 24),
            bd=10,
            insertwidth=2,
            width=14,
            borderwidth=4
        )
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(
                self.master,
                text=button,
                padx=20,
                pady=20,
                font=('Arial', 18),
                command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.result_var.set("")
            return
        if button == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)  # Be cautious with eval in production code
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
            return
        current_text = self.result_var.get()
        new_text = current_text + str(button)
        self.result_var.set(new_text)



