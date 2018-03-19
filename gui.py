from tkinter import Tk, Label, Button, Entry, PhotoImage, END, messagebox
from numpy import array
from circles import MohrCircles
import _thread


class GUI:
    def __init__(self, master):
        self.master = master
        
        self.planes = 1000
        self.sigma_photo = PhotoImage(file="./res/sigma_left.png")
        self.right_bracket_photo = PhotoImage(file="./res/sigma_right.png")

        self.label = Label(
            master,
            text="Porfavor ingrese los valores del tensor de esfuerzos.",
            font=("Times New Roman", 22)
        )

        self.label.grid(columnspan=6, sticky='N')

        self.sigma_label = Label(master, image=self.sigma_photo)
        self.sigma_label.grid(rowspan=3, column=0, sticky='E')

        self.right_bracket = Label(master, image=self.right_bracket_photo)
        self.right_bracket.grid(rowspan=3, column=4, row=1, sticky='W')

        self.x_11_entry = Entry(master, justify='center')
        self.x_12_entry = Entry(master, justify='center')
        self.x_13_entry = Entry(master, justify='center')

        self.x_21_entry = Entry(master, justify='center')
        self.x_22_entry = Entry(master, justify='center')
        self.x_23_entry = Entry(master, justify='center')

        self.x_31_entry = Entry(master, justify='center')
        self.x_32_entry = Entry(master, justify='center')
        self.x_33_entry = Entry(master, justify='center')

        self.x_11_entry.grid(row=1, column=1)
        self.x_12_entry.grid(row=1, column=2)
        self.x_13_entry.grid(row=1, column=3)

        self.x_21_entry.grid(row=2, column=1)
        self.x_22_entry.grid(row=2, column=2)
        self.x_23_entry.grid(row=2, column=3)

        self.x_31_entry.grid(row=3, column=1)
        self.x_32_entry.grid(row=3, column=2)
        self.x_33_entry.grid(row=3, column=3)

        self.planes_label = Label(master, text="Número de planos: ")
        self.planes_label.grid(row=4, column=1)
        self.planes_entry = Entry(master, justify='center')
        self.planes_entry.insert(0, '1000')
        self.planes_entry.grid(row=4, column=2, padx=5)

        self.generate_btn = Button(
            master,
            text="Generar circulos de Mohr",
            command=self.generate_circles
        )
        self.generate_btn.grid(row=5, column=1, pady=25, padx=5)

        self.clear_btn = Button(
            master,
            text="Limpiar campos",
            command=self.clear_fields
        )
        self.clear_btn.grid(row=5, column=2, pady=25, padx=5)

        self.quit_btn = Button(
            master,
            text="Salir",
            command=self.master.quit
        )
        self.quit_btn.grid(row=5, column=3, pady=25, padx=5)

        self.credits_label = Label(
            master,
            text="Software creado por Nicky Garcia F.\n" +
            "Tkinter, Matplotlib y NumPy son de sus respectivos autores.\n" +
            "Sigue la licencia MIT. Código fuente disponible en: " +
            "https://github.com/kotoromo",
            font=("Times New Roman", 9)
        )
        self.credits_label.grid(sticky='S', columnspan=6)

    def generate_circles(self):
        stress_tensor = self.produce_tensor()
        try:
            print("Starting thread!")
            _thread.start_new_thread(
                MohrCircles.draw(stress_tensor, self.planes)
            )

        except:
            print("Thread finished")

        response = messagebox.askyesno(
                "Aviso", "Desea conservar el tensor de esfuerzos?"
            )

        if response is True:
            return
        else:
            self.clear_fields()

    def clear_fields(self):
        self.x_11_entry.delete(0, END)
        self.x_12_entry.delete(0, END)
        self.x_13_entry.delete(0, END)
        self.x_21_entry.delete(0, END)
        self.x_22_entry.delete(0, END)
        self.x_23_entry.delete(0, END)
        self.x_31_entry.delete(0, END)
        self.x_32_entry.delete(0, END)
        self.x_33_entry.delete(0, END)

    def produce_tensor(self):
        try:
            stress_tensor = array([
                [
                    float(self.x_11_entry.get()),
                    float(self.x_12_entry.get()),
                    float(self.x_13_entry.get())
                ],
                [
                    float(self.x_21_entry.get()),
                    float(self.x_22_entry.get()),
                    float(self.x_23_entry.get())
                ],
                [
                    float(self.x_31_entry.get()),
                    float(self.x_32_entry.get()),
                    float(self.x_33_entry.get())
                ]
            ])

            self.planes = int(self.planes_entry.get())

            return stress_tensor
        except:
            messagebox.showerror(
                "Error de Formato",
                "Introdujo algun dato invalido en alguno de los campos."
            )


def start():
    root = Tk()
    root.title('Circulos de Mohr')
    root.iconbitmap("./res/sigma.ico")
    myGUI = GUI(root)
    root.mainloop()
