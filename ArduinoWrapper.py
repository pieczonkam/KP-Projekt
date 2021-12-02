from tkinter.constants import SE
from pyfirmata import boards
from includes import *

class ArduinoWrapper(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app
        
        self.prepared = False
        self.running = False

        self.board = None
        self.ports = None

    def resetAppPins(self):
        self.app.pin_nmb_values_dict['analog'] = ['A' + str(i) for i in range(1)]
        self.app.pin_nmb_prev_values['analog'] = self.app.pin_nmb_values_dict['analog'][0]
        self.app.pin_nmb_values_dict['digital'] = ['D' + str(i) for i in range(1)]
        self.app.pin_nmb_prev_values['digital'] = self.app.pin_nmb_values_dict['digital'][0]
        self.app.pin_type_var.set('Analog')
        self.app.onPinTypeChange('Analog')

    def setAppPins(self):
        self.app.pin_nmb_values_dict['analog'] = ['A' + str(i) for i in range(len(self.board.analog))]
        self.app.pin_nmb_prev_values['analog'] = self.app.pin_nmb_values_dict['analog'][0]
        self.app.pin_nmb_values_dict['digital'] = ['D' + str(i) for i in range(2, len(self.board.digital))]
        self.app.pin_nmb_prev_values['digital'] = self.app.pin_nmb_values_dict['digital'][0]
        self.app.pin_type_var.set('Analog')
        self.app.onPinTypeChange('Analog')

    def connect(self):
        self.app.info_label['text'] = 'Łączenie...'
        self.start()

    def disconnect(self):
        self.app.info_label['text'] = 'Rozłączanie...'
        self.running = False
        
    def run(self):
        self.prepared = False

        self.ports = [port[0] for port in list(serial.tools.list_ports.comports())]
        for port in self.ports:
            try:
                self.board = pyfirmata.Arduino(port)
            except Exception as e:
                pass

        if not isinstance(self.board, type(None)):
            self.setAppPins()
            self.app.chart.clearChart()
            self.app.text_box.clearText(3.0)

            it = pyfirmata.util.Iterator(self.board)
            it.start()
            pin_nmb = prev_pin_nmb = self.app.pin_nmb_var.get()
            pin = int(pin_nmb[1:])
            if pin_nmb[0] == 'A':
                self.board.analog[pin].enable_reporting()

            self.app.info_label['text'] = 'Połączono (port %s)' % (self.board.name)
            self.prepared = True
            self.running = True

            t = 0.0
            while self.running:
                pin_nmb = self.app.pin_nmb_var.get()
                if pin_nmb != prev_pin_nmb:
                    self.app.info_label['text'] = 'Zmiana pinu...'
                    t = 0.0

                    prev_pin = int(prev_pin_nmb[1:])
                    if prev_pin_nmb[0] == 'A':
                        self.board.analog[prev_pin].disable_reporting()
                    prev_pin_nmb = pin_nmb
                    pin = int(pin_nmb[1:])
                    if pin_nmb[0] == 'A':
                        self.board.analog[pin].enable_reporting()
                    self.app.chart.clearChart()
                    self.app.text_box.clearText(3.0)
                    self.app.info_label['text'] = 'Połączono (port %s)' % (self.board.name)
                    
                if pin_nmb[0] == 'A':
                    val = self.board.analog[pin].read()
                else:
                    val = self.board.digital[pin].read()
                if isinstance(val, type(None)):
                    val = 0.0
                val = val * (Settings.RANGE[1] - Settings.RANGE[0]) + Settings.RANGE[0]

                self.app.chart.draw(val, t)
                self.app.text_box.appendText('%s\t\t\t%s' % (str(t), str(val) + ' ' + Settings.UNIT))
                
                t += Settings.DATA_ACQUISITION_FREQUENCY
                time.sleep(Settings.DATA_ACQUISITION_FREQUENCY)
            
            self.board.exit()
            self.board = None
        else:
            self.app.info_label['text'] = 'Nie udało się połączyć, rozłączanie...'
            time.sleep(2)
        
        self.resetAppPins()
        self.app.setButtonDisabled('left bottom', 1)
        self.app.info_label['text'] = 'Rozłączono'
        self.prepared = True
        self.app.arduino_wrapper = None

    
if __name__ == '__main__':
    pass