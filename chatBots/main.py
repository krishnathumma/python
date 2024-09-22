from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(600, 450)

        # Add chat area widgets
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the Input Fields
        self.input_filed = QLineEdit(self)
        self.input_filed.setGeometry(10, 340, 480, 45)
        self.input_filed.returnPressed.connect(self.send_message)

        # Add the Buttons
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 350, 100, 45)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_filed.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>ME: {user_input}</p>")
        self.input_filed.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
