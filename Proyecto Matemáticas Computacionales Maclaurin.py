import math
from tkinter import *
from tkinter import ttk

# Definir funciones con la serie de Maclaurin (trabajando en radianes)
def mac_sin(x):
    # Usamos más términos en la serie de Maclaurin
    x = math.radians(x)  # Convertir de grados a radianes
    return round(x - (x**3)/math.factorial(3) + (x**5)/math.factorial(5) - (x**7)/math.factorial(7) + (x**9)/math.factorial(9), 8)

def mac_cos(x):
    # Usamos más términos en la serie de Maclaurin
    x = math.radians(x)  # Convertir de grados a radianes
    return round(1 - (x**2)/math.factorial(2) + (x**4)/math.factorial(4) - (x**6)/math.factorial(6) + (x**8)/math.factorial(8), 8)

def mac_tan(x):
    return round(mac_sin(x) / mac_cos(x), 8)

def mac_cot(x):
    return round(mac_cos(x) / mac_sin(x), 8)

def mac_sec(x):
    return round(1 / mac_cos(x), 8)

def mac_csc(x):
    return round(1 / mac_sin(x), 8)

# Función para manejar las entradas
def valores(tecla):
    if tecla in "0123456789().":
        entrada2.set(entrada2.get() + tecla)
    elif tecla in "+-*/":
        entrada2.set(entrada2.get() + tecla)
    elif tecla in ["sin", "cos", "tan", "cot", "sec", "csc"]:
        entrada2.set(entrada2.get() + tecla + "(")  # Agrega un paréntesis de apertura
    elif tecla == "=":
        try:
            expresion = entrada2.get()

            # Guardar en entrada1 la expresión actual
            entrada1.set(entrada2.get())
            
            # Reemplazar las funciones trigonométricas por las definidas con Maclaurin
            expresion = expresion.replace("sin", "mac_sin")
            expresion = expresion.replace("cos", "mac_cos")
            expresion = expresion.replace("tan", "mac_tan")
            expresion = expresion.replace("cot", "mac_cot")
            expresion = expresion.replace("sec", "mac_sec")
            expresion = expresion.replace("csc", "mac_csc")

            res = eval(expresion)
            entrada2.set(str(res))
        except Exception as e:
            entrada2.set("Error")
    elif tecla == "AC":
        entrada1.set("")
        entrada2.set("")
    elif tecla == "⌫":
        entrada2.set(entrada2.get()[:-1])

# Configuración de la interfaz
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(W, E, N, S))

# Variables para las entradas
entrada1 = StringVar()
entrada2 = StringVar()

# Etiquetas
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, font="Arial 15", anchor="e", background="#DBDBDB")
label_entrada1.grid(column=0, row=0, columnspan=5, sticky=(W, E, N, S))

label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, font="Arial 40", anchor="e", background="#DBDBDB")
label_entrada2.grid(column=0, row=1, columnspan=5, sticky=(W, E, N, S))

# Crear botones numéricos y operacionales
botones = [
    ('7', 0, 3), ('8', 1, 3), ('9', 2, 3), ('/', 3, 3),
    ('4', 0, 4), ('5', 1, 4), ('6', 2, 4), ('*', 3, 4),
    ('1', 0, 5), ('2', 1, 5), ('3', 2, 5), ('-', 3, 5),
    ('0', 1, 6), ('.', 0, 6), ('+', 2, 6)
]

for (text, col, row) in botones:
    
    estilos_boton_num = ttk.Style()
    estilos_boton_num.configure("Boton_num.TButton", font="Arial 16", width = 5, background = "#FFFFFF", relief= "flat")
    
    estilos_boton_otros = ttk.Style()
    estilos_boton_otros.configure("Boton_otros.TButton", font="Arial 16", width= 5, relief="flat", background="#CECECE")
    
    ttk.Button(mainframe, text=text, style="Boton_num.TButton", command=lambda t=text: valores(t)).grid(column=col, row=row, sticky=(W, E, N, S))
    ttk.Button(mainframe, text="=", style="Boton_otros.TButton", command=lambda: valores("=")).grid(column=0, row=7, columnspan=4, sticky=(W,E,S,N))

# Botones trigonométricos
botones_trig = [
    ('sin', 4, 3), ('cos', 4, 4), ('tan', 4, 5), ('sec', 4, 6),
    ('cot', 3, 6), ('csc', 4, 7), ('(', 0, 2), (')', 1, 2),
]

for (text, col, row) in botones_trig:
    ttk.Button(mainframe, text=text, style="Boton_otros.TButton", command=lambda t=text: valores(t)).grid(column=col, row=row, sticky=(W, E, N, S))

estilos_boton_borrar = ttk.Style()
estilos_boton_borrar.configure("Boton_borrar.TButton", font="Arial 16", width= 5, relief="flat", background="#CECECE")
estilos_boton_borrar.map("Boton_borrar.TButton", foreground=[("active", "#FF0000")], background=[("active", "#858585")])

# Botón de AC y ⌫ (borrar)
ttk.Button(mainframe, text="AC", style="Boton_borrar.TButton", command=lambda: valores("AC")).grid(column=2, row=2, sticky=(W, E, N, S))
ttk.Button(mainframe, text="⌫", style="Boton_borrar.TButton", command=lambda: valores("⌫")).grid(column=3, row=2, columnspan=2, sticky=(W, E, N, S))

           
# Configuración del comportamiento de redimensionamiento
for i in range(4):
    mainframe.grid_columnconfigure(i, weight=1)
for i in range(10):
    mainframe.grid_rowconfigure(i, weight=1)

root.mainloop()

