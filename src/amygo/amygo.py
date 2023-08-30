import sys


from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from sqlalchemy.orm import Session

import logging

from amygo.data.database.database import Database
from amygo.data.database.entity_settings import SettingsEntity
from amygo.ui.main_window import MainWindow
from amygo.helpers import generate_exercise
from amygo.ui.model_expression_list import ExpressionListModel

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)


class Amygo:
    """Main software class"""
    def __init__(self):
        self.database = Database()
        with Session(self.database.engine) as session:
            session.expire_on_commit = False
            self.settings = session.get(SettingsEntity, "default")
            if self.settings is None:
                self.settings = SettingsEntity("default")
                session.add(self.settings)
                session.commit()
            session.commit()

        self.app = QApplication(sys.argv)
        self.window = MainWindow()

        self.window.actionExit.triggered.connect(self.window.close)
        self.window.buttonAdd.clicked.connect(self.button_add)
        self.window.buttonResults.clicked.connect(self.button_results)
        self.window.buttonClear.clicked.connect(self.button_clear)
        self.window.buttonSettingsCancel.clicked.connect(self.button_settings_cancel)
        self.window.buttonSettingsSave.clicked.connect(self.button_settings_save)
        self.model_expression_list = ExpressionListModel()
        self.window.tableViewExpressions.setModel(self.model_expression_list)

        self.button_settings_cancel()
        self.window.show()

    def button_add(self):
        expression = generate_exercise(self.settings)
        self.model_expression_list.expressions.append(expression)
        self.model_expression_list.layoutChanged.emit()

    def button_results(self):
        self.model_expression_list.show_results = not self.model_expression_list.show_results
        self.model_expression_list.layoutChanged.emit()

    def button_clear(self):
        self.model_expression_list.expressions = []
        self.model_expression_list.show_results = False
        self.model_expression_list.layoutChanged.emit()

    def button_settings_save(self):
        with Session(self.database.engine) as session:
            session.expire_on_commit = False
            self.settings = session.merge(self.settings)

            self.settings.addition_enabled = self.window.checkBoxAdditionEnabled.isChecked()
            self.settings.addition_minimum = self.window.spinBoxAdditionMinimum.value()
            self.settings.addition_maximum = max(self.settings.addition_minimum,
                                                 self.window.spinBoxAdditionMaximum.value())
            self.settings.subtraction_enabled = self.window.checkBoxSubstractionEnabled.isChecked()
            self.settings.subtraction_allow_negative = self.window.checkBoxSubstractionAllowNegative.isChecked()
            self.settings.subtraction_minimum = self.window.spinBoxSubstractionMinimum.value()
            self.settings.subtraction_maximum = max(self.settings.subtraction_minimum,
                                                    self.window.spinBoxSubstractionMaximum.value())
            self.settings.multiplication_enabled = self.window.checkBoxMultiplicationEnabled.isChecked()
            self.settings.multiplication_minimum = self.window.spinBoxMultiplicationMinimum.value()
            self.settings.multiplication_maximum = max(self.settings.multiplication_minimum,
                                                       self.window.spinBoxMultiplicationMaximum.value())
            self.settings.division_enabled = self.window.checkBoxDivisionEnabled.isChecked()
            self.settings.division_force_int = self.window.checkBoxDivisionForceInt.isChecked()
            self.settings.division_dividend_minimum = self.window.spinBoxDivisionDividendMinimum.value()
            self.settings.division_dividend_maximum = max(self.settings.division_dividend_minimum,
                                                          self.window.spinBoxDivisionDividendMaximum.value())
            self.settings.division_divisor_minimum = self.window.spinBoxDivisionDivisorMinimum.value()
            self.settings.division_divisor_maximum = max(self.settings.division_divisor_minimum,
                                                         self.window.spinBoxDivisionDivisorMaximum.value())
            session.commit()
        self.window.tabWidget.setCurrentIndex(0)

    def button_settings_cancel(self):
        self.window.checkBoxAdditionEnabled.setChecked(self.settings.addition_enabled)
        self.window.spinBoxAdditionMinimum.setValue(self.settings.addition_minimum)
        self.window.spinBoxAdditionMaximum.setValue(self.settings.addition_maximum)
        self.window.checkBoxSubstractionEnabled.setChecked(self.settings.subtraction_enabled)
        self.window.checkBoxSubstractionAllowNegative.setChecked(self.settings.subtraction_allow_negative)
        self.window.spinBoxSubstractionMinimum.setValue(self.settings.subtraction_minimum)
        self.window.spinBoxSubstractionMaximum.setValue(self.settings.subtraction_maximum)
        self.window.checkBoxMultiplicationEnabled.setChecked(self.settings.multiplication_enabled)
        self.window.spinBoxMultiplicationMinimum.setValue(self.settings.multiplication_minimum)
        self.window.spinBoxMultiplicationMaximum.setValue(self.settings.multiplication_maximum)
        self.window.checkBoxDivisionEnabled.setChecked(self.settings.division_enabled)
        self.window.checkBoxDivisionForceInt.setChecked(self.settings.division_force_int)
        self.window.spinBoxDivisionDividendMinimum.setValue(self.settings.division_dividend_minimum)
        self.window.spinBoxDivisionDividendMaximum.setValue(self.settings.division_dividend_maximum)
        self.window.spinBoxDivisionDivisorMinimum.setValue(self.settings.division_divisor_minimum)
        self.window.spinBoxDivisionDivisorMaximum.setValue(self.settings.division_divisor_maximum)

    def timer_process(self):
        print("Timer")

    def run(self):
        """Start the QT application, enter the event loop"""
        #timer = QTimer()
        #timer.timeout.connect(self.timer_process)
        #timer.start(1000)

        return_code = self.app.exec_()
        sys.exit(return_code)
