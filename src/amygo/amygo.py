import sys


from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sqlalchemy.orm import Session

import logging

from amygo.data.models.database import Database
from amygo.data.settings import Settings
from amygo.main_window import MainWindow
from amygo.helpers import generate_exercise

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)


class Amygo:
    """Main software class"""
    def __init__(self):
        self.settings = Settings()
        self.database = Database()
        with Session(self.database.engine) as session:
            self.settings.import_from_database(session)
            session.commit()

        self.app = QApplication(sys.argv)
        self.window = MainWindow()

        self.window.actionExit.triggered.connect(self.window.close)
        self.window.buttonGenerate.clicked.connect(self.button_generate)
        self.window.buttonResults.clicked.connect(self.button_results)

        self.window.show()

    def button_generate(self):
        for i in range(self.window.NUM_EXPRESSIONS):
            expression, result = generate_exercise(None)
            getattr(self.window, f"expression{i}").setText(expression)
            getattr(self.window, f"result{i}").setText(result)

    def button_results(self):
        print("results")

    def timer_process(self):
        print("Timer")

    def run(self):
        """Start the QT application, enter the event loop"""
        #timer = QTimer()
        #timer.timeout.connect(self.timer_process)
        #timer.start(1000)

        return_code = self.app.exec_()
        sys.exit(return_code)
