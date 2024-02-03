# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_word_window_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_word_window(object):
    def setupUi(self, add_word_window):
        add_word_window.setObjectName("add_word_window")
        add_word_window.resize(253, 144)
        self.centralwidget = QtWidgets.QWidget(add_word_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_word_line = QtWidgets.QLineEdit(self.centralwidget)
        self.add_word_line.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_word_line.setFont(font)
        self.add_word_line.setText("")
        self.add_word_line.setObjectName("add_word_line")
        self.verticalLayout.addWidget(self.add_word_line)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(231, 52))
        self.frame.setMaximumSize(QtCore.QSize(245, 52))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.adding_pushButton = QtWidgets.QPushButton(self.frame)
        self.adding_pushButton.setObjectName("adding_pushButton")
        self.horizontalLayout.addWidget(self.adding_pushButton)
        self.cancel_add_pushButton = QtWidgets.QPushButton(self.frame)
        self.cancel_add_pushButton.setObjectName("cancel_add_pushButton")
        self.horizontalLayout.addWidget(self.cancel_add_pushButton)
        self.verticalLayout.addWidget(self.frame)
        add_word_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_word_window)
        QtCore.QMetaObject.connectSlotsByName(add_word_window)

    def retranslateUi(self, add_word_window):
        _translate = QtCore.QCoreApplication.translate
        add_word_window.setWindowTitle(_translate("add_word_window", "Add Word"))
        self.add_word_line.setPlaceholderText(_translate("add_word_window", "Type word"))
        self.adding_pushButton.setText(_translate("add_word_window", "Add"))
        self.cancel_add_pushButton.setText(_translate("add_word_window", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_word_window = QtWidgets.QMainWindow()
    ui = Ui_add_word_window()
    ui.setupUi(add_word_window)
    add_word_window.show()
    sys.exit(app.exec_())
