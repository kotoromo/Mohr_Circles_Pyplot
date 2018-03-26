from tkinter import Tk, Label, Button, Entry, PhotoImage, END, messagebox, StringVar
from numpy import array
from circles import MohrCircles
import _thread
from tensors import Tensors


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

        # Setting stringvars...
        self.x_11 = StringVar()
        self.x_12 = StringVar()
        self.x_13 = StringVar()
        self.x_21 = StringVar()
        self.x_22 = StringVar()
        self.x_23 = StringVar()
        self.x_31 = StringVar()
        self.x_32 = StringVar()
        self.x_33 = StringVar()

        self.x_11_entry = Entry(master, justify='center', textvariable=self.x_11)
        self.x_12_entry = Entry(master, justify='center', textvariable=self.x_12)
        self.x_13_entry = Entry(master, justify='center', textvariable=self.x_13)

        self.x_21_entry = Entry(master, justify='center', textvariable=self.x_21)
        self.x_22_entry = Entry(master, justify='center', textvariable=self.x_22)
        self.x_23_entry = Entry(master, justify='center', textvariable=self.x_23)

        self.x_31_entry = Entry(master, justify='center', textvariable=self.x_31)
        self.x_32_entry = Entry(master, justify='center', textvariable=self.x_32)
        self.x_33_entry = Entry(master, justify='center', textvariable=self.x_33)

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

        self.principal_stresses_btn = Button(
            master,
            text="Obtener esfuerzos principales",
            command=self.generate_principal_stresses
        )

        self.principal_stresses_btn.grid(row=5, column=2, pady=25, padx=5)

        self.clear_btn = Button(
            master,
            text="Limpiar campos",
            command=self.clear_fields
        )
        self.clear_btn.grid(row=5, column=3, pady=25, padx=5)

        self.quit_btn = Button(
            master,
            text="Salir",
            command=self.master.quit
        )
        self.quit_btn.grid(row=5, column=4, pady=25, padx=5)

        self.credits_label = Label(
            master,
            text="Software creado por Nicky Garcia F.\n" +
            "Tkinter, Matplotlib y NumPy son de sus respectivos autores.\n" +
            "Sigue la licencia MIT. Código fuente disponible en: " +
            "https://github.com/kotoromo",
            font=("Times New Roman", 9)
        )
        self.credits_label.grid(sticky='S', columnspan=6)

        # Cleaning...
        self.clear_fields()

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
    
    def generate_principal_stresses(self):
        tensor = self.produce_tensor()
        tensor = Tensors.principal_stresses(tensor)

        # put it in the entry boxes.
        self.clear_fields()
        self.x_11.set(tensor[0])
        self.x_12.set(0)
        self.x_13.set(0)
        self.x_21.set(0)
        self.x_22.set(tensor[1])
        self.x_23.set(0)
        self.x_31.set(0)
        self.x_32.set(0)
        self.x_33.set(tensor[2])  

    def clear_fields(self):
        self.x_11.set(0)
        self.x_12.set(0)
        self.x_13.set(0)
        self.x_21.set(0)
        self.x_22.set(0)
        self.x_23.set(0)
        self.x_31.set(0)
        self.x_32.set(0)
        self.x_33.set(0)

    def produce_tensor(self):
        try:
            stress_tensor = array([
                [
                    float(self.x_11.get()),
                    float(self.x_12.get()),
                    float(self.x_13.get())
                ],
                [
                    float(self.x_21.get()),
                    float(self.x_22.get()),
                    float(self.x_23.get())
                ],
                [
                    float(self.x_31.get()),
                    float(self.x_32.get()),
                    float(self.x_33.get())
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
