
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QAction,
    QFileDialog,
    QMessageBox
)


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor Sederhana")
        self.setGeometry(300, 300, 600, 400)

        # Text area
        self.text_area = QTextEdit()
        self.setCentralWidget(self.text_area)

        # Create menu bar
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        new_action = QAction("New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Edit menu
        edit_menu = menubar.addMenu("Edit")

        undo_action = QAction("Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.text_area.undo)

        redo_action = QAction("Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        redo_action.triggered.connect(self.text_area.redo)

        cut_action = QAction("Cut", self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.text_area.cut)

        copy_action = QAction("Copy", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.text_area.copy)

        paste_action = QAction("Paste", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.text_area.paste)

        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # Toolbar
        toolbar = self.addToolBar("Tools")
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

    def new_file(self):
        self.text_area.clear()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if filename:
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    self.text_area.setText(file.read())
            except OSError as error:
                QMessageBox.warning(self, "Error", str(error))

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(self.text_area.toPlainText())

                QMessageBox.information(
                    self,
                    "Berhasil",
                    "File berhasil disimpan!"
                )
            except OSError as error:
                QMessageBox.warning(self, "Error", str(error))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())