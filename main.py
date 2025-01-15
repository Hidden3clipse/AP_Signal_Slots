from Signal import Signal
from Slot import Slot

if __name__ == '__main__':
    signal = Signal()
    slot = Slot()

    signal.send_string.connect(slot.slot_string)
    signal.send_int.connect(slot.slot_integer)
    signal.send_void.connect(slot.slot_void)

    signal.set_int(109)
    signal.void()
    signal.set_string("Mein Text")
