from datetime import datetime

from PySide6.QtGui import QFontDatabase, QPixmap
from PySide6.QtWidgets import QMainWindow

from amygo.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Application main window that is seeded with the generated class from .ui file"""

    NUM_EXPRESSIONS = 3

    def __init__(self):
        super().__init__()
        self.setupUi(self)
