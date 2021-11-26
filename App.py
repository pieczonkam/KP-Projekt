from includes import *
from Chart import *
from TextBox import *

class App:
    '''
        Main application classa
    '''
    def __init__(self):
        self.width, self.height = Settings.WINDOW_MIN_SIZE
        self.menu_left_button_idx = self.menu_top_button_idx = -1
        self.measurement_type_text = ''

        # Main window
        self.window = tkinter.Tk()
        self.window.minsize(self.width, self.height)
        self.window.title(Settings.WINDOW_TITLE)
        self.window.protocol('WM_DELETE_WINDOW', self.window.destroy)

        # Frames
        self.menu_left_frame = ttk.Frame(self.window, style='FrameW.TFrame')
        self.menu_top_frame = ttk.Frame(self.window, style='FrameW.TFrame')
        self.main_frame = ttk.Frame(self.window, style='Frame.TFrame')
        self.info_frame = ttk.Frame(self.window, style='Frame.TFrame')

        # Labels
        self.menu_left_header_label = ttk.Label(self.menu_left_frame, text='Pomiar', anchor='center', style='Bold.TLabel')
        self.info_label = ttk.Label(self.info_frame, text='Obecne ustawienia: -', style='Normal.TLabel')
        
        # Buttons
        self.menu_left_buttons = [
            tkinter.Button(self.menu_left_frame, text='Temperatura', command=lambda: self.onClick('left', 0)),
            tkinter.Button(self.menu_left_frame, text='Nat. światła', command=lambda: self.onClick('left', 1)),
            tkinter.Button(self.menu_left_frame, text='Napięcie', command=lambda: self.onClick('left', 2)),
            tkinter.Button(self.menu_left_frame)
        ]

        self.menu_top_buttons = [
            tkinter.Button(self.menu_top_frame, text='Wykres', command=lambda: self.onClick('top', 0)),
            tkinter.Button(self.menu_top_frame, text='Tekst', command=lambda: self.onClick('top', 1)),
            tkinter.Button(self.menu_top_frame, text='Wyczyść', command=lambda: self.onClick('top', 2)),
            tkinter.Button(self.menu_top_frame)
        ]

        self.chart = Chart(self.main_frame)
        self.text_box = TextBox(self.main_frame)

    def onResize(self, _):
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        prev_width = self.width
        prev_height = self.height

        self.width = width if width >= Settings.WINDOW_MIN_SIZE[0] else prev_width
        self.height = height if height >= Settings.WINDOW_MIN_SIZE[1] else prev_height
        if self.width != prev_width or self.height != prev_height:
            self.replaceComponents()
        
    def onClick(self, menu_type, button_idx):
        self.setButtonActive(menu_type, button_idx)
        if menu_type == 'left':
            if button_idx == 0:
                self.measurement_type_text = 'Pomiar temperatury'
            elif button_idx == 1:
                self.measurement_type_text = 'Pomiar natężenia światła'
            elif button_idx == 2:
                self.measurement_type_text = 'Pomiar napięcia'
            else:
                self.measurement_type_text = '-'
            self.info_label['text'] = 'Obecne ustawienia: ' + self.measurement_type_text
        elif menu_type == 'top':
            if button_idx == 0:
                self.text_box.clear()
                self.chart.draw()
            elif button_idx == 1:
                self.chart.clear()
                self.text_box.draw()
            elif button_idx == 2:
                self.chart.clear()
                self.text_box.clear()
        
    def setButtonActive(self, menu_type, button_idx):
        if menu_type == 'left':
            self.menu_left_button_idx = button_idx
            for i, button in enumerate(self.menu_left_buttons[:-1]):
                if i != button_idx:
                    button.configure(bg=Settings.BUTTON_COLOR_DARK, state='normal')
            self.menu_left_buttons[button_idx].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK, state='disabled')
        elif menu_type == 'top':
            self.menu_top_button_idx = button_idx
            for i, button in enumerate(self.menu_top_buttons[:-1]):
                if i != button_idx:
                    button.configure(bg=Settings.BUTTON_COLOR_LIGHT, state='normal')
            if button_idx != 2:
                self.menu_top_buttons[button_idx].configure(bg=Settings.BUTTON_CLICKED_COLOR_LIGHT, state='disabled')
            else:
                self.menu_top_buttons[button_idx].configure(bg=Settings.BUTTON_COLOR_LIGHT, state='normal')

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

        # Buttons
        button_width, button_height = Settings.LEFT_MENU_BUTTON_SIZE
        for i, button in enumerate(self.menu_left_buttons[:-1]):
            button.place(x=0, y=Settings.TOP_MENU_HEIGHT + 2 + i * (button_height + 2), width=button_width, height=button_height)
        button_width, button_height = Settings.TOP_MENU_BUTTON_SIZE
        for i, button in enumerate(self.menu_top_buttons[:-1]):
            button.place(x=i * (button_width + 2), y=0, width=button_width, height=button_height)

    def replaceComponents(self):
        # Frames
        self.menu_left_frame.place(x=0, y=0, width=Settings.LEFT_MENU_WIDTH, height=self.height)
        self.menu_top_frame.place(x=Settings.LEFT_MENU_WIDTH, y=0, width=self.width - Settings.LEFT_MENU_WIDTH, height=Settings.TOP_MENU_HEIGHT)
        self.main_frame.place(x=Settings.LEFT_MENU_WIDTH, y=Settings.TOP_MENU_HEIGHT, width=self.width - Settings.LEFT_MENU_WIDTH, height=self.height - Settings.TOP_MENU_HEIGHT - Settings.INFO_HEIGHT)
        self.info_frame.place(x=Settings.LEFT_MENU_WIDTH, y=self.height - Settings.INFO_HEIGHT, width=self.width - Settings.LEFT_MENU_WIDTH, height=Settings.INFO_HEIGHT)        

        # Dummy button
        button_width, button_height = Settings.TOP_MENU_BUTTON_SIZE
        self.menu_top_buttons[-1].place(x=len(self.menu_top_buttons[:-1]) * (button_width + 2), y=0, width=self.width - Settings.LEFT_MENU_WIDTH - len(self.menu_top_buttons[:-1]) * (button_width + 2), height=button_height)
        button_width, button_height = Settings.LEFT_MENU_BUTTON_SIZE
        self.menu_left_buttons[-1].place(x=0, y=len(self.menu_left_buttons[:-1]) * (button_height + 2) + Settings.TOP_MENU_HEIGHT + 2, width=button_width, height=self.height - (Settings.TOP_MENU_HEIGHT + 2) - len(self.menu_left_buttons[:-1]) * (button_height + 2))

        # TextBox
        self.window.update()
        self.text_box.redraw((self.main_frame.winfo_width(), self.main_frame.winfo_height()))

    def setStyle(self):
        # Style ttk widgets
        style = ttk.Style()
        style.configure('Frame.TFrame', background=Settings.FRAME_COLOR)
        style.configure('FrameW.TFrame', background='white')
        style.configure('Bold.TLabel', background=Settings.FRAME_COLOR, foreground=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_BOLD_20)
        style.configure('Normal.TLabel', background=Settings.FRAME_COLOR, foreground=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_NORMAL_14)

        # Style tk widgets
        for button in self.menu_left_buttons[:-1]:
            button.configure(bg=Settings.BUTTON_COLOR_DARK, fg=Settings.TEXT_COLOR, activebackground=Settings.BUTTON_ACTIVE_COLOR_DARK, activeforeground=Settings.TEXT_COLOR, disabledforeground=Settings.TEXT_COLOR, borderwidth=0, font=Settings.FONT_HELVETICA_BOLD_16)
        self.menu_left_buttons[-1].configure(bg=Settings.BUTTON_COLOR_DARK, fg=Settings.TEXT_COLOR, borderwidth=0, state='disabled')
        for button in self.menu_top_buttons[:-1]:
            button.configure(bg=Settings.BUTTON_COLOR_LIGHT, fg=Settings.TEXT_COLOR, activebackground=Settings.BUTTON_ACTIVE_COLOR_LIGHT, activeforeground=Settings.TEXT_COLOR, disabledforeground=Settings.TEXT_COLOR, borderwidth=0, font=Settings.FONT_HELVETICA_BOLD_16)
        self.menu_top_buttons[-1].configure(bg=Settings.BUTTON_COLOR_LIGHT, fg=Settings.TEXT_COLOR, borderwidth=0, state='disabled')

        self.text_box.configure(wrap=tkinter.WORD, bg=Settings.TEXTBOX_COLOR, fg=Settings.TEXT_COLOR, font=Settings.FONT_HELVETICA_NORMAL_10, borderwidth=0)

    def setBinding(self):
        self.window.bind('<Configure>', self.onResize)
        #self.window.bind('<Key>', self.printChildren)

        self.menu_left_buttons[0].bind('<Enter>', lambda _: self.menu_left_buttons[0].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_button_idx == 0 else self.menu_left_buttons[0].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_buttons[0].bind('<Leave>', lambda _: self.menu_left_buttons[0].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_button_idx == 0 else self.menu_left_buttons[0].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.menu_left_buttons[1].bind('<Enter>', lambda _: self.menu_left_buttons[1].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_button_idx == 1 else self.menu_left_buttons[1].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_buttons[1].bind('<Leave>', lambda _: self.menu_left_buttons[1].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_button_idx == 1 else self.menu_left_buttons[1].configure(bg=Settings.BUTTON_COLOR_DARK))
        self.menu_left_buttons[2].bind('<Enter>', lambda _: self.menu_left_buttons[2].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_button_idx == 2 else self.menu_left_buttons[2].configure(bg=Settings.BUTTON_HOVER_COLOR_DARK))
        self.menu_left_buttons[2].bind('<Leave>', lambda _: self.menu_left_buttons[2].configure(bg=Settings.BUTTON_CLICKED_COLOR_DARK) if self.menu_left_button_idx == 2 else self.menu_left_buttons[2].configure(bg=Settings.BUTTON_COLOR_DARK))

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
        app.window.mainloop()
    except Exception as e:
        print(e)
        input()