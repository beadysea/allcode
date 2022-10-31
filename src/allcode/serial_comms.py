from abc import ABC
import serial

class CommunicationDevice(ABC):
    """Communications Protocol"""
    # Implements a context manager
    def __enter__(self):
        ...

    def __exit__(self, *args):
        ...
    def _flush(self):
        ...
    
    def send_message(self, data: str) -> int:
        ...

class SerialDevice(CommunicationDevice):
    """Serial Device implementation of communication interface"""

    def __init__(self, baudrate: int = 115200, timeout: int = 1) -> None:
        self.serial = serial.serial_for_url(
            url='hwgrep://', baudrate=baudrate, timeout=timeout)
        self.serial.close()

    def _flush(self):
        count = self.serial.in_waiting
        while (count > 0):
            self.serial.readline().rstrip()
            count = self.serial.in_waiting
    
    # Methods implementing a communication interface
    def send_message(self, message: str) -> int:
        """Sends a message to the serial device.
        Return: the response or status.
        """
        with self.serial:
            #self._flush()
            status = self.serial.write(message.encode())
            response = self.serial.readline().decode()
            if response:
                return int(response)
            else: return status


