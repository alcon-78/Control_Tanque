# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tanque.ui'
#
# Created: Fri Jan 30 13:24:29 2015
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
        Form.setEnabled(True)
        Form.resize(371, 590)
        self.progressBar_Nivel = QtGui.QProgressBar(Form)
        self.progressBar_Nivel.setGeometry(QtCore.QRect(40, 60, 111, 391))
        self.progressBar_Nivel.setStyleSheet(_fromUtf8("QProgressBar {\n"
"border: 1px solid black;\n"
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
        self.groupBox.setGeometry(QtCore.QRect(160, 50, 201, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 187, 113))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.sliderMax = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderMax.setProperty("value", 90)
        self.sliderMax.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMax.setObjectName(_fromUtf8("sliderMax"))
        self.gridLayout.addWidget(self.sliderMax, 2, 0, 1, 1)
        self.lcdMinimo = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdMinimo.setProperty("intValue", 15)
        self.lcdMinimo.setObjectName(_fromUtf8("lcdMinimo"))
        self.gridLayout.addWidget(self.lcdMinimo, 1, 2, 1, 1)
        self.sliderMin = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderMin.setProperty("value", 15)
        self.sliderMin.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMin.setObjectName(_fromUtf8("sliderMin"))
        self.gridLayout.addWidget(self.sliderMin, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.bt_confirmar = QtGui.QPushButton(self.gridLayoutWidget)
        self.bt_confirmar.setCheckable(True)
        self.bt_confirmar.setObjectName(_fromUtf8("bt_confirmar"))
        self.gridLayout.addWidget(self.bt_confirmar, 3, 2, 1, 1)
        self.lcdMaximo = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdMaximo.setProperty("intValue", 90)
        self.lcdMaximo.setObjectName(_fromUtf8("lcdMaximo"))
        self.gridLayout.addWidget(self.lcdMaximo, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 530, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.boton_conectar = QtGui.QPushButton(Form)
        self.boton_conectar.setGeometry(QtCore.QRect(20, 480, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_conectar.setFont(font)
        self.boton_conectar.setObjectName(_fromUtf8("boton_conectar"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 210, 201, 71))
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
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(180, 290, 160, 90))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, -50, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.bt_llenado = QtGui.QPushButton(self.widget)
        self.bt_llenado.setEnabled(False)
        self.bt_llenado.setGeometry(QtCore.QRect(20, 20, 120, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PMincho"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bt_llenado.setFont(font)
        self.bt_llenado.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"text-align: left;\n"
"border-bottom-left-radius: 25px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-left-radius: 25px;\n"
"border-top-right-radius: 10px;\n"
"background-color: #D3D3D3;"))
        self.bt_llenado.setCheckable(True)
        self.bt_llenado.setChecked(False)
        self.bt_llenado.setObjectName(_fromUtf8("bt_llenado"))
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(15, 0, 140, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.id_llenado = QtGui.QFrame(self.widget)
        self.id_llenado.setGeometry(QtCore.QRect(98, 30, 31, 31))
        self.id_llenado.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: #FFFAFA;"))
        self.id_llenado.setFrameShape(QtGui.QFrame.StyledPanel)
        self.id_llenado.setFrameShadow(QtGui.QFrame.Raised)
        self.id_llenado.setObjectName(_fromUtf8("id_llenado"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(180, 380, 160, 90))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_9 = QtGui.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(50, -50, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.bt_vaciado = QtGui.QPushButton(self.widget_2)
        self.bt_vaciado.setEnabled(False)
        self.bt_vaciado.setGeometry(QtCore.QRect(20, 20, 120, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PMincho"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bt_vaciado.setFont(font)
        self.bt_vaciado.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"text-align: left;\n"
"border-bottom-left-radius: 25px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-left-radius: 25px;\n"
"border-top-right-radius: 10px;\n"
"background-color: #D3D3D3;"))
        self.bt_vaciado.setCheckable(True)
        self.bt_vaciado.setObjectName(_fromUtf8("bt_vaciado"))
        self.label_12 = QtGui.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(5, 0, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.id_vaciado = QtGui.QFrame(self.widget_2)
        self.id_vaciado.setGeometry(QtCore.QRect(98, 30, 31, 31))
        self.id_vaciado.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"background-color: #FFFAFA;"))
        self.id_vaciado.setFrameShape(QtGui.QFrame.StyledPanel)
        self.id_vaciado.setFrameShadow(QtGui.QFrame.Raised)
        self.id_vaciado.setObjectName(_fromUtf8("id_vaciado"))
        self.nivel_max = QtGui.QFrame(Form)
        self.nivel_max.setGeometry(QtCore.QRect(10, 100, 21, 21))
        self.nivel_max.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;\n"
"\n"
""))
        self.nivel_max.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_max.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_max.setObjectName(_fromUtf8("nivel_max"))
        self.nivel_min = QtGui.QFrame(Form)
        self.nivel_min.setGeometry(QtCore.QRect(10, 390, 21, 21))
        self.nivel_min.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;"))
        self.nivel_min.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_min.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_min.setObjectName(_fromUtf8("nivel_min"))
        self.textObs = QtGui.QTextBrowser(Form)
        self.textObs.setGeometry(QtCore.QRect(130, 491, 221, 61))
        self.textObs.setObjectName(_fromUtf8("textObs"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 550, 151, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 470, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.sliderMax, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdMaximo.display)
        QtCore.QObject.connect(self.sliderMin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdMinimo.display)
        QtCore.QObject.connect(self.progressBar_Nivel, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_1.display)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textObs.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Automatismo Tanque de Agua", None))
        self.progressBar_Nivel.setFormat(_translate("Form", "%p%", None))
        self.groupBox.setTitle(_translate("Form", "Alarmas", None))
        self.label_2.setText(_translate("Form", "Nivel Maximo", None))
        self.label.setText(_translate("Form", "Nivel Minimo", None))
        self.bt_confirmar.setText(_translate("Form", "Configurar", None))
        self.pushButton_2.setText(_translate("Form", "Salir", None))
        self.label_3.setText(_translate("Form", "Automatismo Nivel de tanque de agua", None))
        self.boton_conectar.setText(_translate("Form", "Conectar", None))
        self.groupBox_2.setTitle(_translate("Form", "Volumen de liquido en el tanque", None))
        self.label_4.setText(_translate("Form", "Litros", None))
        self.label_5.setText(_translate("Form", "BOMBA LLENADO", None))
        self.bt_llenado.setText(_translate("Form", "   ON", None))
        self.label_11.setText(_translate("Form", "BOMBA DE LLENADO", None))
        self.label_9.setText(_translate("Form", "BOMBA LLENADO", None))
        self.bt_vaciado.setText(_translate("Form", "   ON", None))
        self.label_12.setText(_translate("Form", "VALVULA DE VACIADO", None))
        self.pushButton.setText(_translate("Form", "Limpiar cuadro", None))
        self.label_6.setText(_translate("Form", "Observaciones:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

