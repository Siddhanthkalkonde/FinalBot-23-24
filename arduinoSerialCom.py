import serial

class ArduinoSerial:
    def __init__(self, baudrate, port):
        self.baudrate = baudrate
        self.port = port
        self.ser = None

    def open_port(self):
        """Open the serial port."""
        if self.ser is None or not self.ser.is_open:
            self.ser = serial.Serial(self.port, self.baudrate)
    
    def send_data(self, message):
        """Send data to the Arduino."""
        if self.ser and self.ser.is_open:
            self.ser.write(f"{message}\n".encode())  # Send the string as bytes followed by a newline character
        else:
            print("Serial connection is not open. Please open the connection first.")

    def close_port(self):
        """Close the serial port."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Serial connection closed.")
        else:
            print("Serial connection is already closed.")
