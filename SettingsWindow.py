from tkinter import Variable
from includes import *

class SettingsWindow:
    def __init__(self, root, width, height, app):
        self.root = root
        self.width = width
        self.height = height
        self.app = app

    def show(self):
        posx = self.root.winfo_x() + (self.root.winfo_width() - self.width) / 2 
        posy = self.root.winfo_y() + (self.root.winfo_height() - self.height) / 2
        self.window = tkinter.Toplevel(self.root)
        self.window.geometry('%dx%d+%d+%d' % (self.width, self.height, posx, posy))
        self.window.resizable(0, 0)
        self.window.title('Ustawienia')
        self.window.iconbitmap(utils.resourcePath('applogo.ico'))
        self.window.grab_set()

        # StringVars
        self.unit_var = tkinter.StringVar(value=Settings.UNIT)
        self.range_min_var = tkinter.StringVar(value=Settings.RANGE[0])
        self.range_max_var = tkinter.StringVar(value=Settings.RANGE[1])
        self.measurement_type_var = tkinter.StringVar(value=Settings.MEASUREMENT_TYPE)

        # Frames
        self.entries_frame = ttk.Frame(self.window, style='Frame.TFrame')
        self.button_frame = ttk.Frame(self.window, style='WFrame.TFrame')
        entries_frame_height = self.height - Settings.SETTINGS_WINDOW_BUTTON_FRAME_HEIGHT
        self.entries_frame.place(x=0, y=0, width=self.width, height=entries_frame_height)
        self.button_frame.place(x=0, y=entries_frame_height, width=self.width, height=Settings.SETTINGS_WINDOW_BUTTON_FRAME_HEIGHT)

        # Buttons
        self.buttons = [
            tkinter.Button(self.button_frame, text='Zapisz', command=self.overwriteValues),
            tkinter.Button(self.button_frame, text='Reset', command=self.resetValues),
            tkinter.Button(self.button_frame, text='Anuluj', command=self.window.destroy)
        ]
        for i, button in enumerate(self.buttons):
            button.place(x=i * (2 + Settings.SETTINGS_WINDOW_BUTTON_WIDTH), y=2, width=Settings.SETTINGS_WINDOW_BUTTON_WIDTH, height=Settings.SETTINGS_WINDOW_BUTTON_FRAME_HEIGHT - 2)
        
        # Labels 
        self.labels = [
            ttk.Label(self.entries_frame, text='Jednostka:', style='Normal_12.TLabel', anchor='e'),
            ttk.Label(self.entries_frame, text='Zakres wartości (min):', style='Normal_12.TLabel', anchor='e'),
            ttk.Label(self.entries_frame, text='Zakres wartości (max):', style='Normal_12.TLabel', anchor='e'),
            ttk.Label(self.entries_frame, text='Typ pomiaru (opcja "Inne"):', style='Normal_12.TLabel', anchor='e')
        ]
        for i, label in enumerate(self.labels):
            label.place(x=5, y=i * entries_frame_height / 4, width=0.65 * self.width - 10, height=entries_frame_height / 4)
        
        # Entries
        self.entries = [
            tkinter.Entry(self.entries_frame, textvariable=self.unit_var, justify='right'),
            tkinter.Entry(self.entries_frame, textvariable=self.range_min_var, justify='right'),
            tkinter.Entry(self.entries_frame, textvariable=self.range_max_var, justify='right'),
            tkinter.Entry(self.entries_frame, textvariable=self.measurement_type_var, justify='right')
        ]
        for i, entry in enumerate(self.entries):
            entry.place(x=5 + 0.65 * self.width, y=(entries_frame_height / 4 - Settings.SETTINGS_WINDOW_ENTRY_HEIGHT) / 2 + i * entries_frame_height / 4, width=0.35 * self.width - 10, height=Settings.SETTINGS_WINDOW_ENTRY_HEIGHT)

        self.setStyle()
        self.setBinding()

    def resetValues(self):
        self.unit_var.set(Settings.UNIT_DEFAULT)
        self.range_min_var.set(Settings.RANGE_DEFAULT[0])
        self.range_max_var.set(Settings.RANGE_DEFAULT[1])
        self.measurement_type_var.set(Settings.MEASUREMENT_TYPE_DEFAULT)
        
    def overwriteValues(self):
        range_min = None
        range_max = None
        range_min_prev = Settings.RANGE[0]
        range_max_prev = Settings.RANGE[1]

        try:
            range_min = float(self.range_min_var.get())
        except Exception:
            self.entries[1].configure(highlightbackground = Settings.ENTRY_BORDER_ERROR_COLOR, highlightcolor=Settings.ENTRY_BORDER_ERROR_COLOR)
        try:
            range_max = float(self.range_max_var.get())
        except Exception:
            self.entries[2].configure(highlightbackground = Settings.ENTRY_BORDER_ERROR_COLOR, highlightcolor=Settings.ENTRY_BORDER_ERROR_COLOR)
        
        if not isinstance(range_min, type(None)):
            self.entries[1].configure(highlightbackground = Settings.ENTRY_BORDER_NORMAL_COLOR, highlightcolor=Settings.ENTRY_BORDER_NORMAL_COLOR)
        if not isinstance(range_max, type(None)):
            self.entries[2].configure(highlightbackground = Settings.ENTRY_BORDER_NORMAL_COLOR, highlightcolor=Settings.ENTRY_BORDER_NORMAL_COLOR)

        if not isinstance(range_min, type(None)) and not isinstance(range_max, type(None)):
            Settings.UNIT = self.unit_var.get()
            Settings.RANGE[0] = range_min
            Settings.RANGE[1] = range_max
            Settings.MEASUREMENT_TYPE = self.measurement_type_var.get()
                        
            if self.app.menu_left_upper_button_idx == 0:
                self.app.chart.setChartParams('Odczyt temperatury', 'Czas [s]', 'Temperatura [%s]' % Settings.UNIT)
            elif self.app.menu_left_upper_button_idx == 1:
                self.app.chart.setChartParams('Odczyt natężenia światła', 'Czas [s]', 'Natężenie światła [%s]' % Settings.UNIT)
            elif self.app.menu_left_upper_button_idx == 2:
                self.app.chart.setChartParams('Odczyt napięcia Halla', 'Czas [s]', 'Napięcie [%s]' % Settings.UNIT)
            elif self.app.menu_left_upper_button_idx == 3:
                self.app.chart.setChartParams('Detekcja dotyku', 'Czas [s]', 'Wartość sygnału [%s]' % Settings.UNIT)
            elif self.app.menu_left_upper_button_idx == 4:
                self.app.chart.setChartParams(Settings.MEASUREMENT_TYPE, 'Czas [s]', 'Wartość sygnału [%s]' % Settings.UNIT)

            self.app.mapValues(range_min_prev, range_max_prev)
            self.app.text_box.setTextFromDict(self.app.time_val_dict)
            self.app.chart.draw()
            self.window.destroy()

    def setStyle(self):
        for button in self.buttons:
            button.configure(bg=Settings.BUTTON_COLOR_DARK, fg=Settings.TEXT_COLOR, activebackground=Settings.BUTTON_ACTIVE_COLOR_DARK, activeforeground=Settings.TEXT_COLOR, disabledforeground=Settings.TEXT_COLOR, borderwidth=0, font=Settings.FONT_HELVETICA_BOLD_16)
        for entry in self.entries:
            entry.configure(bg=Settings.ENTRY_BG_COLOR, fg=Settings.TEXT_COLOR, insertbackground=Settings.TEXT_COLOR, selectbackground=Settings.ENTRY_SELECTED_TEXT_COLOR, highlightbackground = Settings.ENTRY_BORDER_NORMAL_COLOR, highlightcolor=Settings.ENTRY_BORDER_NORMAL_COLOR, highlightthickness=2, bd=0)

    def setBinding(self):
        self.buttons[0].bind('<Enter>', lambda _: self.buttons[0].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.buttons[0].bind('<Leave>', lambda _: self.buttons[0].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.buttons[1].bind('<Enter>', lambda _: self.buttons[1].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.buttons[1].bind('<Leave>', lambda _: self.buttons[1].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.buttons[2].bind('<Enter>', lambda _: self.buttons[2].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.buttons[2].bind('<Leave>', lambda _: self.buttons[2].configure(bg=Settings.BUTTON_COLOR_DARK))

if __name__ == '__main__':
    pass