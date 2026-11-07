
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        loadUi("konverter_suhu.ui", self)

        # Hubungkan input dengan fungsi konversi
        self.input_c.textChanged.connect(self.convert)

    def convert(self):
        try:
            celsius = float(self.input_c.text())
            fahrenheit = (celsius * 9 / 5) + 32

            self.output_f.setText(f"{fahrenheit:.2f} °F")

        except ValueError:
            self.output_f.setText("Invalid input")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureConverter()
    window.show()
    sys.exit(app.exec_())
