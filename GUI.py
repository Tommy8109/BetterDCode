import tkinter
from tkinter import *
from tkinter import ttk
import re
import datetime


class ChromiumDcode():
    def __init__(self):
        self.__title = "Test Application"
        self.__screen_geometry = "1000x700"
        self.__MainWindow = Tk()

        self.inputEntry = object
        self.output_entry = object
        self.user_timestamps = []

    def screen(self):
        mainScreen = self.__MainWindow
        mainScreen.title(self.__title)
        mainScreen.geometry(self.__screen_geometry)

        mainScreen.attributes("-topmost", False)
        mainScreen.resizable(False, False)

        lbl1 = ttk.Label(mainScreen, text='Chromium times', font=("Roboto", 24))
        lbl2 = ttk.Label(mainScreen, text='Converted times', font=("Roboto", 24))
        lbl1.place(x=90, y=64)
        lbl2.place(x=650, y=64)

        input_entry = tkinter.Text(mainScreen)
        input_entry.place(x=30, y=105, height = 400, width = 400)
        self.inputEntry = input_entry

        output_entry = tkinter.Text(mainScreen)
        output_entry.place(x=550, y=105, height=400, width=400)
        self.output_entry = output_entry

        btn = ttk.Button(mainScreen, text=' Convert timestamps ', command=self.retrieve_input)
        btn.place(x=35, y=550)

        btnClipboard = ttk.Button(mainScreen, text='Copy to clipboard', command=self.clipboard)
        btnClipboard.place(x= 190, y=550)

        mainScreen.option_add('*tearOff', False)
        mainScreen.mainloop()

    def retrieve_input(self):
        timestamps = self.inputEntry.get("1.0", END)
        regex = re.compile(r"[0-9]{17}")
        matches = regex.findall(timestamps)
        for m in matches:
            self.user_timestamps.append(m)
        self.converter()

    def clipboard(self):
        self.__MainWindow.clipboard_clear()
        self.__MainWindow.clipboard_append(self.output_entry.get("1.0", END))

    def converter(self):
        for stamp in self.user_timestamps:
            a = int(stamp) / 1000000  # divide by million to get microseconds
            a = a - 11644473600  # minus amount of seconds passed between 1 Jan 1970 and 1 Jan 1601
            t = datetime.datetime.fromtimestamp(a).strftime('%Y-%m-%d %H:%M:%S')
            self.output_entry.insert(tkinter.END, f"{t}\n")


if __name__ == '__main__':
    c = ChromiumDcode()
    c.screen()
















