import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math

class Analizador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Análisis de Regresiones")
        self.root.geometry("1100x950")
        self.root.configure(bg='#f0f0f5')
        
        self.style = ttk.Style()
        self.style.configure('Custom.TFrame', background='#c6b1c9')
        self.style.configure('Custom.TLabelframe', background='#c6b1c9')
        self.style.configure('Custom.TLabelframe.Label', background='#c6b1c9', font=('Arial', 15, 'bold'))
        self.style.configure('Custom.TButton', 
                           background='#c6b1c9',
                           foreground='Black',
                           font=('Arial', 9),
                           padding=5)
        self.style.configure('Custom.TRadiobutton', 
                           background='#c6b1c9',
                           font=('Arial', 9))
        
        self.DatosX = []
        self.DatosY = []
        
        self.create_widgets()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, style='Custom.TFrame', padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        left_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)
        
        right_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # === SECCIÓN IZQUIERDA ===
        # Frame para entrada de datos 
        input_frame = ttk.LabelFrame(left_frame, text="Entrada de Datos", 
                                   style='Custom.TLabelframe', padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(input_frame, text="X:", background='#f0f0f5').grid(row=0, column=0, padx=5)
        self.x_entry = ttk.Entry(input_frame, width=10)
        self.x_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(input_frame, text="Y:", background='#f0f0f5').grid(row=0, column=2, padx=5)
        self.y_entry = ttk.Entry(input_frame, width=10)
        self.y_entry.grid(row=0, column=3, padx=5)
        
        button_frame = ttk.Frame(input_frame, style='Custom.TFrame')
        button_frame.grid(row=1, column=0, columnspan=4, pady=10)
        
        ttk.Button(button_frame, text="Agregar Punto", 
                  style='Custom.TButton', command=self.add_point).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Limpiar Datos", 
                  style='Custom.TButton', command=self.clear_data).grid(row=0, column=1, padx=5)
        
        points_frame = ttk.LabelFrame(left_frame, text="Puntos Ingresados", 
                                    style='Custom.TLabelframe', padding="10")
        points_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        
        self.points_text = tk.Text(points_frame, height=8, width=25, 
                                 bg='white', relief='solid', pady=5)
        self.points_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Frame para selección de regresión 
        regression_frame = ttk.LabelFrame(left_frame, text="Tipo de Regresión", 
                                        style='Custom.TLabelframe', padding="10")
        regression_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=10)
        
        self.regression_type = tk.StringVar()
        regression_types = [
            "Regresión Lineal",
            "Modelo Exponencial",
            "Ecuación de Potencias",
            "Razón de Crecimiento",
            "Regresión Polinomial"
        ]
        
        for i, reg_type in enumerate(regression_types):
            ttk.Radiobutton(regression_frame, text=reg_type, value=reg_type, 
                          style='Custom.TRadiobutton',
                          variable=self.regression_type).grid(row=i, column=0, sticky=tk.W, pady=2)
        
        ttk.Button(regression_frame, text="Calcular Regresión", 
                  style='Custom.TButton',
                  command=self.calculate_regression).grid(row=len(regression_types), column=0, pady=10)
        
        # === SECCIÓN DERECHA ===
        plot_frame = ttk.LabelFrame(right_frame, text="Visualización", 
                                  style='Custom.TLabelframe', padding="10")
        plot_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.fig.patch.set_facecolor('#f0f0f5')
        self.ax.set_facecolor('#ffffff')
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, pady=5)
        
        results_frame = ttk.LabelFrame(right_frame, text="Resultados", 
                                     style='Custom.TLabelframe', padding="10")
        results_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        
        self.results_text = tk.Text(results_frame, height=8, width=50, 
                                  bg='white', relief='solid', pady=5)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Botón para limpiar solo los resultados
        ttk.Button(results_frame, text="Limpiar Resultados", 
                  style='Custom.TButton',
                  command=self.clear_results).grid(row=1, column=0, pady=(0, 5))
        
        main_frame.columnconfigure(1, weight=1)
        right_frame.columnconfigure(0, weight=1)
        
    def add_point(self):
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            self.DatosX.append(x)
            self.DatosY.append(y)
            
            self.points_text.delete(1.0, tk.END)
            for i in range(len(self.DatosX)):
                self.points_text.insert(tk.END, f"Punto {i+1}: ({self.DatosX[i]}, {self.DatosY[i]})\n")
            
            self.x_entry.delete(0, tk.END)
            self.y_entry.delete(0, tk.END)
            
            self.plot_points()
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
    
    def clear_data(self):
        self.DatosX = []
        self.DatosY = []
        self.points_text.delete(1.0, tk.END)
        self.results_text.delete(1.0, tk.END)
        self.ax.clear()
        self.canvas.draw()
    
    # Limpiar solo los resultados
    def clear_results(self):
        self.results_text.delete(1.0, tk.END)
        # Redibujar el gráfico solo con los puntos, sin la línea de regresión
        self.plot_points()
        
    def calculate_std_dev(self, y_true, y_pred):
        n = len(y_true)
        residuals = [y - yp for y, yp in zip(y_true, y_pred)]
        mean_residual = sum(residuals) / n
        squared_diff = [(r - mean_residual) ** 2 for r in residuals]
        std_dev = math.sqrt(sum(squared_diff) / (n - 1))
        return std_dev
    
    def plot_points(self):
        self.ax.clear()
        self.ax.scatter(self.DatosX, self.DatosY, color='#4a90e2', label='Datos', s=100)
        self.ax.set_xlabel('X', fontsize=10)
        self.ax.set_ylabel('Y', fontsize=10)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_facecolor('#ffffff')
        self.canvas.draw()
    
    def calculate_regression(self):
        if len(self.DatosX) < 5:
            messagebox.showerror("Error", "Se necesitan al menos 5 puntos para realizar la regresión")
            return
            
        regression_type = self.regression_type.get()
        if not regression_type:
            messagebox.showerror("Error", "Por favor seleccione un tipo de regresión")
            return
            
        n = len(self.DatosX)
        
        # Cálculos comunes
        sumx = sum(self.DatosX)
        sumy = sum(self.DatosY)
        sumxy = sum(x*y for x, y in zip(self.DatosX, self.DatosY))
        sumx2 = sum(x**2 for x in self.DatosX)
        promx = sumx/n
        promy = sumy/n
        St = sum((y - promy)**2 for y in self.DatosY)
        
        if regression_type == "Regresión Lineal":
            a1 = (n*sumxy - sumx*sumy)/(n*sumx2 - sumx**2)
            a0 = promy - a1*promx

            y_pred_original = [a0 + a1*x for x in self.DatosX]
            
            # Calcular error estándar y R²
            Sr = sum((y - (a0 + a1*x))**2 for x, y in zip(self.DatosX, self.DatosY))
            Syx = math.sqrt(Sr/(n-2))
            R2 = (St - Sr)/St
            r = math.sqrt(R2)
            
            std_dev = self.calculate_std_dev(self.DatosY, y_pred_original)
            # Graficar
            x_range = np.linspace(min(self.DatosX), max(self.DatosX), 100)
            y_pred = a0 + a1*x_range
            
            self.ax.plot(x_range, y_pred, 'r-', label='Regresión')
            self.ax.legend()
            self.canvas.draw()
            
            # Mostrar resultados
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"Regresión Lineal:\n")
            self.results_text.insert(tk.END, f"y = {a0:.4f} + {a1:.4f}x\n")
            self.results_text.insert(tk.END, f"Error estándar (Syx): {Syx:.4f}\n")
            self.results_text.insert(tk.END, f"Coeficiente de determinación (R²): {R2:.4f}\n")
            self.results_text.insert(tk.END, f"Coeficiente de correlación (r): {r:.4f}\n")
            self.results_text.insert(tk.END, f"Desviación estándar: {std_dev:.4f}\n")
        
        elif regression_type == "Modelo Exponencial":
            try:
                if any(y <= 0 for y in self.DatosY):
                    raise ValueError("Los valores de Y deben ser positivos para el modelo exponencial")
                
                logysum = sum(math.log(y) for y in self.DatosY)
                logyx = sum(math.log(y)*x for x, y in zip(self.DatosX, self.DatosY))
                ylogprom = logysum/n
                
                loga1 = (n*logyx - sumx*logysum)/(n*sumx2 - sumx**2)
                loga0 = ylogprom - loga1*promx
                
                alfa = math.exp(loga0)
                beta = loga1

                y_pred_original = [alfa*math.exp(beta*x) for x in self.DatosX]
                
                # Calcular error estándar y R²
                Sr = sum((y - alfa*math.exp(beta*x))**2 for x, y in zip(self.DatosX, self.DatosY))
                Syx = math.sqrt(Sr/(n-2))
                R2 = (St - Sr)/St
                r = math.sqrt(R2) if R2 > 0 else 0

                std_dev = self.calculate_std_dev(self.DatosY, y_pred_original)
                
                # Graficar
                x_range = np.linspace(min(self.DatosX), max(self.DatosX), 100)
                y_pred = alfa*np.exp(beta*x_range)
                
                self.ax.plot(x_range, y_pred, 'r-', label='Regresión')
                self.ax.legend()
                self.canvas.draw()
                
                # Mostrar resultados
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(tk.END, f"Modelo Exponencial:\n")
                self.results_text.insert(tk.END, f"y = {alfa:.4f}e^({beta:.4f}x)\n")
                self.results_text.insert(tk.END, f"Error estándar (Syx): {Syx:.4f}\n")
                self.results_text.insert(tk.END, f"Coeficiente de determinación (R²): {R2:.4f}\n")
                self.results_text.insert(tk.END, f"Coeficiente de correlación (r): {r:.4f}\n")
                self.results_text.insert(tk.END, f"Desviación estándar: {std_dev:.4f}\n")
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        elif regression_type == "Ecuación de Potencias":
            logx = [math.log(x) for x in self.DatosX]
            logy = [math.log(y) for y in self.DatosY]
            
            sumlogx = sum(logx)
            sumlogy = sum(logy)
            sumlogxlogy = sum(x*y for x, y in zip(logx, logy))
            sumlogx2 = sum(x**2 for x in logx)
            
            logxprom = sumlogx/n
            logyprom = sumlogy/n
            
            loga1 = (n*sumlogxlogy - sumlogx*sumlogy)/(n*sumlogx2 - sumlogx**2)
            loga0 = logyprom - loga1*logxprom
            
            alfa = math.exp(loga0)
            beta = loga1
            
            # Calcular error estándar y R²
            Sr = sum((y - alfa*(x**beta))**2 for x, y in zip(self.DatosX, self.DatosY))
            Syx = math.sqrt(Sr/(n-2))
            R2 = (St - Sr)/St
            r = math.sqrt(R2)
            
            # Graficar
            x_range = np.linspace(min(self.DatosX), max(self.DatosX), 100)
            y_pred = alfa*(x_range**beta)
            
            self.ax.plot(x_range, y_pred, 'r-', label='Regresión')
            self.ax.legend()
            self.canvas.draw()
            
            # Mostrar resultados
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"Ecuación de Potencias:\n")
            self.results_text.insert(tk.END, f"y = {alfa:.4f}x^({beta:.4f})\n")
            self.results_text.insert(tk.END, f"Error estándar (Syx): {Syx:.4f}\n")
            self.results_text.insert(tk.END, f"Coeficiente de determinación (R²): {R2:.4f}\n")
            self.results_text.insert(tk.END, f"Coeficiente de correlación (r): {r:.4f}\n")
            
        elif regression_type == "Razón de Crecimiento":
            try:
                if any(x <= 0 for x in self.DatosX) or any(y <= 0 for y in self.DatosY):
                    raise ValueError("Los valores de X e Y deben ser positivos para la razón de crecimiento")

                medioxsum = sum(1/x for x in self.DatosX)
                medioysum = sum(1/y for y in self.DatosY)
                medioxalados = sum((1/x)**2 for x in self.DatosX)
                medioyx = sum((1/x)*(1/y) for x, y in zip(self.DatosX, self.DatosY))

                medioxprom = medioxsum/n
                medioyprom = medioysum/n

                medioa1 = (n*medioyx - medioxsum*medioysum)/(n*medioxalados - medioxsum**2)
                medioa0 = medioyprom - medioa1*medioxprom

                mediobeta = 1/medioa0
                medioalfa = 1/medioa1

                # Calcular error estándar y R²
                Sr = sum((y - medioalfa*(x/mediobeta + x))**2 for x, y in zip(self.DatosX, self.DatosY))
                Syx = math.sqrt(Sr/(n-2))
                R2 = (St - Sr)/St
                r = math.sqrt(R2) if R2 > 0 else 0

                # Graficar
                x_range = np.linspace(min(self.DatosX), max(self.DatosX), 100)
                y_pred = medioalfa*(x_range/mediobeta + x_range)

                self.ax.plot(x_range, y_pred, 'r-', label='Regresión')
                self.ax.legend()
                self.canvas.draw()

                # Mostrar resultados
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(tk.END, f"Razón de Crecimiento:\n")
                self.results_text.insert(tk.END, f"y = {medioalfa:.4f}(x/{mediobeta:.4f} + x)\n")
                self.results_text.insert(tk.END, f"Error estándar (Syx): {Syx:.4f}\n")
                self.results_text.insert(tk.END, f"Coeficiente de determinación (R²): {R2:.4f}\n")
                self.results_text.insert(tk.END, f"Coeficiente de correlación (r): {r:.4f}\n")

            except ValueError as e:
                messagebox.showerror("Error", str(e))

        elif regression_type == "Regresión Polinomial":
            try:
                sumx3 = sum(x**3 for x in self.DatosX)
                sumx4 = sum(x**4 for x in self.DatosX)
                sumx2y = sum((x**2)*y for x, y in zip(self.DatosX, self.DatosY))

                # Matriz de coeficientes
                A = [
                    [n, sumx, sumx2, sumy],
                    [sumx, sumx2, sumx3, sumxy],
                    [sumx2, sumx3, sumx4, sumx2y]
                ]

                solutions = self.gauss_elimination(A)
                a0, a1, a2 = solutions

                # Calcular error estándar y R²
                Sr = sum((y - (a0 + a1*x + a2*x**2))**2 for x, y in zip(self.DatosX, self.DatosY))
                Syx = math.sqrt(Sr/(n-3))
                R2 = (St - Sr)/St
                r = math.sqrt(R2) if R2 > 0 else 0

                # Graficar
                x_range = np.linspace(min(self.DatosX), max(self.DatosX), 100)
                y_pred = a0 + a1*x_range + a2*x_range**2

                self.ax.plot(x_range, y_pred, 'r-', label='Regresión')
                self.ax.legend()
                self.canvas.draw()

                # Mostrar resultados
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(tk.END, f"Regresión Polinomial:\n")
                self.results_text.insert(tk.END, f"y = {a0:.4f} + {a1:.4f}x + {a2:.4f}x²\n")
                self.results_text.insert(tk.END, f"Error estándar (Syx): {Syx:.4f}\n")
                self.results_text.insert(tk.END, f"Coeficiente de determinación (R²): {R2:.4f}\n")
                self.results_text.insert(tk.END, f"Coeficiente de correlación (r): {r:.4f}\n")

            except Exception as e:
                messagebox.showerror("Error", "Error en el cálculo de la regresión polinomial")

    def gauss_elimination(self, matrix):
        matrix = [row[:] for row in matrix]
        rows = len(matrix)
        
        for i in range(rows):
            pivot = matrix[i][i]
            if pivot == 0:
                raise ValueError("El sistema no tiene solución única")
                
            for j in range(i, len(matrix[0])):
                matrix[i][j] /= pivot
            
            # Eliminación
            for k in range(i+1, rows):
                factor = matrix[k][i]
                for j in range(i, len(matrix[0])):
                    matrix[k][j] -= factor * matrix[i][j]
        
        # Sustitución hacia atrás
        solutions = [0] * rows
        for i in range(rows-1, -1, -1):
            solutions[i] = matrix[i][-1]
            for j in range(i+1, rows):
                solutions[i] -= matrix[i][j] * solutions[j]
        
        return solutions    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Analizador()
    app.run()