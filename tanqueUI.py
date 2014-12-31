# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tanque.ui'
#
# Created: Wed Dec 31 18:58:44 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(386, 474)
        self.progressBar_Nivel = QtGui.QProgressBar(Form)
        self.progressBar_Nivel.setGeometry(QtCore.QRect(30, 60, 111, 381))
        self.progressBar_Nivel.setStyleSheet(_fromUtf8("QProgressBar {\n"
"border: 2px solid black;\n"
"text-align: top;\n"
"padding: 2px;\n"
"border-bottom-right-radius: 50px;\n"
"border-bottom-left-radius: 50px;\n"
"border-top-right-radius: 50px;\n"
"border-top-left-radius: 50px;\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #fff,\n"
"stop: 0.4999 #eee,\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee );\n"
"width: 15px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #78d,\n"
"stop: 0.4999 #46a,\n"
"stop: 0.5 #45a,\n"
"stop: 1 #238 );\n"
"border-bottom-right-radius: 50px;\n"
"border-bottom-left-radius: 50px;\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border: 1px solid black;\n"
"}"))
        self.progressBar_Nivel.setMinimum(0)
        self.progressBar_Nivel.setMaximum(100)
        self.progressBar_Nivel.setProperty("value", 30)
        self.progressBar_Nivel.setTextVisible(False)
        self.progressBar_Nivel.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_Nivel.setInvertedAppearance(False)
        self.progressBar_Nivel.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar_Nivel.setObjectName(_fromUtf8("progressBar_Nivel"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(160, 90, 199, 159))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 181, 121))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontaSlider = QtGui.QSlider(self.gridLayoutWidget)
        self.horizontaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontaSlider.setObjectName(_fromUtf8("horizontaSlider"))
        self.gridLayout.addWidget(self.horizontaSlider, 2, 0, 1, 1)
        self.lcdMaximo = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdMaximo.setObjectName(_fromUtf8("lcdMaximo"))
        self.gridLayout.addWidget(self.lcdMaximo, 1, 0, 1, 1)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.gridLayout.addWidget(self.lcdNumber_2, 1, 2, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.gridLayout.addWidget(self.horizontalSlider_2, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.Configurar_Alarmas = QtGui.QPushButton(self.gridLayoutWidget)
        self.Configurar_Alarmas.setObjectName(_fromUtf8("Configurar_Alarmas"))
        self.gridLayout.addWidget(self.Configurar_Alarmas, 3, 0, 1, 1)
        self.Confirmar_Alarmas = QtGui.QPushButton(self.gridLayoutWidget)
        self.Confirmar_Alarmas.setObjectName(_fromUtf8("Confirmar_Alarmas"))
        self.gridLayout.addWidget(self.Confirmar_Alarmas, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 400, 191, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 191, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.boton_conectar = QtGui.QPushButton(Form)
        self.boton_conectar.setGeometry(QtCore.QRect(170, 350, 191, 41))
        self.boton_conectar.setObjectName(_fromUtf8("boton_conectar"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 260, 201, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lcdNumber_1 = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_1.setObjectName(_fromUtf8("lcdNumber_1"))
        self.horizontalLayout.addWidget(self.lcdNumber_1)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.horizontaSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdMaximo.display)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_2.display)
        QtCore.QObject.connect(self.progressBar_Nivel, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_1.display)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Automatismo Tanque de Agua", None))
        self.progressBar_Nivel.setFormat(_translate("Form", "%p%", None))
        self.groupBox.setTitle(_translate("Form", "Alarmas", None))
        self.label_2.setText(_translate("Form", "Nivel Maximo", None))
        self.label.setText(_translate("Form", "Nivel Minimo", None))
        self.Configurar_Alarmas.setText(_translate("Form", "Configurar", None))
        self.Confirmar_Alarmas.setText(_translate("Form", "Confirmar", None))
        self.pushButton_2.setText(_translate("Form", "Salir", None))
        self.label_3.setText(_translate("Form", "Automatismo Nivel de tanque de agua", None))
        self.boton_conectar.setText(_translate("Form", "Conectar", None))
        self.groupBox_2.setTitle(_translate("Form", "Volumen de liquido en el tanque", None))
        self.label_4.setText(_translate("Form", "Litros", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

