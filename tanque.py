# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 18:28:11 2014
<< Pinguino by Marin Purgar (marin.purgar@gmail.com)                         >>
@author: fAnDrEs (fabian.salamanca@openmailbox.org)
Modificada por Cristian O. Viola 2014/2015
"""

import sys
# Importar modulo Qt
from PyQt4 import QtCore, QtGui
# Importar el código del modulo compilado UI
from tanqueUI import Ui_Form
# Importamos Modulos para el manejo de USB
import usb

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------
# Crear una clase para nuestra ventana principal


class Principal(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)

        # Esto es siempre igual.
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Centramos el frame
        self.centrar()

        # Conectamos la senal de click de (boton_conectar) con el metodo inicio
        self.connect(self.ui.boton_conectar, QtCore.SIGNAL("clicked()"),
             self.inicio)
        # Conectamos la senal de click del boton (bt_llenado) con el metodo
        self.connect(self.ui.bt_llenado, QtCore.SIGNAL("toggled()"),
            self.on_bt_llenado_toggled)
        # Conectamos la senal de click del boton (bt_vaciado) con el metodo
        self.connect(self.ui.bt_vaciado, QtCore.SIGNAL("toggled()"),
            self.on_bt_vaciado_toggled)

        # Configurar nivel maximo y minimo del tanque
        self.connect(self.ui.bt_confirmar, QtCore.SIGNAL("toggled()"),
            self.on_bt_confirmar_toggled)

    def inicio(self):
        # Conexcion pinguino
        self.pinguino = Pinguino()
        if (self.pinguino.pinguinoOpen() == None):
            self.ui.textObs.append('El dispositivo no esta disponible. Revise la conexion Pinguino <--> PC')
            # Cerrar aplicacion de manera correcta.
            self.pinguino.pinguinoClose()
        else:
            # Activamos en la GUI el elemento y desactivamos boton conectar.
            self.ui.textObs.clear()
            self.ui.textObs.append('Conexion exitosa!')
            self.ui.boton_conectar.setEnabled(False)
            self.ui.bt_llenado.setEnabled(True)
            self.ui.bt_llenado.setCheckable(True)
            self.ui.bt_vaciado.setEnabled(True)
            self.ui.bt_vaciado.setCheckable(True)

            # Timer
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.nivel)
            self.timer.start(50)  # se ejecutará cada 500 mili segundos

#-------------------------------------------------------------------------------
    def centrar(self):
            # obtiene resolucion del usuario
            screen = QtGui.QDesktopWidget().screenGeometry()
            size = self.geometry()
            self.move((screen.width() - size.width()) / 2, (screen.height() -
            size.height()) / 2)

#-------------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_bt_llenado_pressed(self):  # si presiona el boton,
        self.ui.id_llenado.setStyleSheet("background-color: white;")
        self.ui.bt_llenado.setText("  ON")

    def on_bt_llenado_toggled(self, checked):
        if checked:
            self.rowOverride = True
            self.ui.bt_llenado.setText("  OFF")
            self.ui.id_llenado.setStyleSheet("background-color: green;")
        elif not checked:
            self.rowOverride = False
#-------------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_bt_vaciado_pressed(self):  # si presiona el boton,
        self.ui.id_vaciado.setStyleSheet("background-color: white;")
        self.ui.bt_vaciado.setText("  ON")

    def on_bt_vaciado_toggled(self, checked):
        if checked:
            self.rowOverride = True
            self.ui.bt_vaciado.setText("  OFF")
            self.ui.id_vaciado.setStyleSheet("background-color: green;")
        elif not checked:
            self.rowOverride = False
#-------------------------------------------------------------------------------
    @QtCore.pyqtSlot()
    def on_bt_confirmar_pressed(self):  # si presiona el boton,
        self.ui.bt_confirmar.setText("Confirmar")
        self.ui.lcdMaximo.setEnabled(True)
        self.ui.lcdMinimo.setEnabled(True)
        self.ui.sliderMax.setEnabled(True)
        self.ui.sliderMin.setEnabled(True)

    def on_bt_confirmar_toggled(self, checked):
        if checked:
            self.rowOverride = True
            self.ui.bt_confirmar.setText("Configurar")
            self.ui.lcdMaximo.setEnabled(False)
            self.ui.lcdMinimo.setEnabled(False)
            self.ui.sliderMax.setEnabled(False)
            self.ui.sliderMin.setEnabled(False)
        elif not checked:
            self.rowOverride = False

#-------------------------------------------------------------------------------
    def nivel(self):
        self.INTERVAL = 100  # intervalo (tiempo) de lectura
        deg = unichr(176).encode("utf-8")
        self.myString = ''

        # Obtiene los datos de la targeta Pinguino
        try:
            for i in self.pinguino.pinguinoRead(5, self.INTERVAL):
                if i > 47 and i < 58:    # ANSI 0,1,2,...,9
                    #print "valor actual",i # Debug
                    self.myString += chr(i)

        except usb.USBError as err:
            pass

        if len(self.myString) > 0:
            # Conversión a litros.
            self.nivel = (int(self.myString) * 100) / 1023
            # Asigna valor nivel tanque
            self.ui.progressBar_Nivel.setValue(self.nivel)
            if (self.nivel >= self.ui.sliderMax.value()):
                self.ui.nivel_min.setStyleSheet("QFrame { background-color: #00FF00}")  # VERDE
                self.ui.nivel_max.setStyleSheet("QFrame { background-color: #FF0000}")  # ROJO
            elif (self.nivel <= self.ui.sliderMin.value()):
                self.ui.nivel_min.setStyleSheet("QFrame { background-color: #FF0000}")  # ROJO
                self.ui.nivel_max.setStyleSheet("QFrame { background-color: #00FF00}")  # VERDE
            else:
                self.ui.nivel_max.setStyleSheet("QFrame { background-color: #00FF00}")  # VERDE
                self.ui.nivel_min.setStyleSheet("QFrame { background-color: #00FF00}")  # VERDE


#-------------------------------------------------------------------------------
# Pinguino Class by Marin Purgar (marin.purgar@gmail.com)
#-------------------------------------------------------------------------------
class Pinguino():

    VENDOR = 0x04D8
    PRODUCT = 0xFEAA
    CONFIGURATION = 0x01  # if bootloader v4.x
    #CONFIGURATION = 0x03 # if bootloader v2.x
    #print type(CONFIGURATION)
    INTERFACE = 0
    ENDPOINT_IN = 0x81  # if bootloader v4.x
    #ENDPOINT_IN = 0x82 # if bootloader v2.x
    ENDPOINT_OUT = 0x01

    device = None
    handle = None

    def __init__(self,):
        for bus in usb.busses():
            #print usb.busses()
            for dev in bus.devices:
                #print "vendor",dev.idVendor
                #print "idproduct",dev.idProduct
                if dev.idVendor == self.VENDOR and dev. idProduct == self.PRODUCT:
                    self.device = dev
        return None

    def pinguinoOpen(self):
        if not self.device:
            print >> sys.stderr, "El dispositivo no esta disponible!"
            return None
        try:
            self.handle = self.device.open()
            self.handle.setConfiguration(self.CONFIGURATION)
            self.handle.claimInterface(self.INTERFACE)
        except usb.USBError, err:
            print >> sys.stderr, err
            self.handle = None
        return self.handle

    def pinguinoClose(self):
        try:
            self.handle.releaseInterface()
        except Exception, err:
            print >> sys.stderr, err
        self.handle, self.device = None, None

    def pinguinoRead(self, length, timeout=0):
        return self.handle.bulkRead(self.ENDPOINT_IN, length, timeout)

    def pinguinoWrite(self, buffer, timeout=0):
        return self.handle.bulkWrite(self.ENDPOINT_OUT, buffer, timeout)

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------


def main():
    # Nuevamente, esto es estándar, será igual en cada
    # aplicación que escribas
    app = QtGui.QApplication(sys.argv)
    # Se crea una instancia de la clase
    ventana = Principal()
    # Se muestra el elemento en pantalla
    ventana.show()
    # Se ejecuta y expera a que termine la aplicación
    sys.exit(app.exec_())
    # Cierra la conexcion con el pinguino Correctamente
    Pinguino.pinguinoClose()

if __name__ == "__main__":
    main()