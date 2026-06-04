import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit
)
from PyQt6.QtCore import Qt


class RobcoShell(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ROBCO TERMINK")
        self.showFullScreen()

        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.input = QLineEdit()

        layout.addWidget(self.output)
        layout.addWidget(self.input)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: #00ff00;
                font-family: monospace;
                font-size: 16px;
            }

            QTextEdit, QLineEdit {
                background-color: black;
                border: none;
                color: #00ff00;
            }
        """)

        self.boot_screen()

        self.input.returnPressed.connect(self.run_command)

    def boot_screen(self):
        self.output.append("""
=================================

     ROBCO INDUSTRIES (TM)

     ROBCO TERMLINK V1.0

     SYSTEM STATUS: ONLINE

Type HELP for available commands.

=================================
""")

    def run_command(self):
        command = self.input.text().strip().lower()

        self.output.append(f"> {command}")

        if command == "help":
            self.output.append("""
HELP
GAMES
FILES
SYSTEM
SETTINGS
CLEAR
EXIT
""")

        elif command == "clear":
            self.output.clear()

        elif command == "games":
            self.output.append("""
STEAM
HEROIC
LUTRIS
""")

        elif command == "exit":
            QApplication.quit()

        else:
            self.output.append("UNKNOWN COMMAND")

        self.input.clear()


app = QApplication(sys.argv)

window = RobcoShell()
window.show()

sys.exit(app.exec())
