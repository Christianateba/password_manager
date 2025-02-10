import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit

class PasswordManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Password Manager")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        
        self.label = QLabel("Enter Website/Service:")
        self.input_field = QLineEdit()
        self.generate_btn = QPushButton("Generate Password")
        self.password_display = QTextEdit()
        self.password_display.setReadOnly(True)
        
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.generate_btn)
        layout.addWidget(self.password_display)
        
        self.generate_btn.clicked.connect(self.generate_password)
        
        self.setLayout(layout)
    
    def generate_password(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.setText(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManagerUI()
    window.show()
    sys.exit(app.exec_())
