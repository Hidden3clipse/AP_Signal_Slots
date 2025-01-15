from PyQt6.QtCore import QObject, pyqtSlot


class Slot(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot(str)
    def slot_string(self, string):
        print(string)

    @pyqtSlot(int)
    def slot_integer(self, integer):
        print(integer)

    @pyqtSlot()
    def slot_void(self):
        print("Signal erhalten.")
