
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import ast
import operator

# Operasi matematika yang diizinkan
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def safe_calculate(expression):
    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return OPERATORS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](evaluate(node.operand))
        raise ValueError("Ekspresi tidak valid")

    return evaluate(ast.parse(expression, mode="eval"))

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("kalkulator.ui", self)

        self.expression = ""

        # Hubungkan tombol sesuai objectName di Qt Designer
        self.btn7.clicked.connect(lambda: self.add_text("7"))
        self.btn8.clicked.connect(lambda: self.add_text("8"))
        self.btn9.clicked.connect(lambda: self.add_text("9"))
        self.btn4.clicked.connect(lambda: self.add_text("4"))
        self.btn5.clicked.connect(lambda: self.add_text("5"))
        self.btn6.clicked.connect(lambda: self.add_text("6"))
        self.btn1.clicked.connect(lambda: self.add_text("1"))
        self.btn2.clicked.connect(lambda: self.add_text("2"))
        self.btn3.clicked.connect(lambda: self.add_text("3"))
        self.btn0.clicked.connect(lambda: self.add_text("0"))

        self.btnPlus.clicked.connect(lambda: self.add_text("+"))
        self.btnMinus.clicked.connect(lambda: self.add_text("-"))
        self.btnMultiply.clicked.connect(lambda: self.add_text("*"))
        self.btnDivide.clicked.connect(lambda: self.add_text("/"))

        self.btnClear.clicked.connect(self.clear_display)
        self.btnEqual.clicked.connect(self.calculate)

        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

    def add_text(self, text):
        self.expression += text
        self.display.setText(self.expression)

    def clear_display(self):
        self.expression = ""
        self.display.clear()

    def calculate(self):
        try:
            result = safe_calculate(self.expression)
            self.expression = str(result)
            self.display.setText(self.expression)
        except (ValueError, SyntaxError, ZeroDivisionError, TypeError):
            self.expression = ""
            self.display.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
