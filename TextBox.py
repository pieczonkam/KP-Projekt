from includes import *

class TextBox:
    def __init__(self, root_frame):
        self.is_open = False
        self.root_frame = root_frame
        self.text_box_frame = ttk.Frame(self.root_frame, style='Frame.TFrame')
        self.text_box = scrolledtext.ScrolledText(self.text_box_frame)

        self.setText('Czas [s]\t\t\tWartość\n')

    def show(self):
        self.is_open = True
        self.text_box_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def clear(self):
        self.is_open = False
        self.text_box_frame.place_forget()

    def redraw(self, size):
        self.text_box.place(x=Settings.TEXTBOX_LEFT_MARGIN, y=0, width=size[0] - Settings.TEXTBOX_LEFT_MARGIN, height=size[1])

    def configure(self, **kwargs):
        self.text_box.configure(kwargs)

    def scrollToBottom(self):
        self.text_box.see(tkinter.END)

    def setText(self, text):
        self.text_box.configure(state='normal')
        self.text_box.delete(1.0, tkinter.END)
        self.text_box.insert(tkinter.INSERT, '\n' + text)
        self.text_box.configure(state='disabled')

    def setTextFromDict(self, time_val_dict):
        self.text_box.configure(state='normal')
        self.text_box.delete(4.0, tkinter.END)
        for i in range(len(time_val_dict['time'])):
            self.text_box.insert(tkinter.END, '\n%.1f\t\t\t%.2f %s' % (time_val_dict['time'][i], round(time_val_dict['val'][i], 2), Settings.UNIT))
        self.text_box.configure(state='disabled')

    def appendText(self, text, newline=True):
        if newline:
            text = '\n' + text
        self.text_box.configure(state='normal')
        self.text_box.insert(tkinter.END, text)
        self.text_box.configure(state='disabled')

    def clearText(self, start_pos=1.0):
        self.text_box.configure(state='normal')
        self.text_box.delete(start_pos + 1, tkinter.END)
        self.text_box.configure(state='disabled')


if __name__ == '__main__':
    pass