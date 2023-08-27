import sys


from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sqlalchemy.orm import Session

import logging

from amygo.data.models.database import Database
from amygo.data.settings import Settings
from amygo.ui.main_window import MainWindow
from amygo.helpers import generate_exercise
from amygo.ui.model_expression_list import ExpressionListModel

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
        self.window.buttonAdd.clicked.connect(self.button_add)
        self.window.buttonResults.clicked.connect(self.button_results)
        self.model_expression_list = ExpressionListModel()
        self.window.tableViewExpressions.setModel(self.model_expression_list)

        self.window.show()

    def button_add(self):
        expression = generate_exercise(None)
        self.model_expression_list.expressions.append(expression)
        self.model_expression_list.layoutChanged.emit()

    def button_results(self):
        self.model_expression_list.show_results = not self.model_expression_list.show_results
        self.model_expression_list.layoutChanged.emit()

    def timer_process(self):
        print("Timer")

    def run(self):
        """Start the QT application, enter the event loop"""
        #timer = QTimer()
        #timer.timeout.connect(self.timer_process)
        #timer.start(1000)

        return_code = self.app.exec_()
        sys.exit(return_code)
