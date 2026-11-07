
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QSpinBox, QMessageBox
)


class DataMahasiswa(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Mahasiswa")
        self.setGeometry(300, 200, 600, 400)

        self.data = []

        # Input data
        self.nim_input = QLineEdit()
        self.nama_input = QLineEdit()

        self.nilai_input = QSpinBox()
        self.nilai_input.setRange(0, 100)

        # Form
        form = QFormLayout()
        form.addRow("NIM:", self.nim_input)
        form.addRow("Nama:", self.nama_input)
        form.addRow("Nilai:", self.nilai_input)

        # Tabel
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["NIM", "Nama", "Nilai"]
        )

        # Tombol
        self.add_button = QPushButton("Tambah")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Hapus")
        self.clear_button = QPushButton("Clear")

        buttons = QHBoxLayout()
        buttons.addWidget(self.add_button)
        buttons.addWidget(self.update_button)
        buttons.addWidget(self.delete_button)
        buttons.addWidget(self.clear_button)

        # Layout utama
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(buttons)
        layout.addWidget(QLabel("Daftar Mahasiswa"))
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Hubungkan tombol
        self.add_button.clicked.connect(self.add_data)
        self.update_button.clicked.connect(self.update_data)
        self.delete_button.clicked.connect(self.delete_data)
        self.clear_button.clicked.connect(self.clear_form)

        self.table.itemSelectionChanged.connect(self.on_select)

    def add_data(self):
        nim = self.nim_input.text().strip()
        nama = self.nama_input.text().strip()
        nilai = self.nilai_input.value()

        if not nim or not nama:
            QMessageBox.warning(
                self, "Peringatan",
                "NIM dan Nama harus diisi!"
            )
            return

        # Periksa NIM duplikat
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).text() == nim:
                QMessageBox.warning(
                    self, "Peringatan",
                    "NIM sudah terdaftar!"
                )
                return

        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(nim))
        self.table.setItem(row, 1, QTableWidgetItem(nama))
        self.table.setItem(
            row, 2, QTableWidgetItem(str(nilai))
        )

        self.clear_form()

    def update_data(self):
        current = self.table.currentRow()

        if current < 0:
            QMessageBox.warning(
                self, "Peringatan",
                "Pilih data yang ingin diubah!"
            )
            return

        nim = self.nim_input.text().strip()
        nama = self.nama_input.text().strip()
        nilai = self.nilai_input.value()

        if not nim or not nama:
            QMessageBox.warning(
                self, "Peringatan",
                "NIM dan Nama harus diisi!"
            )
            return

        # Periksa NIM duplikat di baris lain
        for row in range(self.table.rowCount()):
            if (
                row != current
                and self.table.item(row, 0).text() == nim
            ):
                QMessageBox.warning(
                    self, "Peringatan",
                    "NIM sudah digunakan!"
                )
                return

        self.table.setItem(
            current, 0, QTableWidgetItem(nim)
        )
        self.table.setItem(
            current, 1, QTableWidgetItem(nama)
        )
        self.table.setItem(
            current, 2, QTableWidgetItem(str(nilai))
        )

        self.clear_form()

    def delete_data(self):
        current = self.table.currentRow()

        if current >= 0:
            jawaban = QMessageBox.question(
                self, "Konfirmasi",
                "Yakin ingin menghapus data ini?",
                QMessageBox.Yes | QMessageBox.No
            )

            if jawaban == QMessageBox.Yes:
                self.table.removeRow(current)
                self.clear_form()
        else:
            QMessageBox.warning(
                self, "Peringatan",
                "Pilih data yang ingin dihapus!"
            )

    def clear_form(self):
        self.nim_input.clear()
        self.nama_input.clear()
        self.nilai_input.setValue(0)
        self.table.clearSelection()

    def on_select(self):
        current = self.table.currentRow()

        if current >= 0:
            self.nim_input.setText(
                self.table.item(current, 0).text()
            )
            self.nama_input.setText(
                self.table.item(current, 1).text()
            )
            self.nilai_input.setValue(
                int(self.table.item(current, 2).text())
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataMahasiswa()
    window.show()
    sys.exit(app.exec_())
