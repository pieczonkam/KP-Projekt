from includes import *

class Chart:
    def __init__(self, root_frame):
        self.root_frame = root_frame
        self.chart_frame = ttk.Frame(self.root_frame)

        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self.chart_frame)
        self.canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)
    
    def draw(self):
        self.chart_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.plot(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20), label='f(x) = x')
        ax.plot(np.linspace(-5, 5, 100), np.sin(np.linspace(-5, 5, 100)), label='f(x) = sin(x)')
        ax.plot(np.linspace(-5, 5, 50), np.square(np.linspace(-5, 5, 50)), label='f(x) = $x^2$')

        ax.set_title('Przykładowy wykres', weight='bold')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True, which='both')
        
        self.canvas.draw()

    def clear(self):
        self.chart_frame.place_forget()

if __name__ == '__main__':
    pass