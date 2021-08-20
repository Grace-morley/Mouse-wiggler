from PyQt5 import QtCore, QtWidgets, uic
import sys
import pyautogui


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("Wiggler_gui.ui", self)

        self.wiggle_conndition = False

        self.Start.clicked.connect(self.startpressed)
        self.Pause.clicked.connect(self.pausepressed)
        self.Quit.clicked.connect(self.quitpressed)

    @QtCore.pyqtSlot()
    def startpressed(self):
        self.Status.setText('Wiggling')
        self.wiggle_conndition = True
        while self.wiggle_conndition:
            pyautogui.move(0, 1)
            pyautogui.move(0, -1)
            pyautogui.press('shift')
            app.processEvents()

    @QtCore.pyqtSlot()
    def pausepressed(self):
        self.wiggle_conndition = False
        self.Status.setText('Not Currently Wiggling')
        app.processEvents()

    @QtCore.pyqtSlot()
    def quitpressed(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
