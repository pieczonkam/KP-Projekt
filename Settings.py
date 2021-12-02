class Settings:
    '''
        Settings class contains useful constants
    '''
    # Main window properties
    WINDOW_MIN_SIZE = (1200, 700)
    WINDOW_TITLE = 'Komputeryzacja Pomiarów Projekt'

    # Widgets properties
    TOP_MENU_HEIGHT = 50
    LEFT_MENU_WIDTH = 170
    INFO_HEIGHT = 40
    TOP_MENU_BUTTON_SIZE = (170, 50)
    LEFT_MENU_UPPER_BUTTON_SIZE = (170, 40)
    LEFT_MENU_LOWER_BUTTON_SIZE = (170, 60)
    LEFT_MENU_HEADER_WIDTH = 170
    TEXTBOX_LEFT_MARGIN = 15
    LEFT_MENU_LOWER_HEIGHT = 344
    LEFT_MENU_LOWER_ITEM_HEIGHT = 40
    SETTINGS_WINDOW_SIZE = (313, 180)
    SETTINGS_WINDOW_BUTTON_FRAME_HEIGHT = 42
    SETTINGS_WINDOW_BUTTON_WIDTH = 103
    SETTINGS_WINDOW_ENTRY_HEIGHT = 25

    # Colors
    FRAME_COLOR = '#333333'
    BUTTON_COLOR_LIGHT = '#616161'
    BUTTON_HOVER_COLOR_LIGHT = '#767676'
    BUTTON_ACTIVE_COLOR_LIGHT = '#999999'
    BUTTON_CLICKED_COLOR_LIGHT = '#999999'
    BUTTON_DISABLED_COLOR_DARK = '#ababab'
    BUTTON_COLOR_DARK = '#333333'
    BUTTON_HOVER_COLOR_DARK = '#434343'
    BUTTON_ACTIVE_COLOR_DARK = '#555555'
    BUTTON_CLICKED_COLOR_DARK = '#555555'
    TEXT_COLOR = '#ffffff'
    TEXT_DISABLED_COLOR = '#cecece'
    TEXTBOX_COLOR = '#333333'
    ENTRY_BG_COLOR = '#555555'
    ENTRY_SELECTED_TEXT_COLOR = '#767676'
    ENTRY_BORDER_NORMAL_COLOR = '#ababab'
    ENTRY_BORDER_ERROR_COLOR = '#ff0000'

    # Fonts
    FONT_HELVETICA_NORMAL_12 = ('Helvetica', 12)
    FONT_HELVETICA_NORMAL_14 = ('Helvetica', 14)
    FONT_HELVETICA_NORMAL_10 = ('Helvetica', 10)
    FONT_HELVETICA_BOLD_12 = ('Helvetica', 12, 'bold')
    FONT_HELVETICA_BOLD_16 = ('Helvetica', 16, 'bold')
    FONT_HELVETICA_BOLD_20 = ('Helvetica', 20, 'bold')

    # SettingsWindow
    RANGE = [0, 100]
    RANGE_DEFAULT = (0, 100)
    UNIT = '%'
    UNIT_DEFAULT = '%'
    MEASUREMENT_TYPE = 'Inne'
    MEASUREMENT_TYPE_DEFAULT = 'Inne'

    # Others
    CHART_DATA_LEN = 100
    DATA_ACQUISITION_FREQUENCY = 1.0


if __name__ == '__main__':
    pass