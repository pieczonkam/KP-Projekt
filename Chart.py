from includes import *

class Chart:
    def __init__(self, root_frame):
        self.is_open = False
        self.root_frame = root_frame
        self.chart_frame = ttk.Frame(self.root_frame)

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.chart_frame)
        self.canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)

        self.setChartParams()
        self.x_list = []
        self.y_list = []

    def setChartParams(self, title='', x_label='', y_label=''):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        
    def show(self):
        self.is_open = True
        self.chart_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def clear(self):
        self.is_open = False
        self.chart_frame.place_forget()
       
    def draw(self, new_val=None, t=None):
        self.ax.clear()
    
        if not isinstance(new_val, type(None)) and not isinstance(t, type(None)):
            if len(self.x_list) < Settings.CHART_DATA_LEN:
                self.x_list.append(t)
                self.y_list.append(new_val)
            else:
                self.x_list = self.x_list[1:] + [t]
                self.y_list = self.y_list[1:] + [new_val]
        self.ax.plot(self.x_list, self.y_list)

        self.ax.set_title(self.title, weight='bold')
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        self.ax.set_ylim((Settings.RANGE[0] - 0.1 * (Settings.RANGE[1] - Settings.RANGE[0]), Settings.RANGE[1] + 0.1 * (Settings.RANGE[1] - Settings.RANGE[0])))
        self.ax.grid(True, which='both')

        self.canvas.draw()

    def clearChart(self):
        self.x_list = []
        self.y_list = []
        self.draw()


if __name__ == '__main__':
    pass