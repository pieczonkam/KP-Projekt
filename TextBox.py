from includes import *

class TextBox:
    def __init__(self, root_frame):
        self.is_open = False
        self.root_frame = root_frame
        self.text_box_frame = ttk.Frame(self.root_frame, style='Frame.TFrame')
        self.text_box = scrolledtext.ScrolledText(self.text_box_frame)
      
        # Long text for widget's behavior testing
        self.setText('''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ac sodales eros, a vulputate risus. Nam ullamcorper, magna vitae auctor gravida, risus orci semper sapien, in pharetra turpis augue ut lacus. Duis ullamcorper vestibulum accumsan. Donec in dui neque. Nulla efficitur venenatis leo vitae porta. Sed volutpat eu libero non imperdiet. Morbi efficitur in felis non pretium. Donec non nisi vestibulum, volutpat enim at, elementum nunc. Curabitur sapien mi, pulvinar sit amet orci et, facilisis vulputate ante. Ut viverra, odio pharetra pellentesque pretium, erat justo finibus orci, nec tristique velit risus et nibh. Mauris ac tortor eros. Vivamus vitae sagittis quam. Donec scelerisque diam libero, ac consectetur lectus congue non. In quis erat at magna mollis posuere pulvinar eget sem.

            Curabitur purus ligula, viverra vitae tempus in, lobortis eu elit. Vestibulum at consequat arcu. Pellentesque sollicitudin quis risus a consectetur. Aenean eget urna vulputate, tempus nisl nec, pellentesque orci. Integer nec turpis a leo dignissim rhoncus eu eget lectus. Integer urna ipsum, interdum ut turpis et, dignissim egestas neque. Quisque diam tellus, congue vitae sapien id, suscipit ultrices neque. Nulla luctus est quis nibh suscipit imperdiet. Sed eleifend vulputate venenatis.

            Nulla facilisi. Donec sagittis, mauris quis dapibus commodo, leo est dictum erat, ut mollis purus diam id nulla. Praesent ut nunc maximus, blandit arcu vitae, porttitor tellus. Nam hendrerit venenatis mi, a hendrerit urna aliquam sit amet. Quisque gravida, lacus quis molestie lacinia, arcu lectus pharetra magna, vitae maximus enim odio a tellus. Donec quis urna ac quam laoreet fermentum vel vitae risus. Vestibulum vulputate placerat iaculis. Suspendisse dignissim, diam quis volutpat lobortis, enim neque lacinia ex, et consectetur libero enim vitae massa. Integer condimentum quis lectus sed convallis. Quisque eu tortor augue.

            Suspendisse eleifend ligula quis nisi condimentum, eget tincidunt justo ultrices. Vivamus aliquam lacus at est facilisis, vel lacinia felis pretium. Proin eget ligula nunc. Phasellus vel ex sit amet neque tristique tincidunt at at felis. Quisque efficitur ultrices dolor, sit amet ullamcorper dolor porttitor at. Duis scelerisque et neque ut vestibulum. Morbi id vestibulum nunc.

            Curabitur laoreet viverra libero. Quisque dapibus imperdiet sapien, eu tristique felis maximus at. Aliquam elementum sit amet leo sollicitudin rhoncus. Nulla efficitur tellus mauris, a bibendum est elementum dictum. Maecenas nulla erat, consequat et rutrum fermentum, vestibulum cursus mauris. Nullam eget finibus lectus. Ut molestie odio tellus, a gravida tellus accumsan viverra. Aliquam mollis rhoncus quam, nec tempus mi tempus eget. Aliquam hendrerit facilisis nibh, et semper turpis dapibus luctus. In imperdiet maximus luctus.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ac sodales eros, a vulputate risus. Nam ullamcorper, magna vitae auctor gravida, risus orci semper sapien, in pharetra turpis augue ut lacus. Duis ullamcorper vestibulum accumsan. Donec in dui neque. Nulla efficitur venenatis leo vitae porta. Sed volutpat eu libero non imperdiet. Morbi efficitur in felis non pretium. Donec non nisi vestibulum, volutpat enim at, elementum nunc. Curabitur sapien mi, pulvinar sit amet orci et, facilisis vulputate ante. Ut viverra, odio pharetra pellentesque pretium, erat justo finibus orci, nec tristique velit risus et nibh. Mauris ac tortor eros. Vivamus vitae sagittis quam. Donec scelerisque diam libero, ac consectetur lectus congue non. In quis erat at magna mollis posuere pulvinar eget sem.

            Curabitur purus ligula, viverra vitae tempus in, lobortis eu elit. Vestibulum at consequat arcu. Pellentesque sollicitudin quis risus a consectetur. Aenean eget urna vulputate, tempus nisl nec, pellentesque orci. Integer nec turpis a leo dignissim rhoncus eu eget lectus. Integer urna ipsum, interdum ut turpis et, dignissim egestas neque. Quisque diam tellus, congue vitae sapien id, suscipit ultrices neque. Nulla luctus est quis nibh suscipit imperdiet. Sed eleifend vulputate venenatis.

            Nulla facilisi. Donec sagittis, mauris quis dapibus commodo, leo est dictum erat, ut mollis purus diam id nulla. Praesent ut nunc maximus, blandit arcu vitae, porttitor tellus. Nam hendrerit venenatis mi, a hendrerit urna aliquam sit amet. Quisque gravida, lacus quis molestie lacinia, arcu lectus pharetra magna, vitae maximus enim odio a tellus. Donec quis urna ac quam laoreet fermentum vel vitae risus. Vestibulum vulputate placerat iaculis. Suspendisse dignissim, diam quis volutpat lobortis, enim neque lacinia ex, et consectetur libero enim vitae massa. Integer condimentum quis lectus sed convallis. Quisque eu tortor augue.

            Suspendisse eleifend ligula quis nisi condimentum, eget tincidunt justo ultrices. Vivamus aliquam lacus at est facilisis, vel lacinia felis pretium. Proin eget ligula nunc. Phasellus vel ex sit amet neque tristique tincidunt at at felis. Quisque efficitur ultrices dolor, sit amet ullamcorper dolor porttitor at. Duis scelerisque et neque ut vestibulum. Morbi id vestibulum nunc.

            Curabitur laoreet viverra libero. Quisque dapibus imperdiet sapien, eu tristique felis maximus at. Aliquam elementum sit amet leo sollicitudin rhoncus. Nulla efficitur tellus mauris, a bibendum est elementum dictum. Maecenas nulla erat, consequat et rutrum fermentum, vestibulum cursus mauris. Nullam eget finibus lectus. Ut molestie odio tellus, a gravida tellus accumsan viverra. Aliquam mollis rhoncus quam, nec tempus mi tempus eget. Aliquam hendrerit facilisis nibh, et semper turpis dapibus luctus. In imperdiet maximus luctus.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ac sodales eros, a vulputate risus. Nam ullamcorper, magna vitae auctor gravida, risus orci semper sapien, in pharetra turpis augue ut lacus. Duis ullamcorper vestibulum accumsan. Donec in dui neque. Nulla efficitur venenatis leo vitae porta. Sed volutpat eu libero non imperdiet. Morbi efficitur in felis non pretium. Donec non nisi vestibulum, volutpat enim at, elementum nunc. Curabitur sapien mi, pulvinar sit amet orci et, facilisis vulputate ante. Ut viverra, odio pharetra pellentesque pretium, erat justo finibus orci, nec tristique velit risus et nibh. Mauris ac tortor eros. Vivamus vitae sagittis quam. Donec scelerisque diam libero, ac consectetur lectus congue non. In quis erat at magna mollis posuere pulvinar eget sem.

            Curabitur purus ligula, viverra vitae tempus in, lobortis eu elit. Vestibulum at consequat arcu. Pellentesque sollicitudin quis risus a consectetur. Aenean eget urna vulputate, tempus nisl nec, pellentesque orci. Integer nec turpis a leo dignissim rhoncus eu eget lectus. Integer urna ipsum, interdum ut turpis et, dignissim egestas neque. Quisque diam tellus, congue vitae sapien id, suscipit ultrices neque. Nulla luctus est quis nibh suscipit imperdiet. Sed eleifend vulputate venenatis.

            Nulla facilisi. Donec sagittis, mauris quis dapibus commodo, leo est dictum erat, ut mollis purus diam id nulla. Praesent ut nunc maximus, blandit arcu vitae, porttitor tellus. Nam hendrerit venenatis mi, a hendrerit urna aliquam sit amet. Quisque gravida, lacus quis molestie lacinia, arcu lectus pharetra magna, vitae maximus enim odio a tellus. Donec quis urna ac quam laoreet fermentum vel vitae risus. Vestibulum vulputate placerat iaculis. Suspendisse dignissim, diam quis volutpat lobortis, enim neque lacinia ex, et consectetur libero enim vitae massa. Integer condimentum quis lectus sed convallis. Quisque eu tortor augue.

            Suspendisse eleifend ligula quis nisi condimentum, eget tincidunt justo ultrices. Vivamus aliquam lacus at est facilisis, vel lacinia felis pretium. Proin eget ligula nunc. Phasellus vel ex sit amet neque tristique tincidunt at at felis. Quisque efficitur ultrices dolor, sit amet ullamcorper dolor porttitor at. Duis scelerisque et neque ut vestibulum. Morbi id vestibulum nunc.

            Curabitur laoreet viverra libero. Quisque dapibus imperdiet sapien, eu tristique felis maximus at. Aliquam elementum sit amet leo sollicitudin rhoncus. Nulla efficitur tellus mauris, a bibendum est elementum dictum. Maecenas nulla erat, consequat et rutrum fermentum, vestibulum cursus mauris. Nullam eget finibus lectus. Ut molestie odio tellus, a gravida tellus accumsan viverra. Aliquam mollis rhoncus quam, nec tempus mi tempus eget. Aliquam hendrerit facilisis nibh, et semper turpis dapibus luctus. In imperdiet maximus luctus.
        ''')

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

    def setText(self, text):
        self.text_box.configure(state='normal')
        self.text_box.delete(1.0, tkinter.END)
        self.text_box.insert(tkinter.INSERT, '\n' + text)
        self.text_box.configure(state='disabled')

    def appendText(self, text, newline=True):
        if newline:
            text = '\n' + text
        self.text_box.configure(state='normal')
        self.text_box.insert(tkinter.END, text)
        self.text_box.configure(state='disabled')

    def clearText(self):
        self.text_box.configure(state='normal')
        self.text_box.delete(1.0, tkinter.END)
        self.text_box.configure(state='disabled')

if __name__ == '__main__':
    pass