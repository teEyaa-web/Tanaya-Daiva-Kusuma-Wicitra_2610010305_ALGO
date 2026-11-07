
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Memuat desain dari Qt Designer
        loadUi("to_do_list.ui", self)
        self.setWindowTitle("To-Do List")

        # Menghubungkan tombol dengan fungsi
        self.add_btn.clicked.connect(self.add_task)
        self.complete_btn.clicked.connect(self.complete_task)
        self.delete_btn.clicked.connect(self.delete_task)

        # Tekan Enter untuk menambahkan tugas
        self.task_input.returnPressed.connect(self.add_task)

    def add_task(self):
        task = self.task_input.text().strip()

        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
            self.task_input.setFocus()

    def complete_task(self):
        item = self.task_list.currentItem()

        if item:
            text = item.text()

            if not text.startswith("✓ "):
                item.setText(f"✓ {text}")
                item.setForeground(Qt.green)

    def delete_task(self):
        row = self.task_list.currentRow()

        if row >= 0:
            self.task_list.takeItem(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())