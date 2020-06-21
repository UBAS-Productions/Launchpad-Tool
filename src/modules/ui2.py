# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overview.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self):
        self.size = 620, 620

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(self.size[0], self.size[1])
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, self.size[0], self.size[1]))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(2)
        self.frames = []
        self.widgets = []
        self.verticalLayouts = []
        self.labels = []
        self.labels_2 = []
        self.labels_3 = []

        for x in range(8):
            for y in range(8):
                self.frames.append(QtWidgets.QFrame(self.gridLayoutWidget))
                self.frames[-1].setFrameShape(QtWidgets.QFrame.Box)
                self.frames[-1].setFrameShadow(QtWidgets.QFrame.Raised)
                self.frames[-1].setLineWidth(1)
                self.frames[-1].setMidLineWidth(0)
                self.frames[-1].setObjectName("frame")
                self.widgets.append(QtWidgets.QWidget(self.frames[-1]))
                self.widgets[-1].setGeometry(QtCore.QRect(10, 7, self.size[0] // 8, self.size[1] // 8))
                self.widgets[-1].setObjectName("widget")
                self.verticalLayouts.append(QtWidgets.QVBoxLayout(self.widgets[-1]))
                self.verticalLayouts[-1].setContentsMargins(0, 0, 0, 0)
                self.verticalLayouts[-1].setObjectName("verticalLayout")
                self.verticalLayouts[-1].setSpacing(0)
                self.labels.append(QtWidgets.QLabel(self.widgets[-1]))
                self.labels[-1].setObjectName("label")
                font = QtGui.QFont()
                font.setPointSize(7)
                self.labels[-1].setFont(font)
                self.labels[-1].setScaledContents(True)
                self.labels[-1].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                self.labels[-1].setText(str(x + y * 16))
                self.verticalLayouts[-1].addWidget(self.labels[-1])
                self.labels_2.append(QtWidgets.QLabel(self.widgets[-1]))
                self.labels_2[-1].setObjectName("label_2")
                font2 = QtGui.QFont()
                font2.setPointSize(10)
                self.labels_2[-1].setFont(font2)
                self.labels_2[-1].setScaledContents(True)
                self.labels_2[-1].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.verticalLayouts[-1].addWidget(self.labels_2[-1])
                self.labels_3.append(QtWidgets.QLabel(self.widgets[-1]))
                self.labels_3[-1].setObjectName("label_3")
                self.labels_3[-1].setFont(font)
                self.labels_3[-1].setScaledContents(True)
                self.labels_3[-1].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.verticalLayouts[-1].addWidget(self.labels_3[-1])
                self.gridLayout.addWidget(self.frames[-1], y, x, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Launchpad Overview"))
        # for label in self.labels:
        #     label.setText(_translate("Form", "TextLabel"))
        for label_2 in self.labels_2:
            label_2.setText(_translate("Form", "TextLabel"))
        for label_3 in self.labels_3:
            label_3.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
