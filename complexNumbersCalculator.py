import cmath
from tkinter import *
import re
from enum import Enum
from cmath import *


class Operation(Enum):
    ADDITION = 1
    MULTIPLICATION = 2
    NEGATION = 3
    INVERSION = 4


class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real: float = real
        self.imaginary: float = imaginary

    @classmethod
    def fromstring(cls, string: str):
        number = complex(string)
        real: float = number.real
        imaginary: float = number.imag
        return cls(real, imaginary)

    def add(self, other_complex):
        new_real = self.real + other_complex.real
        new_imaginary = self.imaginary + other_complex.imaginary
        return Complex(new_real, new_imaginary)

    def negation(self):
        new_real = self.real * -1
        new_imaginary = self.imaginary * -1
        return Complex(new_real, new_imaginary)

    def multiply(self, other_complex):
        new_real = self.real * other_complex.real - self.imaginary * other_complex.imaginary
        new_imaginary = self.imaginary * other_complex.imaginary + self.real * other_complex.real
        return Complex(new_real, new_imaginary)

    def inversion(self):
        scale = self.real ** 2 + self.imaginary ** 2
        return Complex(self.real / scale, (self.imaginary * -1) / scale)

    def to_string(self):
        return str(self.real) + "+" + str(self.imaginary) + "j"



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.operation = Operation.ADDITION
        self.initialize_window()

    def initialize_window(self):
        self.master.title("Complex Number Calculator")
        self.pack(fill=BOTH, expand=1)  # allows widget to take full space of window

        calculate_button = Button(self, text="Calculate", width=18, height=8, command=self.calculate)
        calculate_button.place(x=270, y=0)

        self.input_box = Text(self, height=8, width=35)
        self.input_box.place(x=0, y=0)

        self.output_box = Text(self, height=8, width=53, state=DISABLED)
        self.output_box.place(x=0, y=150)

        self.menu = Menu(self.master)

        self.master.config(menu=self.menu)

        self.calculation_menu = Menu(self.menu)
        self.calculation_menu.add_checkbutton(label="Addition",
                                              command=self.setAddition,
                                              onvalue=Operation.ADDITION,
                                              offvalue=Operation.ADDITION,
                                              variable=self.operation)
        self.calculation_menu.add_checkbutton(label="Multiplication",
                                              command=self.setMultiplication,
                                              onvalue=Operation.MULTIPLICATION,
                                              offvalue=Operation.MULTIPLICATION,
                                              variable=self.operation)
        self.calculation_menu.add_checkbutton(label="Negation",
                                              command=self.setNegation,
                                              onvalue=Operation.NEGATION,
                                              offvalue=Operation.NEGATION,
                                              variable=self.operation)
        self.calculation_menu.add_checkbutton(label="Inversion",
                                              command=self.setInversion,
                                              onvalue=Operation.INVERSION,
                                              offvalue=Operation.INVERSION,
                                              variable=self.operation)

        self.menu.add_cascade(label="Calculation", menu=self.calculation_menu)

    def get_input(self):
        return self.input_box.get("1.0", END)

    def set_output(self, newOutput):
        self.output_box.config(state=NORMAL)
        self.output_box.delete("1.0", END) #Deletes all text from first character index to end.
        self.output_box.insert("1.0", newOutput)
        self.output_box.config(state=DISABLED)

    def setMultiplication(self):
        self.operation = Operation.MULTIPLICATION

    def setAddition(self):
        self.operation = Operation.ADDITION

    def setInversion(self):
        self.operation = Operation.INVERSION

    def setNegation(self):
        self.operation = Operation.NEGATION

    def calculate(self):
        string = self.get_input()
        if self.operation == Operation.MULTIPLICATION:
            to_multiply = string.split("\n")
            first_number_string = to_multiply[0]
            second_number_string = to_multiply[1]
            first_number_string.replace(" ", "")
            second_number_string.replace(" ", "")
            first_complex = Complex.fromstring(first_number_string)
            second_complex = Complex.fromstring(second_number_string)
            self.set_output(first_complex.multiply(second_complex).to_string())
        elif self.operation == Operation.ADDITION:
            to_add = string.split("\n")
            first_number_string = to_add[0]
            second_number_string = to_add[1]
            first_number_string.replace(" ", "")
            second_number_string.replace(" ", "")
            print(second_number_string)
            first_complex = Complex.fromstring(first_number_string)
            second_complex = Complex.fromstring(second_number_string)
            self.set_output(first_complex.add(second_complex).to_string())
        elif self.operation == Operation.NEGATION:
            number = Complex.fromstring(string.split("\n")[0].replace(" ", ""))
            self.set_output(number.negation().to_string())
        elif self.operation == Operation.INVERSION:
            number = Complex.fromstring(string.split("\n")[0].replace(" ", ""))
            self.set_output(number.inversion().to_string())


root = Tk()
root.geometry("400x300")
window = Window(root)
root.mainloop()
