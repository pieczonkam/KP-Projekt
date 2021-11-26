from includes import *
from Chart import *
from TextBox import *

class App:
    '''
        Main application class
    '''
    def __init__(self):
        self.width, self.height = Settings.WINDOW_MIN_SIZE
        self.menu_left_upper_button_idx = self.menu_top_button_idx = -1
        self.menu_left_lower_button_idx = 1
        self.info_text = 'Nie połączono'

        # Main window
        self.window = tkinter.Tk()
        self.window.geometry('+%i+%i' % ((self.window.winfo_screenwidth() - self.width) / 2, (self.window.winfo_screenheight() - self.height) / 2))
        self.window.minsize(self.width, self.height)
        self.window.title(Settings.WINDOW_TITLE)
        self.window.protocol('WM_DELETE_WINDOW', self.onExit)

        # Frames
        self.menu_left_upper_frame = ttk.Frame(self.window, style='FrameW.TFrame')
        self.menu_left_lower_frame = ttk.Frame(self.window, style='FrameW.TFrame')
        self.menu_top_frame = ttk.Frame(self.window, style='FrameW.TFrame')
        self.main_frame = ttk.Frame(self.window, style='Frame.TFrame')
        self.info_frame = ttk.Frame(self.window, style='Frame.TFrame')

        # Labels
        self.menu_left_header_label = ttk.Label(self.menu_left_upper_frame, text='Pomiar', anchor='center', style='Bold_20.TLabel')
        self.info_label = ttk.Label(self.info_frame, text=self.info_text, style='Normal.TLabel')
        self.pin_type_label = ttk.Label(self.menu_left_lower_frame, text=' Rodzaj pinu:', anchor='w', style='Bold_16.TLabel')
        self.pin_nmb_label = ttk.Label(self.menu_left_lower_frame, text=' Numer pinu:', anchor='w', style='Bold_16.TLabel')
        
        # OptionMenus
        self.pin_type_values = ['Analog', 'Digital']
        self.pin_type_var = tkinter.StringVar(value=self.pin_type_values[0])
        self.pin_type_om = ttk.OptionMenu(self.menu_left_lower_frame, self.pin_type_var, self.pin_type_values[0], *self.pin_type_values, command=self.onPinTypeChange)
        
        self.pin_nmb_values_dict = {'analog': ['A' + str(i) for i in range(Settings.PIN_ANALOG_COUNT)], 'digital': ['D' + str(i) for i in range(Settings.PIN_DIGITAL_COUNT)]}
        self.pin_nmb_values = self.pin_nmb_values_dict['analog']
        self.pin_nmb_prev_values = {'analog': self.pin_nmb_values_dict['analog'][0], 'digital': self.pin_nmb_values_dict['digital'][0]}
        self.pin_nmb_var = tkinter.StringVar(value=self.pin_nmb_values[0])
        self.pin_nmb_var.trace('w', self.onPinNmbChange)
        self.pin_nmb_om = ttk.OptionMenu(self.menu_left_lower_frame, self.pin_nmb_var)
        for pin_nmb in self.pin_nmb_values:
                self.pin_nmb_om['menu'].add_radiobutton(label=pin_nmb, variable=self.pin_nmb_var)

        # Buttons
        self.menu_left_upper_buttons = [
            tkinter.Button(self.menu_left_upper_frame, text='Temperatura', command=lambda: self.onClick('left top', 0)),
            tkinter.Button(self.menu_left_upper_frame, text='Nat. światła', command=lambda: self.onClick('left top', 1)),
            tkinter.Button(self.menu_left_upper_frame, text='Napięcie Halla', command=lambda: self.onClick('left top', 2)),
            tkinter.Button(self.menu_left_upper_frame, text='Dotyk', command=lambda: self.onClick('left top', 3)),
            tkinter.Button(self.menu_left_upper_frame)
        ]

        self.menu_left_lower_buttons = [
            tkinter.Button(self.menu_left_lower_frame, text='Połącz', command=lambda: self.onClick('left bottom', 0)),
            tkinter.Button(self.menu_left_lower_frame, text='Rozłącz', command=lambda: self.onClick('left bottom', 1))
        ]

        self.menu_top_buttons = [
            tkinter.Button(self.menu_top_frame, text='Wykres', command=lambda: self.onClick('top', 0)),
            tkinter.Button(self.menu_top_frame, text='Sygnał', command=lambda: self.onClick('top', 1)),
            tkinter.Button(self.menu_top_frame, text='Wyczyść', command=lambda: self.onClick('top', 2)),
            tkinter.Button(self.menu_top_frame)
        ]

        # Objects of user-defined classes
        self.chart = Chart(self.main_frame)
        self.text_box = TextBox(self.main_frame)
    
    def onExit(self):
        print('Active threads count:', threading.active_count())
        for thread in threading.enumerate():
            print(thread)
        self.window.destroy()

    def onPinTypeChange(self, val):
        if val in ['Analog', 'Digital']:
            val = val.lower()
            self.pin_nmb_values = self.pin_nmb_values_dict[val]
            self.pin_nmb_var.set(self.pin_nmb_prev_values[val])

            self.pin_nmb_om['menu'].delete(0, tkinter.END)
            for pin_nmb in self.pin_nmb_values:
                self.pin_nmb_om['menu'].add_radiobutton(label=pin_nmb, variable=self.pin_nmb_var)

    def onPinNmbChange(self, *args):
        self.pin_nmb_prev_values[self.pin_type_var.get().lower()] = self.pin_nmb_var.get()

    def onResize(self, _):
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        prev_width = self.width
        prev_height = self.height

        self.width = width if width >= Settings.WINDOW_MIN_SIZE[0] else prev_width
        self.height = height if height >= Settings.WINDOW_MIN_SIZE[1] else prev_height
        if self.width != prev_width or self.height != prev_height:
            self.window.geometry('%ix%i' % (self.width, self.height))
            self.replaceComponents()

    def onClick(self, menu_type, button_idx):
        self.setButtonActive(menu_type, button_idx)
        if menu_type == 'left top':
            if button_idx == 0:
                self.chart.setChartParams('Odczyt temperatury', 'Czas [s]', 'Temperatura []')
            elif button_idx == 1:
                self.chart.setChartParams('Odczyt natężenia światła', 'Czas [s]', 'Natężenie światła []')
            elif button_idx == 2:
                self.chart.setChartParams('Odczyt napięcia Halla', 'Czas [s]', 'Napięcie []')
            elif button_idx == 3:
                self.chart.setChartParams('Detekcja dotyku', 'Czas [s]', 'Stan')
        elif menu_type == 'left bottom':
            if button_idx == 0:
                self.info_text = 'Połączono z Arduino na porcie COM6'
            if button_idx == 1:
                self.info_text = 'Nie połączono'
            self.info_label['text'] = self.info_text
        elif menu_type == 'top':
            if button_idx == 0:
                self.text_box.clear()
                self.chart.show()
            elif button_idx == 1:
                self.chart.clear()
                self.text_box.show()
            elif button_idx == 2:
                if self.chart.is_open:
                    self.chart.clearChart()
                elif self.text_box.is_open:
                    self.text_box.clearText()
        
    def setButtonActive(self, menu_type, button_idx):
        if menu_type == 'left top':
            self.menu_left_upper_button_idx = button_idx
            for i, button in enumerate(self.menu_left_upper_buttons[:-1]):
                if i != button_idx:
                    button.configure(bg=Settings.BUTTON_COLOR_DARK, state='normal')
            self.menu_left_upper_buttons[button_idx].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK, state='disabled')
        if menu_type == 'left bottom':
            self.menu_left_lower_button_idx = button_idx
            for i, button in enumerate(self.menu_left_lower_buttons):
                if i != button_idx:
                    button.configure(bg=Settings.BUTTON_COLOR_DARK, state='normal')
            self.menu_left_lower_buttons[button_idx].configure(bg=Settings.BUTTON_DISABLED_COLOR_DARK, state='disabled')
        elif menu_type == 'top':
            if button_idx != 2:
                self.menu_top_button_idx = button_idx
                for i, button in enumerate(self.menu_top_buttons[:-1]):
                    if i != button_idx:
                        button.configure(bg=Settings.BUTTON_COLOR_LIGHT, state='normal')
                self.menu_top_buttons[button_idx].configure(bg=Settings.BUTTON_CLICKED_COLOR_LIGHT, state='disabled')
    
    def placeComponents(self):
        self.replaceComponents()

        # Separators
        ttk.Separator(self.menu_top_frame, orient='vertical', style='Sep.TSeparator').place(x=0, y=0, relheight=1)
        ttk.Separator(self.main_frame, orient='vertical', style='Sep.TSeparator').place(x=0, y=0, relheight=1)
        ttk.Separator(self.info_frame, orient='vertical', style='Sep.TSeparator').place(x=0, y=0, relheight=1)
        ttk.Separator(self.main_frame, orient='horizontal', style='Sep.TSeparator').place(x=2, y=0, relwidth=1)
        ttk.Separator(self.info_frame, orient='horizontal', style='Sep.TSeparator').place(x=2, y=0, relwidth=1)

        # Labels
        self.menu_left_header_label.place(x=0, y=0, width=Settings.LEFT_MENU_HEADER_WIDTH, height=Settings.TOP_MENU_HEIGHT)
        self.info_label.place(x=10, y=7)
        self.pin_type_label.place(x=0, y=2, width=Settings.LEFT_MENU_WIDTH, height=Settings.LEFT_MENU_LOWER_ITEM_HEIGHT)
        self.pin_nmb_label.place(x=0, y=6 + 2 * Settings.LEFT_MENU_LOWER_ITEM_HEIGHT, width=Settings.LEFT_MENU_WIDTH, height=Settings.LEFT_MENU_LOWER_ITEM_HEIGHT)

        # OptionMenus
        self.pin_type_om.place(x=0, y=4 + Settings.LEFT_MENU_LOWER_ITEM_HEIGHT, width=Settings.LEFT_MENU_WIDTH, height=Settings.LEFT_MENU_LOWER_ITEM_HEIGHT)
        self.pin_nmb_om.place(x=0, y=8 + 3 * Settings.LEFT_MENU_LOWER_ITEM_HEIGHT, width=Settings.LEFT_MENU_WIDTH, height=Settings.LEFT_MENU_LOWER_ITEM_HEIGHT)

        # Buttons
        button_width, button_height = Settings.LEFT_MENU_UPPER_BUTTON_SIZE
        for i, button in enumerate(self.menu_left_upper_buttons[:-1]):
            button.place(x=0, y=Settings.TOP_MENU_HEIGHT + 2 + i * (button_height + 2), width=button_width, height=button_height)
        button_width, button_height = Settings.LEFT_MENU_LOWER_BUTTON_SIZE
        for i, button in enumerate(self.menu_left_lower_buttons):
            button.place(x=0, y=10 + 4 * Settings.LEFT_MENU_LOWER_ITEM_HEIGHT + i * (button_height + 2), width=button_width, height=button_height)
        button_width, button_height = Settings.TOP_MENU_BUTTON_SIZE
        for i, button in enumerate(self.menu_top_buttons[:-1]):
            button.place(x=i * (button_width + 2), y=0, width=button_width, height=button_height)

    def replaceComponents(self):
        # Frames
        self.menu_left_upper_frame.place(x=0, y=0, width=Settings.LEFT_MENU_WIDTH, height=self.height - Settings.LEFT_MENU_LOWER_HEIGHT)
        self.menu_left_lower_frame.place(x=0, y=self.height - Settings.LEFT_MENU_LOWER_HEIGHT, width=Settings.LEFT_MENU_WIDTH, height=Settings.LEFT_MENU_LOWER_HEIGHT)
        self.menu_top_frame.place(x=Settings.LEFT_MENU_WIDTH, y=0, width=self.width - Settings.LEFT_MENU_WIDTH, height=Settings.TOP_MENU_HEIGHT)
        self.main_frame.place(x=Settings.LEFT_MENU_WIDTH, y=Settings.TOP_MENU_HEIGHT, width=self.width - Settings.LEFT_MENU_WIDTH, height=self.height - Settings.TOP_MENU_HEIGHT - Settings.INFO_HEIGHT)
        self.info_frame.place(x=Settings.LEFT_MENU_WIDTH, y=self.height - Settings.INFO_HEIGHT, width=self.width - Settings.LEFT_MENU_WIDTH, height=Settings.INFO_HEIGHT)        

        # Dummy button
        button_width, button_height = Settings.TOP_MENU_BUTTON_SIZE
        self.menu_top_buttons[-1].place(x=len(self.menu_top_buttons[:-1]) * (button_width + 2), y=0, width=self.width - Settings.LEFT_MENU_WIDTH - len(self.menu_top_buttons[:-1]) * (button_width + 2), height=button_height)
        button_width, button_height = Settings.LEFT_MENU_UPPER_BUTTON_SIZE
        self.menu_left_upper_buttons[-1].place(x=0, y=len(self.menu_left_upper_buttons[:-1]) * (button_height + 2) + Settings.TOP_MENU_HEIGHT + 2, width=button_width, height=self.height - (Settings.TOP_MENU_HEIGHT + 2) - len(self.menu_left_upper_buttons[:-1]) * (button_height + 2))

        # TextBox
        self.window.update()
        self.text_box.redraw((self.main_frame.winfo_width(), self.main_frame.winfo_height()))

    def setStyle(self):
        # Style ttk widgets
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Frame.TFrame', background=Settings.FRAME_COLOR)
        style.configure('FrameW.TFrame', background='white')
        style.configure('Bold_20.TLabel', background=Settings.FRAME_COLOR, foreground=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_BOLD_20)
        style.configure('Bold_16.TLabel', background=Settings.FRAME_COLOR, foreground=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_BOLD_16)
        style.configure('Normal.TLabel', background=Settings.FRAME_COLOR, foreground=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_NORMAL_14)
        style.configure('TMenubutton', relief=tkinter.FLAT, background=Settings.BUTTON_COLOR_DARK, foreground=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_BOLD_16, arrowcolor=Settings.TEXT_COLOR, bd=0, highlightthickness=0)
        style.map('TMenubutton', background=[('pressed', Settings.BUTTON_HOVER_COLOR_DARK), ('active', Settings.BUTTON_HOVER_COLOR_DARK)])
        for om in [self.pin_type_om, self.pin_nmb_om]:
            om['menu'].configure(relief=tkinter.FLAT, font=Settings.FONT_HELVETICA_NORMAL_10, borderwidth=1, activeborderwidth=5, foreground=Settings.TEXT_COLOR, background=Settings.BUTTON_COLOR_DARK, activebackground=Settings.BUTTON_CLICKED_COLOR_DARK, selectcolor=Settings.TEXT_COLOR)
        
        # Style tk widgets
        for button in self.menu_left_upper_buttons[:-1]:
            button.configure(bg=Settings.BUTTON_COLOR_DARK, fg=Settings.TEXT_COLOR, activebackground=Settings.BUTTON_ACTIVE_COLOR_DARK, activeforeground=Settings.TEXT_COLOR, disabledforeground=Settings.TEXT_COLOR, borderwidth=0, font=Settings.FONT_HELVETICA_BOLD_16)
        self.menu_left_upper_buttons[-1].configure(bg=Settings.BUTTON_COLOR_DARK, fg=Settings.TEXT_COLOR, borderwidth=0, state='disabled')
        for i, button in enumerate(self.menu_left_lower_buttons):
            if i != self.menu_left_lower_button_idx:
                button.configure(bg=Settings.BUTTON_COLOR_DARK, fg=Settings.TEXT_COLOR, activebackground=Settings.BUTTON_ACTIVE_COLOR_DARK, activeforeground=Settings.TEXT_COLOR, disabledforeground=Settings.TEXT_DISABLED_COLOR, borderwidth=0, font=Settings.FONT_HELVETICA_BOLD_16)
        self.menu_left_lower_buttons[self.menu_left_lower_button_idx].configure(bg=Settings.BUTTON_DISABLED_COLOR_DARK, fg=Settings.TEXT_COLOR, activebackground=Settings.BUTTON_ACTIVE_COLOR_DARK, activeforeground=Settings.TEXT_COLOR, disabledforeground=Settings.TEXT_DISABLED_COLOR, borderwidth=0, font=Settings.FONT_HELVETICA_BOLD_16, state='disabled')
        for button in self.menu_top_buttons[:-1]:
            button.configure(bg=Settings.BUTTON_COLOR_LIGHT, fg=Settings.TEXT_COLOR, activebackground=Settings.BUTTON_ACTIVE_COLOR_LIGHT, activeforeground=Settings.TEXT_COLOR, disabledforeground=Settings.TEXT_COLOR, borderwidth=0, font=Settings.FONT_HELVETICA_BOLD_16)
        self.menu_top_buttons[-1].configure(bg=Settings.BUTTON_COLOR_LIGHT, fg=Settings.TEXT_COLOR, borderwidth=0, state='disabled')
        
        self.text_box.configure(wrap=tkinter.WORD, bg=Settings.TEXTBOX_COLOR, fg=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_NORMAL_10, borderwidth=0)

    def setBinding(self):
        self.window.bind('<Configure>', self.onResize)
        # self.window.bind('<Key>', self.printChildren)

        # Left upper menu
        self.menu_left_upper_buttons[0].bind('<Enter>', lambda _: self.menu_left_upper_buttons[0].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 0 else self.menu_left_upper_buttons[0].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_upper_buttons[0].bind('<Leave>', lambda _: self.menu_left_upper_buttons[0].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 0 else self.menu_left_upper_buttons[0].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.menu_left_upper_buttons[1].bind('<Enter>', lambda _: self.menu_left_upper_buttons[1].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 1 else self.menu_left_upper_buttons[1].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_upper_buttons[1].bind('<Leave>', lambda _: self.menu_left_upper_buttons[1].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 1 else self.menu_left_upper_buttons[1].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.menu_left_upper_buttons[2].bind('<Enter>', lambda _: self.menu_left_upper_buttons[2].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 2 else self.menu_left_upper_buttons[2].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_upper_buttons[2].bind('<Leave>', lambda _: self.menu_left_upper_buttons[2].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 2 else self.menu_left_upper_buttons[2].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.menu_left_upper_buttons[3].bind('<Enter>', lambda _: self.menu_left_upper_buttons[3].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 3 else self.menu_left_upper_buttons[3].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_upper_buttons[3].bind('<Leave>', lambda _: self.menu_left_upper_buttons[3].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_upper_button_idx == 3 else self.menu_left_upper_buttons[3].configure(bg=Settings.BUTTON_COLOR_DARK))

        # Left lower menu
        self.menu_left_lower_buttons[0].bind('<Enter>', lambda _: self.menu_left_lower_buttons[0].configure(bg=Settings.BUTTON_DISABLED_COLOR_DARK) if self.menu_left_lower_button_idx == 0 else self.menu_left_lower_buttons[0].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_lower_buttons[0].bind('<Leave>', lambda _: self.menu_left_lower_buttons[0].configure(bg=Settings.BUTTON_DISABLED_COLOR_DARK) if self.menu_left_lower_button_idx == 0 else self.menu_left_lower_buttons[0].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.menu_left_lower_buttons[1].bind('<Enter>', lambda _: self.menu_left_lower_buttons[1].configure(bg=Settings.BUTTON_DISABLED_COLOR_DARK) if self.menu_left_lower_button_idx == 1 else self.menu_left_lower_buttons[1].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_lower_buttons[1].bind('<Leave>', lambda _: self.menu_left_lower_buttons[1].configure(bg=Settings.BUTTON_DISABLED_COLOR_DARK) if self.menu_left_lower_button_idx == 1 else self.menu_left_lower_buttons[1].configure(bg=Settings.BUTTON_COLOR_DARK))

        # Top menu
        self.menu_top_buttons[0].bind('<Enter>', lambda _: self.menu_top_buttons[0].configure(bg=Settings.BUTTON_CLICKED_COLOR_LIGHT) if self.menu_top_button_idx == 0 else self.menu_top_buttons[0].configure(bg=Settings.BUTTON_HOVER_COLOR_LIGHT))
        self.menu_top_buttons[0].bind('<Leave>', lambda _: self.menu_top_buttons[0].configure(bg=Settings.BUTTON_CLICKED_COLOR_LIGHT) if self.menu_top_button_idx == 0 else self.menu_top_buttons[0].configure(bg=Settings.BUTTON_COLOR_LIGHT))
        self.menu_top_buttons[1].bind('<Enter>', lambda _: self.menu_top_buttons[1].configure(bg=Settings.BUTTON_CLICKED_COLOR_LIGHT) if self.menu_top_button_idx == 1 else self.menu_top_buttons[1].configure(bg=Settings.BUTTON_HOVER_COLOR_LIGHT))
        self.menu_top_buttons[1].bind('<Leave>', lambda _: self.menu_top_buttons[1].configure(bg=Settings.BUTTON_CLICKED_COLOR_LIGHT) if self.menu_top_button_idx == 1 else self.menu_top_buttons[1].configure(bg=Settings.BUTTON_COLOR_LIGHT))
        self.menu_top_buttons[2].bind('<Enter>', lambda _: self.menu_top_buttons[2].configure(bg=Settings.BUTTON_HOVER_COLOR_LIGHT))
        self.menu_top_buttons[2].bind('<Leave>', lambda _: self.menu_top_buttons[2].configure(bg=Settings.BUTTON_COLOR_LIGHT))
       
    def printChildren(self, event):
        '''
            Method prints all child elements of created frames when 'W' is pressed (for debug purposes)
        '''
        if event.keycode == 87:
            for child in self.window.winfo_children():
                print(child)
                for child_child in child.winfo_children():
                    print('\t', child_child)


if __name__ == '__main__':
    try:
        app = App()
        app.placeComponents()
        app.setStyle()
        app.setBinding()
        ani = animation.FuncAnimation(app.chart.figure, app.chart.draw, interval=500)
        app.window.mainloop()
    except Exception as e:
        print('Exception:', e)
        input()