from PyQt6.QtCore import QObject, pyqtSignal


class Signal(QObject):
    send_string = pyqtSignal(str)
    send_int = pyqtSignal(int)
    send_void = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.__string = "Hallo Welt"
        self.__int = 42

    def set_string(self, string):
        self.__string = string

        self.send_string.emit(string)

    def set_int(self, number):
        self.__int = number

        self.send_int.emit(number)

    def void(self):
        self.send_void.emit()
