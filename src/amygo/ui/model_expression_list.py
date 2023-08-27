from PySide6.QtCore import QAbstractTableModel, Qt


class ExpressionListModel(QAbstractTableModel):
    def __init__(self, show_results=False):
        super(ExpressionListModel, self).__init__()
        self.expressions = []
        self.show_results = show_results

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return self.expressions[index.row()] + " ="
            else:
                if self.show_results:
                    return eval(self.expressions[index.row()])
                else:
                    return ""
        elif role == Qt.ItemDataRole.TextAlignmentRole:
            if index.column() == 0:
                return Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            else:
                return Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter

    def rowCount(self, index):
        return len(self.expressions)

    def columnCount(self, index):
        return 2
