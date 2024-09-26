class BluetoothNotPowerOn(Exception):
    def __init__(self, message):
        super().__init__(message)


class BluetoothNotPowerOff(Exception):
    def __init__(self, message):
        super().__init__(message)


class ElementNotClicked(Exception):
    def __init__(self, message):
        super().__init__(message)


class ElementNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class ElementNotClickable(Exception):
    def __init__(self, message):
        super().__init__(message)


class ElementDisplayed(Exception):
    def __init__(self, message):
        super().__init__(message)


class DataNotAvailable(Exception):
    def __init__(self, message):
        super().__init__(message)
